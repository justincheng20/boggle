from boggle import Boggle
from flask import Flask, render_template, session, jsonify, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

boggle_game = Boggle()

words = []

@app.route("/")
def root():

    board = boggle_game.make_board()

    session["board"] = board
    print("session", session)

    return render_template("index.html", board=board)

@app.route("/guesses", methods=["POST"])
def guesses():
    word = request.json["word"]
    print(word)
    words.append(word)
    board = session["board"]
    print("words", words)
    testList = ["this", "is", "a", "test list"]

    return render_template("/index.html", board=board, words=testList)