#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,\
returns information about his/her todo list progress."""

import json
import requests
import sys


if __name__ == '__main__':

    filename = "todo_all_employees.json"
    req = requests.get('https://jsonplaceholder.typicode.com/todos')
    req_id = requests.get('https://jsonplaceholder.typicode.com/users/')
    with open(filename, "w") as f:
        d = {j.get("id"): [{'task': i.get('title'),
             'completed': i.get('completed'),
                            'username': j.get('username')} for i in req.json()
                           if j.get("id") == i.get('userId')]
             for j in req_id.json()}
        json.dump(d, f)