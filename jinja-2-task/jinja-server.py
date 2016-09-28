from wsgiref.simple_server import make_server
from jinja2 import FileSystemLoader, Environment
import selector

class Base(object):

	def __init__(self,environ,start_response,link,template):
		self.env = environ
		self.start_response = start_response
		self.templates  = Environment(loader=FileSystemLoader('src'))
		self.template = template
		self.link = link

	def __iter__(self):
		self.start_response('200 OK',[("Content-Type", "text/html")])
		yield self.templates.get_template(self.template).render(link=self.link)

class IndexPage(Base):
	def __init__(self,environ,start_response):
		Base.__init__(self, 
					environ, 
					start_response, 
					"""<a href="aboutme/aboutme.html">About me!</a>""", 
					"index.html")

class AboutPage(Base):
	def __init__(self,environ,start_response):
		Base.__init__(self,
					environ,
					start_response, 
					"""<a href="/">Index</a>""", 
					"aboutme/aboutme.html")


if __name__ == '__main__':
	#'RESTful' mapping, lol
	# app =  selector.Selector()
	# app.add('/',GET=IndexPage)
	# app.add("/index.html",GET=IndexPage)
	# app.add("/aboutme/aboutme.html",GET=AboutPage)

	_server = make_server('localhost', 8000, app)
	print('Serving localhost on port 8000...')
	_server.serve_forever()
