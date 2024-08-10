from flask import Flask, request, render_template
from markupsafe import escape

# Documentation: https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hi(name):
    return f"Hi, {escape(name)}!"


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("index.html", name=name)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # return do_the_login()
        pass
    else:
        # return show_the_login_form()
        pass


@app.route("/chart")
def chart():
    labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
    data = [12, 19, 3, 5, 2, 3]

    return render_template("chart.html", labels=labels, data=data)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
