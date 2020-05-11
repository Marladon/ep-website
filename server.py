from aiohttp import web
import aiohttp_jinja2
import jinja2
import asyncio
import posixpath
import ssl
from os.path import isfile

from data.products import products, friendly_name
from data.other import intro, technical, address, more
import data.download as download_data
from data.walker.walk import FileInfo, walk
from translator.translator import translator, all_languages

from typing import Dict, List, Optional

files: Dict[str, Dict[str, List[FileInfo]]] = {}  # Download page files, must be initialized


routes = web.RouteTableDef()


def translatable_template(func):
    async def handler(request):
        language = request.match_info.get("language", "ru")
        tr = translator(language)

        result = await func(request)

        # Link to current page without /ru or /en prefix
        current_link_nolang = posixpath.join(*request.path.split("/")[2:])

        # Links to ru, en, ... etc versions of current page
        languages_links = {f"{lang}_link": posixpath.join("/"+lang, current_link_nolang) for lang in all_languages}
        return {"tr": tr,
                "lang": language,
                **languages_links,
                **result}
    return handler


def base_template(func):
    async def handler(request):
        result = await func(request)
        return {"address": address, **result}
    return translatable_template(handler)


@routes.get("/")
async def index(request):
    raise web.HTTPFound(location="/ru/")  # redirect to default language


@routes.get("/{language}/")
@aiohttp_jinja2.template("index.html")
@base_template
async def index(request):
    return {"intro": intro,
            "products": products,
            "technical": technical,
            "more": more
            }


@routes.get("/{language}/product/{product}/")
@aiohttp_jinja2.template("download.html")
@base_template
async def download(request):
    product = request.match_info["product"]
    return {"product_name": friendly_name(product),
            "all_software": files[product],
            "version": download_data.version,
            "release_date": download_data.release_date,
            "size": download_data.size,
            "link": download_data.link,
            "download": download_data.download,
            "software_type": download_data.software_category_by_name
            }


# TODO: use nginx
routes.static('/static', "view/static")


async def walk_periodic(path: str, url_prefix: str):
    global files
    while True:
        files = walk(path, url_prefix)
        await asyncio.sleep(300)  # Update every 5 minutes


def _app_factory() -> web.Application:
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('view/templates'))

    app.router.add_routes(routes)

    return app


async def _server_factory(keyfile: Optional[str] = None, certfile: Optional[str] = None) -> web.TCPSite:
    app = _app_factory()
    runner = web.AppRunner(app)
    await runner.setup()

    ssl_ctx = None
    if keyfile or certfile:
        ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        ssl_ctx.load_cert_chain(certfile=certfile, keyfile=keyfile)

    site = web.TCPSite(runner, ssl_context=ssl_ctx)
    return site


async def main():
    walker_coro = walk_periodic("view/static/download", "/static/download")  # periodic run
    asyncio.create_task(walker_coro)

    http_server_coro = (await _server_factory()).start()
    asyncio.create_task(http_server_coro)

    cert, key = "fullchain.pem", "privkey.pem"
    if isfile(cert) and isfile(key):
        https_server_coro = (await _server_factory(keyfile=key, certfile=cert)).start()
        asyncio.create_task(https_server_coro)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
