from aiohttp import web
import aiohttp_jinja2
import jinja2
import gettext
from data.products import products
from data.other import intro, technical
from data.utils import _


routes = web.RouteTableDef()


@routes.get("/")
async def index(request):
    raise web.HTTPFound(location="/en/")


@routes.get("/{language}/")
@aiohttp_jinja2.template("index.html")
async def index(request):
    language = request.match_info["language"]
    if language == "ru":
        translator = _
    else:
        translator = gettext.translation(language, localedir='locale', languages=[language]).gettext
    return {"intro": translator(intro),
            "products": [p.translated(gettext.gettext) for p in products],
            "technical": translator(technical)}


@routes.get("/download")
@aiohttp_jinja2.template("download.html")
async def download(request):
    return {}


# TODO: use nginx
routes.static('/static', "view/static")


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('view/templates'))

app.router.add_routes(routes)

web.run_app(app)
