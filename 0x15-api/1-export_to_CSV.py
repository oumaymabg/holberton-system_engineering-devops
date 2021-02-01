#!/usr/bin/python3
"""  Export to CSV  """
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    USER_ID = argv[1]
    """ Extract Employee name """
    user = requests.get('{}/users/{}'.format(url, USER_ID)).json()
    USERNAME = user.get('username')
    """ Extract Employee Tasks """
    todos = requests.get('{}/todos?userId={}'.format(url, USER_ID)).json()
    rows = []
    for Task in todos:
        TASK_COMPLETED_STATUS = Task.get("completed")
        TASK_TITLE = Task.get("title")
        rows.append([USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])
    filename = "%s.csv" % USER_ID
    """ export to csv file """
    with open(filename, 'wt') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [csv_writer.writerow(row) for row in rows]