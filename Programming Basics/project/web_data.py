from wtforms import Form
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, RadioField, \
    SelectField, SelectMultipleField, DateField, PasswordField, validators, SubmitField

from wtforms.validators import InputRequired, NumberRange, DataRequired
from wtforms.widgets import ListWidget, CheckboxInput
from flask_wtf import FlaskForm


class RegisterForm(Form):
    first_name = StringField(
        "Имя",
        validators=[InputRequired(message="Вы не указали имя.")]
    )
    last_name = StringField(
        "Фамилия",
        validators=[InputRequired(message="Вы не указали фамилию.")]
    )
    gender = StringField(
        "Пол",
        validators=[InputRequired(message="Вы не указали пол.")]
    )
    username = StringField(
        "Логин",
        validators=[InputRequired(message="Вы не указали логин.")]
    )
    password = PasswordField(
        "Пароль",
        validators=[
            InputRequired(message="Вы не указали пароль."),
            validators.EqualTo('confirm_password', message='Пароли не совпадают')
        ]
    )
    confirm_password = PasswordField(
        "Подтвердить пароль",
        validators=[InputRequired(message="Вы не указали пароль.")]
    )

    submit = SubmitField("Зарегистрироваться")


class LoginForm(Form):
    username = StringField(
        "Логин",
        validators=[InputRequired(message="Вы не указали логин.")]
    )
    password = PasswordField(
        "Пароль",
        validators=[
            InputRequired(message="Вы не указали пароль."),
        ]
    )

    submit = SubmitField("Войти")


class EditForm(Form):
    first_name = StringField(
        "Имя"
    )
    last_name = StringField(
        "Фамилия"
    )
    gender = StringField(
        "Пол"
    )
    username = StringField(
        "Логин"
    )
    password = PasswordField(
        "Пароль",
        validators=[
            validators.EqualTo('confirm_password', message='Пароли не совпадают')
        ]
    )
    confirm_password = PasswordField(
        "Подтвердить пароль"
    )

    submit = SubmitField('Изменить')


class SendForm(Form):
    receiver = SelectField(
        "Получатель",
        coerce=int,
        validators=[InputRequired()]
    )

    content = StringField(
        "Сообщение"
    )
    submit = SubmitField('Отправить')
