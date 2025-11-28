from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login


@login.user_loader
def load_user(id):
    """ 
    Flask-Login callback function.
    converts user id into a User object
        
    """
    return db.session.get(User, int(id))


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)    
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    todos: so.Mapped[list['Todo']] = so.relationship(back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User id={self.id} username='{self.username}'>"
    
class Todo(db.Model):
    __tablename__ = "todos"
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(), index=True)
    description: so.Mapped[str] = so.mapped_column(sa.String())    
    created_at: so.Mapped[datetime] = so.mapped_column(sa.DateTime, default=datetime.now)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('users.id'), index=True, nullable=False)
    user: so.Mapped[User] = so.relationship(back_populates='todos')
    completed: so.Mapped[bool] = so.mapped_column(sa.Boolean, default=False)

    def __repr__(self):
        return f'<Todo id={self.id} title={self.title}>'
    