

from flask import Flask
from api.v1.auth.auth import auth_app
from api.v1.scraper.scraper  import scraper_app

app = Flask(__name__)


app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(scraper_app, url_prefix="/scraper")


# index
@app.route("/", methods=["GET"])
def index():
    return app.send_static_file("html/index.html")


# css files
@app.route("/css/<file>", methods=["GET"])
def css_file(file):
    return app.send_static_file("css/" + str(file))


# js files
@app.route("/js/<file>", methods=["GET"])
def js_file(file):
    return app.send_static_file("js/" + str(file))


# html files
@app.route("/html/<file>", methods=["GET"])
def html_file(file):
    return app.send_static_file("html/" + str(file))


if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)