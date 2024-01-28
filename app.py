from flask import Flask
from router.router import Router

app_flask = Flask(__name__)
     
if __name__ == "__main__":
    app = Router(app_flask)
    app.routes()
    app.run(debug=True)
    