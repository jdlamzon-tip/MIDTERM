from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)