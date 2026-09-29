from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = "ninja_gold_secret"


@app.route("/")
def index():
    if "gold" not in session:
        session["gold"] = 0

    if "activities" not in session:
        session["activities"] = []

    return render_template(
        "index.html",
        gold=session["gold"],
        activities=session["activities"]
    )


@app.route("/process_money", methods=["POST"])
def process_money():

    building = request.form["building"]

    if building == "farm":
        gold_earned = random.randint(10, 20)
        message = f"Earned {gold_earned} gold from the farm!"

    elif building == "cave":
        gold_earned = random.randint(5, 10)
        message = f"Earned {gold_earned} gold from the cave!"

    elif building == "house":
        gold_earned = random.randint(2, 5)
        message = f"Earned {gold_earned} gold from the house!"

    elif building == "casino":
        gold_earned = random.randint(-50, 50)

        if gold_earned >= 0:
            message = f"Entered the casino and earned {gold_earned} gold!"
        else:
            message = f"Entered the casino and lost {abs(gold_earned)} gold!"

    session["gold"] += gold_earned

    session["activities"].append(message)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)