from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
    print('home')
    return "Hello World"
@app.route('/<name>')
def user(name):
    print('user')
    return f"Hello {name} !"

@app.route('/admin')
def admin():
    print('admin')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()