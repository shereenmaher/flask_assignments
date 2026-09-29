from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)

app.secret_key = "great_number_game_secret"


@app.route("/")
def index():
    
    if "number" not in session:
        session["number"] = random.randint(1, 100)

    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def guess():
    user_guess = int(request.form["guess"])
    number = session["number"]

    if user_guess > number:
        session["result"] = "Too high!"
    elif user_guess < number:
        session["result"] = "Too low!"
    else:
        session["result"] = "Correct! You guessed the number!"

    return redirect("/")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)