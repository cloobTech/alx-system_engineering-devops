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
    tasks = requests.get('{}/todos?userId={}'.format(url, employee_id)).json()

    print(sum(1 for x in tasks if x.get('completed')))
