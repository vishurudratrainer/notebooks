from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/student')
def student():
   return render_template('student.html')

@app.route('/result1',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result1.html",result = result)

app.run(debug = True)
