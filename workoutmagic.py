
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.models import User, Workout, Exercise
from app import app, db

@app.shell_context_processor
def make_shell_context():
    return {"app": app, "db": db, "sa": sa, "so": so, \
        "User": User, "Workout": Workout, "Exercise": Exercise}
    