import datetime as dt

from schema import factory, User, Story, Category
from web_data import StoryForm, LoginForm, UpdateForm
from flask import Flask, request, render_template, redirect, flash, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
# manager = Manager(app)


@app.errorhandler(404)
def router_not_found(e):
    return render_template('page-not-found.html')


@app.route('/')
@app.route('/index')
def show_all_news():
    result = session.query(Story)
    return render_template('all-news-page.html', stories=result)


@app.route('/add-story', methods=["GET", "POST"])
def add_new_story():
    all_users = session.query(User)
    all_categories = session.query(Category)

    story_form = StoryForm()

    story_form.story_author.choices = [
        (u.id, f'{u.first_name} {u.last_name} ({u.username})') for u in all_users
    ]

    story_form.story_topics.choices = [(c.id, c.name) for c in all_categories]

    if request.method == "GET":
        story_form.creation_date.data = dt.datetime.now()
        return render_template('add-story-page.html', f=story_form)

    if request.method == "POST":
        story_form.process(request.form)

        if not story_form.validate():
            return render_template('add-story-page.html', f=story_form)

        new_story = Story()
        new_story.title = story_form.story_title.data
        new_story.content = story_form.story_content.data
        new_story.author_id = story_form.story_author.data

        if story_form.scope.data == 'public':
            new_story.is_private = False

        if story_form.creation_date.data is not None:
            new_story.created_on = story_form.creation_date.data

        print(story_form.story_topics.data)

        for category_id in story_form.story_topics.data:
            c = session.get(Category, category_id)
            new_story.categories.append(c)

        try:
            session.add(new_story)
            session.commit()
            return redirect('/index')
        except Exception as e:
            session.rollback()
            return f"Что-то пошло не так. Ошибка: {e}"


@app.route('/edit-story/<int:story_id>', methods=["GET", "POST"])
def edit_existing_story(story_id):
    story = session.get(Story, story_id)
    if story is None:
        return f"Истории с идентификатором {story_id} не существует."

    all_users = session.query(User)
    all_categories = session.query(Category)

    story_form = StoryForm()

    story_form.story_author.choices = [
        (u.id, f'{u.first_name} {u.last_name} ({u.username})') for u in all_users
    ]

    story_form.story_topics.choices = [(c.id, c.name) for c in all_categories]

    if request.method == "GET":
        story_form.story_title.data = story.title
        story_form.story_content.data = story.content
        story_form.story_author.data = story.author_id

        if story.is_private:
            story_form.scope.data = "private"
        else:
            story_form.scope.data = "public"

        story_form.story_topics.data = [c.id for c in story.categories]
        story_form.creation_date.data = story.created_on
        story_form.responsibility.data = True

        return render_template("edit-story-page.html", story_id=story.id, f=story_form)

    if request.method == "POST":
        story_form.process(request.form)

        if not story_form.validate():
            return render_template("edit-story-page.html", story_id=story.id, f=story_form)

        story.title = story_form.story_title.data
        story.content = story_form.story_content.data

        story.author_id = story_form.story_author.data

        if story_form.scope.data == 'public':
            story.is_private = False

        story.created_on = story_form.creation_date.data

        story.categories.clear()
        for category_id in story_form.story_topics.data:
            c = session.get(Category, category_id)
            story.categories.append(c)

        try:
            session.commit()
            return redirect('/index')
        except Exception as e:
            session.rollback()
            return f"Что-то пошло не так. Ошибка: {e}"


@app.route('/delete-story/<int:story_id>')
def delete_existing_story(story_id):
    story = session.get(Story, story_id)
    if story is None:
        return f"Истории с идентификатором {story_id} не существует."

    try:
        session.delete(story)
        session.commit()
        return redirect('/index')
    except Exception as e:
        session.rollback()
        return f"Что-то пошло не так. Ошибка: {e}"


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if request.method == "GET":
        return render_template('login.html', title='Sign In', form=login_form)

    if request.method == "POST":
        if not login_form.validate_on_submit():
            flash('Ошибка валидации формы регистрации', 'error')
            return render_template('login.html', title='Sign In', form=login_form)

        new_user = User(
            username=request.form.get('username'),
            first_name=request.form.get('first_name'),
            last_name=request.form.get('last_name'),
            password=request.form.get('password'),
        )

        try:
            session.add(new_user)
            session.commit()
            print("Зарегистрирован новый пользователь:", new_user)
            return redirect('/index')
        except Exception as e:
            session.rollback()
            return f"Что-то пошло не так. Ошибка: {e}"


@app.route('/update-profile', methods=['GET', 'POST'])
def update():
    update_form = UpdateForm()

    all_users = session.query(User)
    update_form.profile.choices = [
        (u.id, f'{u.first_name} {u.last_name} ({u.username})') for u in all_users
    ]

    if request.method == "GET":
        return render_template('update-profile.html', form=update_form)

    if request.method == 'POST' and update_form.validate():
        if not update_form.validate_on_submit():
            return render_template('update-profile.html', form=update_form)

        user_id = update_form.profile.data
        user = session.get(User, user_id)

        # Обновляем данные пользователя
        if update_form.first_name.data:
            user.first_name = update_form.first_name.data
        if update_form.last_name.data:
            user.last_name = update_form.last_name.data
        if update_form.username.data:
            user.username = update_form.username.data
        if update_form.password.data:
            user.password = update_form.password.data

        try:
            session.commit()
            print("Данные обновлены для:", user)
            return redirect('/index')
        except Exception as e:
            session.rollback()
            return f"Что-то пошло не так. Ошибка: {e}"

    return render_template('update-profile.html', form=update_form)



if __name__ == "__main__":
    session = factory()
    app.run(host="127.0.0.1", port=4321)
