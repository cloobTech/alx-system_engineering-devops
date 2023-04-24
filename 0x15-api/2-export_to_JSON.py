#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    employee = requests.get('{}/users/{}'.format(url, employee_id)).json()
    tasks = requests.get('{}/todos'.format(url)).json()

    EMPLOYEE_NAME = employee.get('username')
    task_data = []

    for task in tasks:
        if task.get('userId') == employee_id:
            task_data.append({
                    'task': task.get('title'),
                    'completed': task.get('completed'),
                    'username': EMPLOYEE_NAME,
                    })

    json_data = {str(employee_id): task_data}
    output_file = '{}.json'.format(employee_id)

    with open(output_file, 'w') as jsonfile:
        json.dump(json_data, jsonfile)
