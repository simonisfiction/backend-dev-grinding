from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db= SQLAlchemy(app)


tasks = []
mult_answer = 0



@app.route('/templates')
def user():
  print("entering the user view function")
  return render_template('user.html', tasks = tasks)



@app.route('/add', methods=['POST'])
def add():
  task = request.form['task']
  tasks.append(task)
  return redirect(url_for('index'))



@app.route('/multiply', methods=['POST'])
def multiply():
  global mult_answer
  num1 = int(request.form['input1'])
  num2 = int(request.form['input2'])
  print(f"{num1} {num2}")
  mult_answer = num1 * num2
  return redirect(url_for('index'))

@app.route('/')
def index():
  print("entering the index view function")
  return render_template('user.html', tasks = tasks, mult_answer = mult_answer)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'), 500

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True)

