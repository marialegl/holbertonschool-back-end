#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


import requests
from sys import argv

if __name__ == "__main__":
    id = int(argv[1])

    employee = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    n_employee = (employee.json().get("name"))

    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = response.json()

    employee_task = []
    for todo in todos:
        if todo['userId'] == id:
            employee_task.append(todo)

    d_task = 0
    for todo in employee_task:
        if todo['completed']:
            d_task += 1

    total_tasks = len(employee_task)

    print(f"Employee {n_employee} is done with tasks({d_task}/{total_tasks}):")
    for todo in employee_task:
        if todo['completed']:
            print(f"\t{todo['title']}")
