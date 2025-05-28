import sqlalchemy as sa 
import sqlalchemy.orm as so 
from app import db
from typing import Optional
from datetime import datetime, timezone


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(32), unique=True, index=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True, index=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return "<User {}".format(self.username) 


class Workout(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), unique=False)
    created: so.Mapped[datetime] = so.mapped_column(default=datetime.now(timezone.utc))
    started: so.Mapped[Optional[datetime]] = so.mapped_column()
    finished: so.Mapped[Optional[datetime]] = so.mapped_column()
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    guy: so.Mapped[User] = so.relationship(back_populates="workouts")

    def __repr__(self):
        return "<Workout {}".format(self.id) 
    

class Exercise(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), unique=False)

    def __repr__(self):
        return "<Exercise {}".format(self.id) 