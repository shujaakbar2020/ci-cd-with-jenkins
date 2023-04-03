from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
import os

host = os.environ.get('host')
username = os.environ.get('username')
password = os.environ.get('password')
print(host, username, password)

data = [
    {
        "dept_no": "d009",
        "dept_name": "Customer Service"
    },
    {
        "dept_no": "d005",
        "dept_name": "Development"
    },
    {
        "dept_no": "d002",
        "dept_name": "Finance"
    },
    {
        "dept_no": "d003",
        "dept_name": "Human Resources"
    },
    {
        "dept_no": "d001",
        "dept_name": "Marketing"
    },
    {
        "dept_no": "d004",
        "dept_name": "Production"
    },
    {
        "dept_no": "d006",
        "dept_name": "Quality Management"
    },
    {
        "dept_no": "d008",
        "dept_name": "Research"
    },
    {
        "dept_no": "d007",
        "dept_name": "Sales"
    }
]

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{password}@{host}:3306/company"
# db = SQLAlchemy(app)
# ma = Marshmallow(app)
api = Api(app)


# class Post(db.Model):
#     __tablename__ = "departments"
#     dept_no = db.Column(db.Integer, primary_key=True)
#     dept_name = db.Column(db.String(50))

#     def __repr__(self):
#         return '<Post %s>' % self.dept_name


# class PostSchema(ma.Schema):
#     class Meta:
#         fields = ("dept_no", "dept_name")


# post_schema = PostSchema()
# posts_schema = PostSchema(many=True)

import json

class PostListResource(Resource):
    def get(self):
        # posts = Post.query.all()
        # return posts_schema.dump(posts)
        return data

api.add_resource(PostListResource, '/')


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
