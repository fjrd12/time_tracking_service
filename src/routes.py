from flask import Blueprint, request, jsonify
from flask_restx import Resource, fields, Namespace
from src.create_app import db, api
from src.models import User, Task, Category, TimeTrackingRequest
from sqlalchemy.sql import func

api_bp = Blueprint('api', __name__)

user_ns = Namespace('users', description='User operations')
category_ns = Namespace('categories', description='Category operations')

task_model = api.model('Task', {
    'name': fields.String(required=True, description='Task name'),
    'category_id': fields.Integer(required=True, description='Category ID')
})

category_model = api.model('Category', {
    'name': fields.String(required=True, description='Category name')
})


@user_ns.route('/')
class UserList(Resource):
    def get(self):
        """
        The get function returns a list of all users in the database.
            The function queries the User table and returns the id and the username for each user.

        """
        users = User.query.all()
        result = [{'id': user.id, 'username': user.username} for user in users]
        return jsonify(result)


@category_ns.route('/')
class CategoryList(Resource):
    def get(self):
        """
        The get function returns a list of all categories in the database.
            The result is returned as JSON, and each category has an id and name.

        """
        categories = Category.query.all()
        result = [{'id': category.id, 'name': category.name} for category in categories]
        return jsonify(result)

    @api.expect(category_model)
    def post(self):
        """
        The post function creates a new category.
            It takes in the name of the category as a json object and checks if it exists in the database.
            If it does, then object it's returned with its id.
            Otherwise, a new category is created and added to the database.

        """
        data = request.json
        qry = Category.query.filter(Category.name == data['name']).first()
        if qry:
            return jsonify({'message': 'Category already exists', ' id: ': qry.id})
        new_category = Category(name=data['name'])
        db.session.add(new_category)
        db.session.commit()
        return jsonify({'message': 'Category created successfully', 'id': new_category.id})


# Rutas para tareas del usuario
@api.route('/user/<int:user_id>/tasks')
class UserTasks(Resource):
    @api.expect(task_model)
    def post(self, user_id):
        """
        The post function creates a new task or updates an existing one.
            If the task already exists, it will update the end_time of its last time tracking request to now.
            If not, it will create a new task and start tracking time for that.

        """
        data = request.json
        task_name = data['name']
        category_id = data['category_id']
        user = User.query.get_or_404(user_id)
        task = Task.query.filter_by(name=task_name, user_id=user_id, category_id=category_id).first()
        if task:
            time_tracking_request = TimeTrackingRequest.query.filter_by(task_id=task.id, end_time=None).first()
            if time_tracking_request:
                time_tracking_request.update_end_time()
            else:
                new_request = TimeTrackingRequest(task_id=task.id)
                db.session.add(new_request)
        else:
            task = Task(name=task_name, user_id=user_id, category_id=category_id)
            db.session.add(task)
            db.session.flush()
            new_request = TimeTrackingRequest(task_id=task.id)
            db.session.add(new_request)

        db.session.commit()
        return jsonify({'message': 'Task updated or created successfully'})


@user_ns.route('/<int:user_id>/records')
class UserRecords(Resource):
    def get(self, user_id):
        """
        The get function returns a list of all the time tracking requests for a given user.
        The result is returned in JSON format.

        """
        user = User.query.get_or_404(user_id)

        records = db.session.query(
            Task.name.label('task_name'),
            Category.name.label('category_name'),
            TimeTrackingRequest.start_time,
            TimeTrackingRequest.end_time,
            (func.strftime('%s', TimeTrackingRequest.end_time) - func.strftime('%s',
                                                                               TimeTrackingRequest.start_time)) / 60.0
        ) \
            .join(Task, TimeTrackingRequest.task_id == Task.id) \
            .join(Category, Task.category_id == Category.id) \
            .filter(Task.user_id == user_id) \
            .all()

        result = [{'task_name': record.task_name, 'category_name': record.category_name,
                   'start_time': record.start_time, 'end_time': record.end_time,
                   'spent_time_minutes': record[4]} for record in records]
        return jsonify(result)


# adding namespaces into the API
api.add_namespace(user_ns, path='/api/users')
api.add_namespace(category_ns, path='/api/categories')
api.add_namespace(api, path='/api')
