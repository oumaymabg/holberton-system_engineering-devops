#!/usr/bin/python3
""" Gather data from an API  """
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    employee_id = argv[1]
    """ Extract Employee name """
    user = requests.get('{}/users/{}'.format(url, employee_id))
    employee_name = user.json().get('name')
    """ Extract Employee Tasks """
    todos = requests.get('{}/todos?userId={}'.format(url, employee_id))
    result = todos.json()
    """ Extract List of completed Tasks of Employee """
    Done = [Task for Task in result if Task.get('completed')]
    """ Result """
    print('Employee {} is done with tasks({}/{}):'.
          format(employee_name, len(Done), len(result)))
    for Task in Done:
        print('\t {}'.format(Task.get('title')))