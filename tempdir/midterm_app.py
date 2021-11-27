from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/login', code=302)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)