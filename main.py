from flask import Flask
app = Flask('__name__')

@app.route('/')
def index():
  return '<h1>Olá Mundo!</h1>'

@app.route('/unifran')
def unifran():
  return '<h2>Universidade de Franca</h2>'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)