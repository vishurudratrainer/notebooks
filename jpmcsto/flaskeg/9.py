from flask import Flask
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/render')
def index():
   return render_template('7.html')

if __name__ == '__main__':
   app.run(debug = True)
