#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    employee = requests.get('{}/users/{}'.format(url, employee_id)).json()
    tasks = requests.get('{}/todos'.format(url)).json()

    EMPLOYEE_NAME = employee.get('name')

    output_file = '{}.csv'.format(employee_id)

    with open(output_file, 'w') as csvfile:
        for task in tasks:
            if task.get('userId') == employee_id:
                csvfile.write('"{}","{}","{}","{}"\n'.format(
                            task.get('userId'),
                            EMPLOYEE_NAME,
                            task.get("completed"),
                            task.get("title"))
                        )
