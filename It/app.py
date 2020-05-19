import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define,options


from handlers.it import ItHandler
define('port', default='8889',help="Listening Port",type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/it',ItHandler)
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