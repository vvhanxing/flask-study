#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by vellhe 2017/7/9
import requests
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask import request
app = Flask(__name__)
api = Api(app)
print("server1")
TODOS = {
    'todo1': {'task': 'start'},
    'todo2': {'task': 'process'},
    'todo3': {'task': 'finish'},
    'todo4': {'task': 'error'}
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('task')


# # 操作（put / get / delete）单一资源Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

    def post(self, todo_id):
        req_json = request.get_json()
        return req_json

# 操作（post / get）资源列表TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

class SendMasg(Resource):

    def post(self):
        req_json = request.get_json()
        print(req_json)   
        url = "http://127.0.0.1:7600/getMasg"
        res = requests.post(url=url, json=req_json)
        res.raise_for_status()
        return {"receved":""}         
class GetMasg(Resource):
    def post(self):
        req_json = request.get_json()
        print("--",req_json)

        
# 设置路由
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(SendMasg, '/sendMasg')
api.add_resource(GetMasg, '/getMasg')

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=7000)