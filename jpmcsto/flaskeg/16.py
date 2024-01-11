from flask import Flask, redirect, url_for,render_template
app = Flask(__name__)

@app.route("/")
def displayHtml():
    return render_template("hello.html")
app.run()
