#!/usr/bin/python3
import requests
from sys import argv
"""
Write a Python script that, using this REST API.
"""


if __name__ == "__main__":
    """
    display on the standard output the employee TODO list
    """
    ID = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID)).json()
    tables = []
    for table in todo:
        if table.get('completed') is True:
            tables.append(table.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(tables), len(todo)))
    for table in tables:
        print("\t {}".format(table))
