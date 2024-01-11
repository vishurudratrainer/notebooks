from flask import Flask, render_template, request,make_response
app = Flask(__name__)

@app.route('/index')
def index():
   return render_template('cookie.html')


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   resp = make_response(render_template('readcookie.html'))
   if request.method == 'POST':
      user = request.form['nm']
      resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

if __name__ == '__main__':
   app.run(debug = True)
