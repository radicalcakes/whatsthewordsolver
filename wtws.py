import re
import os.path
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata

from bs4 import BeautifulSoup, NavigableString
from tornado.options import define, options
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=9)
pipe = r.pipeline()

tornado.options.define("port", default=1922, help="run on the given port", type=int)

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            #/user, /matches  are for the api
            (r"/", IndexHandler),
            # (r"/answers", AnswerHandler),
            # (r"/bakasubo", ScrapeHandler),
       
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=False,
            autoescape=None
        )
        tornado.web.Application.__init__(self, handlers, **settings)



class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html",answers=False)

	def post(self):
		self.letters = self.get_argument("letters")
		self.length = self.get_argument("length")
		words = r.smembers(self.length)
		l = []
		for word in words:
			s = ""
			for char in word:
				if char in self.letters:
					s += char
					print s
			if len(s) == int(self.length):
				l.append(s)
		self.render("index.html", answers=l)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
	main()