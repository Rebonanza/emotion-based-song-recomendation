from flask import Flask, redirect, url_for, render_template

app =  Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotion")
def emotion():
    return render_template("emotion.html")

@app.route("/songs")
def songs():
    return render_template("songs.html")

if __name__ == "__main__":
    app.run(debug=True)