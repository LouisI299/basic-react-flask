from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SavingsGoal(db.Model):
    id