"""
models a python module to concentrate the definition from all the models to be use into the ORM and microservice.
"""
from datetime import datetime
from create_app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='category', lazy=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    time_tracking_requests = db.relationship('TimeTrackingRequest', backref='task', lazy=True)


class TimeTrackingRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    end_time = db.Column(db.DateTime)
    spent_time = db.Column(db.Interval)

    def update_end_time(self):
        """
        The update_end_time function updates the end_time and spent_time attributes of a Task object.

        :param self: Represent the instance of the class
        :return: The time spent on the task
        :doc-author: Trelent
        """
        self.end_time = datetime.utcnow()
        self.spent_time = self.end_time - self.start_time
