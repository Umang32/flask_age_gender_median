from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)

now = dt.datetime.now().year


@app.route('/')
def home():

    return render_template("index.html", num=now)

@app.route('/guess/<name>')
def guess(name):
    gender = f"https://api.genderize.io?name={name}"
    age = f"https://api.agify.io?name={name}"

    response_gender = requests.get(gender)
    response_age = requests.get(age)

    response_gender = response_gender.json()
    response_age = response_age.json()
    gender = response_gender['gender']
    age = response_age['age']
    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)


