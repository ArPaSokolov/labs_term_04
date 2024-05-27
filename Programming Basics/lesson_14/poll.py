from flask import Flask, render_template, request, redirect, make_response

answers = {
    "mommy": {"yes": 0, "no": 0, "notsure": 0},
    "daddy": {"yes": 0, "no": 0, "notsure": 0},
}

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def show_questions():
    if "voted" in request.cookies and request.cookies["voted"] == "OK":
        return "Вы уже голосовали!"
    else:
        return render_template("question.html")

@app.route("/results", methods=["GET","POST"])
def process_answers():
    if request.method == "GET":
        return render_template("answers.html", answers=answers)

    if request.method == "POST":
        if "voted" in request.cookies and request.cookies["voted"] == "OK":
            return "Вы уже голосовали!"
        else:
            if "mommy" in request.form:
                if request.form["mommy"] == "yes":
                    answers["mommy"]["yes"] += 1
                elif request.form["mommy"] == "no":
                    answers["mommy"]["no"] += 1
                elif request.form["mommy"] == "notsure":
                    answers["mommy"]["notsure"] += 1
            if "daddy" in request.form and \
                    request.form["daddy"] in ("yes", "no", "notsure"):
                answers["daddy"][request.form["daddy"]] += 1

            response = make_response(render_template("answers.html", answers=answers))

            response.set_cookie("voted", "OK")

            return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4321)
