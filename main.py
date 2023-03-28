from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
import os

host = os.environ.get('host')
username = os.environ.get('username')
password = os.environ.get('password')
print(host, username, password)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{password}@{host}:3306/company"
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


class Post(db.Model):
    __tablename__ = "departments"
    dept_no = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(50))

    def __repr__(self):
        return '<Post %s>' % self.dept_name


class PostSchema(ma.Schema):
    class Meta:
        fields = ("dept_no", "dept_name")


post_schema = PostSchema()
posts_schema = PostSchema(many=True)


class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return posts_schema.dump(posts)


api.add_resource(PostListResource, '/')


if __name__ == '__main__':
    app.run(debug=True)
