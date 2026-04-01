from flask import Flask, render_template

app = Flask(__name__)


@app.route('/templates')
def index():
  return render_template('user.html')

@app.route('/templates/<name>')
def user(name):
  return render_template('user.html', name = name)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('/templates'), 500

if __name__ == '__main__':
  app.run(debug=True)
