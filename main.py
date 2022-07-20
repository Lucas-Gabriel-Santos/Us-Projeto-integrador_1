from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quem_somos')
def somos():
  return render_template('Quem_somos.html')

@app.route('/missao')
def mi():
  return render_template("Missao.html")

@app.route('/login')
def login():
  return render_template('Login.html')
  
app.run(host='0.0.0.0', port=81)