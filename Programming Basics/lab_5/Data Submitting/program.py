import datetime as dt

from schema import factory, User, Story, Category
from flask import Flask, request, render_template, redirect


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def show_all_news():
    result = session.query(Story)
    return render_template('all news.html', stories=result)


@app.route('/add-story')
def add_new_story():
    all_users = session.query(User)
    all_categories = session.query(Category)
    return render_template('our-form.html',
                           users=all_users, categories=all_categories, errors=[])


@app.route('/info-receiver', methods=['POST'])
def process_information():
    errors = []
    print(request.form)

    if 'story-title' not in request.form \
            or request.form['story-title'] is None \
            or request.form['story-title'] == '':
        errors.append('Вы не указали заголовок новости.')

    if 'story-content' not in request.form \
            or request.form['story-content'] is None \
            or request.form['story-content'] == '':
        errors.append('Вы не указали содержание новости.')

    if 'story-author' not in request.form \
            or request.form['story-author'] is None \
            or request.form['story-author'] == '':
        errors.append('Вы не указали ID автора новости.')
    elif not request.form['story-author'].isdigit():
        errors.append('ID автора указан в недопустимом формате.')
    else:
        user_id = int(request.form['story-author'])
        u = session.get(User, user_id)
        if u is None:
            errors.append('Указан ID несуществующего автора.')

    if 'scope' not in request.form \
            or request.form['scope'] is None \
            or request.form['scope'] == '':
        errors.append('Вы не указали степень доступности новости.')
    elif request.form['scope'] not in ('public', 'private', 'super-private'):
        errors.append('Степень доступности новости указана в недопустимом формате.')

    if 'creation-date' not in request.form \
            or request.form['creation-date'] is None \
            or request.form['creation-date'] == '':
        date_of_creation = None
    else:
        try:
            date_of_creation = dt.datetime.strptime(request.form['creation-date'], '%Y-%m-%d')
        except:
            date_of_creation = None

    if 'story-topics' not in request.form \
            or request.form['story-topics'] is None:
        errors.append('Вы не отметили, к каким темам относится эта новость.')
    else:
        try:
            # request.form['story-topics'] -> '1'
            # request.form.getlist['story-topics'] -> ['1', '2', '4', '3', '6', '10']
            topics_id = [int(x) for x in map(int, request.form.getlist('story-topics'))]
        except:
            errors.append('Список тем, к которым относится новость, указан в недопустимом формате.')

        topics = []
        for x in topics_id:
            c = session.get(Category, x)
            if c is None:
                errors.append('Указан ID несуществующей темы.')
                break
            else:
                topics.append(c)

    if 'severity' not in request.form \
            or request.form['severity'] is None \
            or request.form['severity'] == '':
        errors.append('Вы не указали степень важности новости.')
    elif not request.form['severity'].isdigit():
        errors.append('Степень важности новости должна быть целым числом от 1 до 5.')
    else:
        severity_level = int(request.form['severity'])
        if not 1 <= severity_level <= 5:
            errors.append('Степень важности новости должна быть целым числом от 1 до 5.')

    if 'responsibility' not in request.form \
            or request.form['responsibility'] is None \
            or request.form['responsibility'] == '':
        errors.append('Вы не указали, готовы ли взять на себя ответственность за публикацию новостей спорного характера.')
    elif request.form['responsibility'] != '1':
        errors.append('Согласие/несогласие об ответственности указано в недопустимом формате.')

    if errors:
        all_users = session.query(User)
        all_categories = session.query(Category)
        return render_template('our-form.html',
                               users=all_users, categories=all_categories, errors=errors)
    else:
        new_story = Story()
        new_story.title = request.form['story-title']
        new_story.content = request.form['story-content']

        if request.form['scope'] == 'public':
            new_story.is_private = False

        if date_of_creation is not None:
            new_story.created_on = date_of_creation

        for c in topics:
            new_story.categories.append(c)

        u.stories.append(new_story)

        try:
            session.commit()
            return redirect('/index')
        except:
            session.rollback()
            all_users = session.query(User)
            all_categories = session.query(Category)
            return render_template('our-form.html',
                                   users=all_users, categories=all_categories,
                                   errors=['Не удалось добавить новость в базу данных.']
                                   )


if __name__ == "__main__":
    session = factory()
    app.run(host="127.0.0.1", port=4321)
