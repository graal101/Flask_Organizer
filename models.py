"""Model."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import DateTime


db = SQLAlchemy()

class Guests(db.Model):
    """Reg of unique customers."""

    ids = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip = db.Column(db.String(20), unique=False, nullable=True)
    user_agent = db.Column(db.Text, unique=False, nullable=True)
    ref = db.Column(db.String(200), unique=False, nullable=True)
    visittime = db.Column(db.DateTime, server_default=func.now())
    
    
class Users(db.Model):
    """Пользователи зарегистрированные."""
    
    ids = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=True)
