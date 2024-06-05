from flask import Flask, render_template, request, redirect, url_for, make_response
import uuid

app = Flask(__name__)

# ответы
answers = {}  # глобальная переменная


# главная
@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    user_id = request.cookies.get('user_id')  # получаем куки с айди пользователя

    if not user_id:  # новый пользователь
        user_id = str(uuid.uuid4())  # генерируем айди
        answers[user_id] = {
            "optimist": 0,
            "pessimist": 0
        }
        response = make_response(render_template('index.html'))
        response.set_cookie('user_id', user_id)  # генерируем куки
        return response

    else:  # пользователь имеет куки
        response = make_response(redirect(url_for('results')))
        return response


# вопросы
@app.route('/questions', methods=['GET', 'POST'])
def questions():

    user_id = request.cookies.get('user_id')
    result = request.cookies.get('result')
    if user_id and result:  # пользователь уже проходил тест
        response = make_response(redirect(url_for('results')))
        return response

    if request.method == 'POST':

        answers[user_id] = {  # обновляем результаты
            "optimist": 0,
            "pessimist": 0
        }

        if "glass" in request.form:  # вопрос 1
            if request.form["glass"] == "full":
                answers[user_id]["optimist"] += 1
            elif request.form["glass"] == "empty":
                answers[user_id]["pessimist"] += 1

        if "fear" in request.form:  # вопрос 2
            if request.form["fear"] == "yes":
                answers[user_id]["pessimist"] += 1
            elif request.form["fear"] == "no":
                answers[user_id]["optimist"] += 1

        if "truth" in request.form:  # вопрос 3
            if request.form["truth"] == "yes":
                answers[user_id]["optimist"] += 1
            elif request.form["truth"] == "no":
                answers[user_id]["pessimist"] += 1

        response = make_response(redirect(url_for('results')))
        return response

    if request.method == "GET":
        return render_template('questions.html')


# результаты
@app.route('/results', methods=["GET", "POST"])
def results():
    if request.method == "GET":
        user_id = request.cookies.get('user_id')
        if not request.cookies.get('result'):
            if answers[user_id]["optimist"] > answers[user_id]["pessimist"]:  # пользователь больше оптимист, чем пессимист
                result = "оптимист"
            else:
                result = "пессимист"
        else:
            result = request.cookies.get('result')

        response = make_response(render_template('results.html', result=result))
        response.set_cookie("result", result)
        return response

    if request.method == "POST":
        # Перенаправляем пользователя обратно на страницу вопросов со сюрошенным результатом
        response = make_response(redirect(url_for('questions')))
        response.delete_cookie("result")
        return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4321)

# browser://settings/siteData
