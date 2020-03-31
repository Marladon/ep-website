from aiohttp import web
import aiohttp_jinja2
import jinja2


routes = web.RouteTableDef()


@routes.get("/")
@aiohttp_jinja2.template("index.html")
async def index(request):
    return {}


routes.static('/static', "view/static")


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('view/templates'))

app.router.add_routes(routes)

web.run_app(app)
