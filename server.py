from aiohttp import web
import aiohttp_jinja2
import jinja2
import asyncio
import posixpath

from data.products import products, friendly_name
from data.other import intro, technical, address
import data.download as download_data
from data.walker.walk import FileInfo, walk
from translator.translator import translator, all_languages

from typing import Dict, List

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
            }


@routes.get("/{language}/product/{product}/")
@aiohttp_jinja2.template("download.html")
@base_template
async def download(request):
    product = request.match_info["product"]
    return {"product_name": friendly_name(product),
            "software_types": files[product],
            "version": download_data.version,
            "release_date": download_data.release_date,
            "size": download_data.size,
            "link": download_data.link,
            "download": download_data.download,
            "software_friendly_name": download_data.software_friendly_name
            }


# TODO: use nginx
routes.static('/static', "view/static")


async def walk_periodic(path: str, url_prefix: str):
    global files
    while True:
        await asyncio.sleep(3600)  # update every hour
        files = walk(path, url_prefix)


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('view/templates'))

app.router.add_routes(routes)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    runner = web.AppRunner(app)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner)
    loop.run_until_complete(site.start())
    files = walk("view/static/download", "/static/download")  # run once before server run
    loop.create_task(walk_periodic("view/static/download", "/static/download"))  # periodic run

    loop.run_forever()
