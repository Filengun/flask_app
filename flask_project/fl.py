from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdgegsdf8a7er03rhosfhaowfyq93r3oiofh"


menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Обратная связь", "url": "feedback"},
]


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template(
            "page404.html", title="Страница не найдена", menu=menu
        ),
        404,
    )


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Главная страница!', menu=menu)


@app.route('/about/')
def about():
    # print(url_for('about', username='filengun'))
    return render_template(
        'about.html',
        title='About Us!',
        menu=menu,
        # username=username
    )


@app.route('/feedback/', methods=["POST", "GET"])
def feedback():
    # пока нет бд так что не юзабельно и чисто для наглядности
    if request.method == "POST":
        print(request.form)
        if len(request.form["message"]) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Сообщение не отправлено', category='error')

    return render_template('feedback.html', title='Обратная связь', menu=menu)


@app.route("/login/", methods=["POST", "GET"])
def login():
    if "userLogin" in session:
        return redirect(url_for("index"))
    elif (
        request.method == "POST"
        and request.form["username"] == "filengun"
        and request.form["psw"] == "1234"
    ):

        session['userLogged'] = request.form['username']
        return redirect(url_for("index"))
    if request.form["username"] != "filengun":
        flash('Неправильный логин', category='error')
    elif request.form["psw"] != "1234":
        flash('Неправильный пароль', category='error')
    return render_template("login.html", title="Авторизация", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
