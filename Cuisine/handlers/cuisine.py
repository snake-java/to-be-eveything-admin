import tornado.web


class CuisineHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello")