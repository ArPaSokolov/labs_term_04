import datetime as dt
import uuid

from schema import factory, User, Message
from web_data import RegisterForm, EditForm, LoginForm, SendForm
from flask import Flask, request, render_template, redirect, flash, url_for, make_response
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
# manager = Manager(app)

@app.errorhandler(404)
def router_not_found(e):
    return render_template('page-not-found.html')


# @app.route('/')
# @app.route('/index')
# def show_all_news():
    # result = session.query(Story)
    # return render_template('all-news-page.html', stories=result)

@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()

    if request.method == "GET":
        return render_template('register.html', form=register_form)

    if request.method == "POST":
        register_form.process(request.form)
        if not register_form.validate():
            flash('Ошибка валидации формы регистрации', 'error')
            return render_template('register.html', form=register_form)

        new_user = User(
            username=request.form.get('username'),
            first_name=request.form.get('first_name'),
            last_name=request.form.get('last_name'),
            password=request.form.get('password'),
            gender=request.form.get('gender')
        )

        try:
            session.add(new_user)
            session.commit()
            print("Зарегистрирован новый пользователь:", new_user)
            return redirect('/login')
        except Exception as e:
            session.rollback()
            return f"Что-то пошло не так. Ошибка: {e}"


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if request.method == "GET":
        return render_template('login.html', title='Sign In', form=login_form)

    if request.method == "POST":
        login_form.process(request.form)
        if not login_form.validate():
            flash('Ошибка валидации формы регистрации', 'error')
            return render_template('login.html', title='Sign In', form=login_form)

        username = request.form.get('username')
        password = request.form.get('password')

        try:
            user = session.query(User).filter(User.username == username).one()
            if user.password == password:
                # Пароль совпадает, пользователь найден
                response = make_response(redirect('/edit-user'))
                response.set_cookie('username', username)
                return response
            else:
                # Пароль не совпадает
                flash('Неправильный пароль', 'error')
                return render_template('login.html', title='Sign In', form=login_form)
        except NoResultFound:
            # Пользователь не найден
            flash('Пользователь не найден', 'error')
            return render_template('login.html', title='Sign In', form=login_form)


@app.route('/edit-user', methods=['GET', 'POST'])
def edit():
    edit_form = EditForm()

    if request.method == "GET":
        username = request.cookies.get('username')
        if username:
            # Куки пользователя найдены
            return render_template('edit-user.html', form=edit_form)
        else:
            # Куки пользователя не найдены, перенаправляем на страницу логина
            return redirect('/login')

    if request.method == 'POST':
        edit_form.process(request.form)
        if not edit_form.validate():
            print("Ошибка")
            return render_template('edit-user.html', form=edit_form)

        user_name = request.cookies.get('username')
        user = session.query(User).filter(User.username == user_name).first()

        # Обновляем данные пользователя
        if edit_form.first_name.data:
            user.first_name = edit_form.first_name.data
        if edit_form.last_name.data:
            user.last_name = edit_form.last_name.data
        if edit_form.username.data:
            user.username = edit_form.username.data
        if edit_form.gender.data:
            user.first_name = edit_form.gender.data
        if edit_form.password.data:
            user.password = edit_form.password.data

        try:
            session.commit()
            print("Данные обновлены для:", user)
            response = make_response(redirect('/login'))
            response.delete_cookie('username')
            return response

        except Exception as e:
            print("мы тут")
            session.rollback()
            return f"Что-то пошло не так. Ошибка: {e}"

    return render_template('login.html', form=edit_form)


@app.route('/send', methods=['GET', 'POST'])
def send():
    send_form = SendForm()

    all_users = session.query(User)
    send_form.receiver.choices = [
        (u.id, f'{u.first_name} {u.last_name} ({u.username})') for u in all_users
    ]

    if request.method == 'POST':
        send_form.process(request.form)
        if not send_form.validate():
            print("Ошибка")
            return render_template('send.html', form=send_form)

        receiver_id = int(send_form.receiver.data)

        content = send_form.content.data

        # Получение отправителя из куки
        sender_username = request.cookies.get('username')
        sender = session.query(User).filter(User.username == sender_username).first()

        # Создание объекта сообщения
        message = Message(sender_id=sender.id, receiver_id=receiver_id, content=content)

        try:
            session.add(message)
            session.commit()
            response = make_response(redirect(url_for('send')))
            response.delete_cookie('username')
            return response

        except Exception as e:
            print("мы тут")
            session.rollback()
            return f"Что-то пошло не так. Ошибка: {e}"

    if request.method == 'GET':
        username = request.cookies.get('username')
        if username:
            # Куки пользователя найдены
            return render_template("send.html", form=send_form)
        else:
            # Куки пользователя не найдены, перенаправляем на страницу логина
            return redirect('/login')


@app.route('/inbox', methods=['GET'])
def inbox():
    # Получение имени пользователя из куки
    username = request.cookies.get('username')

    # Получение отправителя из куки
    receiver_username = request.cookies.get('username')
    receiver = session.query(User).filter(User.username == receiver_username).first()
    current_id = receiver.id

    if username:
        # Получение всех сообщений пользователя из базы данных
        messages = session.query(Message).filter(Message.receiver_id == current_id).all()
        return render_template('inbox.html', messages=messages)
    else:
        return redirect('/login')


@app.route('/sent', methods=['GET'])
def sent():
    # Получение имени пользователя из куки
    username = request.cookies.get('username')

    # Получение отправителя из базы данных по имени пользователя
    sender_username = request.cookies.get('username')
    sender = session.query(User).filter(User.username == sender_username).first()
    current_id = sender.id

    if sender:
        # Получение всех отправленных сообщений пользователя из базы данных
        messages = session.query(Message).filter_by(sender_id=sender.id).all()

        return render_template('sent.html', messages=messages)
    else:
        return redirect('/login')


@app.route('/logout', methods=['GET'])
def logout():
    # Удаление куки с именем пользователя
    session.delete("username")

    return redirect('/login')


if __name__ == "__main__":
    session = factory()
    app.run(host="127.0.0.1", port=4321)
