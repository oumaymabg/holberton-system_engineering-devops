#!/usr/bin/python3
"""  Export to JSON  """

import requests
from sys import argv
from json import dump

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    USER_ID = argv[1]
    """ Extract Employee name """
    user = requests.get('{}/users/{}'.format(url, USER_ID)).json()
    USERNAME = user.get('username')
    """ Extract Employee Tasks """
    todos = requests.get('{}/todos?userId={}'.format(url, USER_ID)).json()
    data = []
    json_dict = {"{}".format(USER_ID): data}
    for Task in todos:
        TASK_COMPLETED_STATUS = Task.get("completed")
        TASK_TITLE = Task.get("title")
        data.append({"task": TASK_TITLE,
                     "completed": TASK_COMPLETED_STATUS,
                     "username": USERNAME})
    filename = "%s.json" % USER_ID
    with open(filename, 'w') as f:
        dump(json_dict, f)