from aiohttp import web
import aiohttp_jinja2
import jinja2
from data.products import products
from data.other import intro, technical, address
from translator.translator import translator


routes = web.RouteTableDef()


def translatable_template(func):
    async def handler(request):
        language = request.match_info.get("language", "ru")
        tr = translator(language)

        result = await func(request)

        return {"tr": tr, "lang": language, **result}
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
            "address": address
            }


@routes.get("/{language}/product/{product}/")
@aiohttp_jinja2.template("download.html")
@base_template
async def download(request):
    return {}


# TODO: use nginx
routes.static('/static', "view/static")


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('view/templates'))

app.router.add_routes(routes)

web.run_app(app)
