#!/usr/bin/python3
"""Python script that uses a REST API
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    file = "{}.csv".format(user_id)
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'
    tasks_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    response_user = requests.get(users_url.format(user_id))
    response_task1 = requests.get(tasks_url.format(user_id))
    username = response_user.json()['username']
    t_total = len(response_task1.json())
    with open(file, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"')
        for tasks in range(t_total):
            status = response_task1.json()[tasks]['completed']
            task = response_task1.json()[tasks]['title']
            csv_writer.writerow([user_id, username, status, task])
