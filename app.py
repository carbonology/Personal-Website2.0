import tornado.ioloop
import tornado.web
import tornado.httpserver
import os.path

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('home.html')

class tetradHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('tetrad.html')

class presentationHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('presentation.html')

settings = dict(
	template_path = os.path.join(os.path.dirname(__file__), "templates"),
	static_path = os.path.join(os.path.dirname(__file__), "static"),
	debug = True
)

handlers = [(r'/', MainHandler),
			('/tetrad', tetradHandler),
			('/presentation', presentationHandler)]

def app():
	print('Server Running...')
	print('Press ctrl + c to close')
	application = tornado.web.Application(handlers, **settings)
	#http_server = tornado.httpserver.HTTPServer(application)
	#port = int(os.environ.get("PORT", 5000))
	#http_server.listen(port)
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()

#Start the server at port n
if __name__ == "__main__":
	app()