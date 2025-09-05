"""Model."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import DateTime


db = SQLAlchemy()

class Guests(db.Model):
    """Reg of unique customers."""
    
    __tablename__ = 'guests' 
    ids = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip = db.Column(db.String(20), unique=False, nullable=True)
    user_agent = db.Column(db.Text, unique=False, nullable=True)
    ref = db.Column(db.String(200), unique=False, nullable=True)
    visittime = db.Column(db.DateTime, server_default=func.now())
    
    
class Users(db.Model):
    """Пользователи зарегистрированные."""
    
    __tablename__ = 'users' 
    ids = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)


class Todolist(db.Model):
    """Таблица для записей списков дел."""
    
    __tablename__ = 'todolist'
    ids = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(50), unique=False, nullable=True)
    note = db.Column(db.Text, unique=False, nullable=True)
    is_done = db.Column(db.Boolean, default=False, nullable=False)
    
    
