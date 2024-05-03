#!/usr/bin/python3
"""
Script that, using this REST API,
records all tasks of all employees in JSON format
"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    """Crear un diccionario para almacenar los datos de todos los empleados"""
    all_employees_data = {}

    """Iterar sobre todos los usuarios"""
    for user in users:
        user_id = user['id']
        username = user['username']

        """Obtener las tareas de cada usuario"""
        todos = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
            ).json()

        """Crear una lista de tareas para el usuario actual"""
        user_tasks = []

        """Iterar sobre todas las tareas del usuario"""
        for todo in todos:
            task_data = {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            user_tasks.append(task_data)

        """Agregar las tareas del usuario al diccionario general"""
        all_employees_data[str(user_id)] = user_tasks

    """Escribir el diccionario en el archivo JSON"""
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_data, json_file)
