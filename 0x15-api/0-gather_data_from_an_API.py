#!/usr/bin/python3
"""Python script that uses a REST API
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    t_done = 0
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'
    tasks_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    response_user = requests.get(users_url.format(user_id))
    response_task1 = requests.get(tasks_url.format(user_id))
    response_task2 = requests.get(tasks_url.format(user_id))
    name = response_user.json()['name']
    t_total = len(response_task1.json())
    for tasks in range(t_total):
        if response_task1.json()[tasks]['completed'] is True:
            t_done += 1
    text = "Employee {} is done with tasks({}/{}):"
    print(text.format(name, t_done, t_total))
    for tasks in range(t_total):
        if response_task1.json()[tasks]['completed'] is True:
            task = response_task1.json()[tasks]['title']
            print("\t {}".format(task))
