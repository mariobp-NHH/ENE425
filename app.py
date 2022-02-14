from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Home page updated again</h1>"

@app.route('/developers')
def developers():
    return "<h1>Developers</h1>"

@app.route('/app_calculator')
def app_calculator():
    return "<h1>App Calculator</h1>"

if __name__ == '__main__':
    app.run(debug=True)
