from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
from sqlalchemy import Boolean, DateTime, Column, Integer, String, ForeignKey

from database import Base

db = SQLAlchemy()

class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

class Role(Base, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))
