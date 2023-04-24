#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == '__main__':
    EMPLOYEE_NAME = ""
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    employee = requests.get('{}/users/{}'.format(url, employee_id)).json()
    tasks = requests.get('{}/todos'.format(url)).json()

    EMPLOYEE_NAME = employee.get('name')
    completed_tasks = []

    for task in tasks:
        if task.get('userId') == employee_id:
            if task.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                completed_tasks.append(task.get('title'))
            TOTAL_NUMBER_OF_TASKS += 1

    print('Employee {} is done with tasks({}/{}):'.format
          (EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    [print('\t {}'.format(com_task)) for com_task in completed_tasks]
