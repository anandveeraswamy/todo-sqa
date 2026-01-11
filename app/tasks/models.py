import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from datetime import datetime


class Todo(db.Model):
    __tablename__ = "todos"
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(), index=True)
    description: so.Mapped[str] = so.mapped_column(sa.String())
    created_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime, default=datetime.now
    )
    user_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey("users.id"), index=True, nullable=False
    )
    user: so.Mapped["User"] = so.relationship(back_populates="todos")
    completed: so.Mapped[bool] = so.mapped_column(sa.Boolean, default=False)

    def __repr__(self):
        return f"<Todo id={self.id} title={self.title}>"
