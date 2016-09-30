from bottle import Bottle, run
from jinja2 import FileSystemLoader, Environment

env = Environment(loader=FileSystemLoader('src'))
app = Bottle()

@app.get('/')
@app.get('/index.html')
def IndexPage():
    return env.get_template('index.html').render(link="""<a href="about/aboutme.html">About me!</a>""")

@app.get('/about/aboutme.html')
def AboutMePage():
    return env.get_template('about/aboutme.html').render(link="""<a href="/">Index!</a>""")

if __name__=="__main__":
    run(app, host='localhost', port=8000)
