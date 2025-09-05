#!/usr/bin/env python3
from flask import Flask, render_template, request, url_for

from models import Users, Guests, db

app = Flask(__name__)
app.config['SECRET_KEY'] = '1111uouohohouo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

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


if __name__ == '__main__':
    app.run(debug=True)
