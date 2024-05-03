#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about the progress of your TODO list
in JSON format
"""


import requests
import json
from sys import argv


if __name__ == "__main__":
    id = int(argv[1])

    employee = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json()
    user_name = employee.get("username")

    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos').json()

    """Creamos una lista de diccionarios con la estructura correcta"""
    todo_list = [
        {"task": todo["title"],
         "completed": todo["completed"],
         "username": user_name} for todo in todos]

    """Creamos un diccionario que contiene la lista de tareas"""
    data = {str(id): todo_list}

    """Escribimos el diccionario en el archivo JSON"""
    with open("{}.json".format(id), "w") as json_file:
        json.dump(data, json_file)
