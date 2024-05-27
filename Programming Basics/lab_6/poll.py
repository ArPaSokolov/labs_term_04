from flask import Flask, render_template, request, redirect, url_for, make_response
import uuid

app = Flask(__name__)

# ответы
answers = {
    "optimist": 0,
    "pessimist": 0
}


# главная
@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    user_id = request.cookies.get('user_id')
    if not user_id:
        user_id = str(uuid.uuid4())
        response = make_response(render_template('index.html'))
        response.set_cookie('user_id', user_id)
        return response
    else:
        return f"Вы уже проходили этот тест! Вы - {request.cookies.get('result')}"


# вопрос 1
@app.route('/question1', methods=['GET', 'POST'])
def question1():
    if request.method == 'POST':
        if "glass" in request.form:
            if request.form["glass"] == "full":
                answers["optimist"] += 1
            elif request.form["glass"] == "empty":
                answers["pessimist"] += 1
        response = make_response(redirect(url_for('question2')))
        return response

    if request.method == "GET":
        return render_template('question1.html')


# вопрос 2
@app.route('/question2', methods=['GET', 'POST'])
def question2():
    if request.method == 'POST':
        if "fear" in request.form:
            if request.form["fear"] == "yes":
                answers["pessimist"] += 1
            elif request.form["fear"] == "no":
                answers["optimist"] += 1
        response = make_response(redirect(url_for('question3')))
        return response

    if request.method == "GET":
        return render_template('question2.html')


# вопрос 3
@app.route('/question3', methods=['GET', 'POST'])
def question3():
    if request.method == 'POST':
        if "fear" in request.form:
            if request.form["sense"] == "yes":
                answers["optimist"] += 1
            elif request.form["fear"] == "no":
                answers["pessimist"] += 1
        response = make_response(redirect(url_for('result')))
        return response

    if request.method == "GET":
        return render_template('question3.html')


# результаты
@app.route('/answers', methods=["GET", "POST"])
def result():
    if request.method == "GET":
        if answers["optimist"] > answers["pessimist"]:
            answer = "оптимист"
        else:
            answer = "пессимист"

        response = make_response(render_template('answers.html', result=answer))
        response.set_cookie('result', str(answer))
        return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4321)