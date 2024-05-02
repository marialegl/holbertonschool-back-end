#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


import requests
from sys import argv

if __name__ == "__main__":
    id = int(argv[1])

    employee = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json()
    user_name = (employee.get("username"))

    todos = requests.get(
        'https://jsonplaceholder.typicode.com/user/{}/todos'.format(id)).json()
    with open("{}.csv".format(id), "w") as csv_file:
        for todo in todos:
            csv_file.write('"{}","{}","{}","{}"\n'
                           .format(
                               id,
                               user_name,
                               todo["completed"],
                               todo["title"]))
