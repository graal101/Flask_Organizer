#!/usr/bin/env python3
from flask import Flask, render_template, request

from models import Guests, db

app = Flask(__name__)
app.config['SECRET_KEY'] = '1111uouo111uo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning
db.init_app(app)

menus = ['Chapter 1', 'Chapter 2', 'Chapter 3']

@app.route('/')
@app.route('/index')
def index():
    with app.app_context():
        db.create_all()
        
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
