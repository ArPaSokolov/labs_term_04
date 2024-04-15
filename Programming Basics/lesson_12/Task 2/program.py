from flask import Flask, render_template
from schema import factory, Story, User, Category


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def show_all_news():
    all_stories = session.query(Story)
    return render_template("all news.html", stories=all_stories)


@app.route("/add-story/<ttl>/<cntn>/<auth>/<restricted>/<topics>")
def add_new_story(ttl, cntn, auth, restricted, topics):
    new_story = Story()
    new_story.title = ttl
    new_story.content = cntn
    if restricted == "0":
        new_story.is_private = False
    else:
        new_story.is_private = True

    u = session.query(User).filter(User.username == auth).first()
    u.stories.append(new_story)

    cats = session.query(Category).filter(
        Category.name.in_(topics.split(","))
    )
    for c in cats:
        new_story.categories.append(c)

    try:
        session.commit()
        return "OK"
    except:
        session.rollback()
        return "Failed"

if __name__ == "__main__":
    session = factory()
    app.run(host="127.0.0.1", port=4321)

