from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 10)
print(random_number)


@app.route('/')
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/DhiRqIsofVMi7fWNBQ/giphy.gif' width=200px>")


@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return ("<h1 style='color: red'> TOO HIGH TRY AGAIN </h1>"
                "<img src='https://media.giphy.com/media/MwrQvTZA9Puuc/giphy.gif' width=200px>")
    elif guess < random_number:
        return ("<h1 style='color: red'> TOO LOW TRY AGAIN </h1>"
                "<img src='https://media.giphy.com/media/dKpEvFHdGsZBRuszpv/giphy.gif' width=200px>")
    else:
        return ("<h1 style='color: green'> RIGHT ON </h1>"
                "<img src='https://media.giphy.com/media/9bIE6lhb6o2lsEgiud/giphy.gif' width=200px>")


if __name__ == "__main__":
    app.run(debug=True)
