from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from jinja2 import FileSystemLoader, Environment

env = Environment(loader=FileSystemLoader('views'))

def IndexPage(request):
    return Response(env.get_template('index.html').render(link="""<a href="about/aboutme.html">About me!</a>"""))

def AboutMePage(request):
    return Response(env.get_template('about/aboutme.html').render(link="""<a href="/">Index!</a>"""))

if __name__ == '__main__':
    config = Configurator()
    config.add_route('index', '/')
    config.add_view(IndexPage, route_name='index')
    config.add_route('about', '/about/aboutme.html')
    config.add_view(AboutMePage, route_name='about')
    app = config.make_wsgi_app()
    server = make_server('localhost', 8080, app)
    print("Serving localhost on 8080...")
    server.serve_forever()