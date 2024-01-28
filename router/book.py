from controller.book import Books_Controller

class Books_Router:

    def __init__(self, flask_app):
        self.app = flask_app
    
    def routes(self):
        self.app.add_url_rule('/books', 'books', Books_Controller.getBooks,methods=['GET'])
        self.app.add_url_rule('/books/new', 'new_book', Books_Controller.createBook,methods=['POST'])