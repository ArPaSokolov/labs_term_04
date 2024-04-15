from flask import Flask, render_template
from schema import factory, Story


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def show_all_news():
    all_stories = session.query(Story)
    return render_template("all news.html", stories=all_stories)


if __name__ == "__main__":
    session = factory()
    app.run(host="127.0.0.1", port=4321)
