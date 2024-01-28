from router.book import Books_Router

class Router:

    def __init__(self, app):
        self.app = app
        self.book = Books_Router(self.app)

    def routes(self):
        self.book.routes()

    def run(self, **kwargs):
        self.app.run(**kwargs)

