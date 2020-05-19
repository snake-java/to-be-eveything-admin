import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define,options


from handlers.joke import JokeHandler
define('port', default='8890',help="Listening Port",type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/joke',JokeHandler)
        ]
        settings = dict(
            debug=True,
            template_path='templates'
        )
        super().__init__(handlers,**settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = Application()
    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()