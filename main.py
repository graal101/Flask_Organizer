#!/usr/bin/env python3
from flask import Flask, render_template, request, url_for, flash, session, redirect
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from models import Users, Guests, Todolist, db

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):  # Вынести отдельно!
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


app = Flask(__name__)
app.config['SECRET_KEY'] = '1111uouohohouo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#login_manager = LoginManager(app)
csrf = CSRFProtect(app)

with app.app_context():
    db.create_all()
    print('create')
    
@app.route('/')
@app.route('/index')
def index():
    menus = {'Редактировать': url_for('index'), 'Анализ':'#', 'logout':'#'}
    ip = request.headers.get('X-Real-IP')
    user_agent = request.user_agent.string
    ref = request.headers.get('Referer')
    new_entry = Guests(ip=ip, user_agent=user_agent, ref=ref)
    db.session.add(new_entry)
    db.session.commit()
    return render_template('index.html', menus=menus, title='Главная (templates)',
                            content='<h1>Template index page</h1>',
                          )


@app.route('/logins', methods=['GET', 'POST'])
def logins():
    menus = {'Редактировать': url_for('index'), 'Анализ':'#', 'logout':'#'}
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'admin':
            session['username'] = form.username.data
            flash('Успешный вход!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Неверное имя пользователя или пароль', 'danger')
    return render_template('login.html', menus=menus, title='Вход на сайт',
                            content='<h1>Template index page</h1>', form=form)


if __name__ == '__main__':
    app.run(debug=True)
