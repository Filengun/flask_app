from flask import Flask, render_template

app = Flask(__name__)

menu = ["Главная", "О нас", "Лента"]


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


@app.route('/')
def index():
    return render_template('index.html', title='Главная страница!', menu=menu)


@app.route('/about/')
def about():
    return render_template('about.html', title='About Us!', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
