import sqlalchemy as sa 
import sqlalchemy.orm as so 
from app import db
from typing import Optional
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(32), unique=True, index=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True, index=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    workouts: so.WriteOnlyMapped['Workout'] = so.relationship(back_populates='user')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return "<User {}>".format(self.username) 


class Workout(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64), unique=False)
    created: so.Mapped[datetime] = so.mapped_column(default=datetime.now(timezone.utc))
    started: so.Mapped[Optional[datetime]] = so.mapped_column()
    finished: so.Mapped[Optional[datetime]] = so.mapped_column()
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    user: so.Mapped[User] = so.relationship(back_populates="workouts")

    def __repr__(self):
        return "<Workout {}>".format(self.id) 
    

class Exercise(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), unique=False)

    def __repr__(self):
        return "<Exercise {}>".format(self.id) 