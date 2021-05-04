#!/usr/bin/python3
"""Python script that uses a REST API
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    output_list = []
    output = {}
    file = "{}.json".format(user_id)
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'
    tasks_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    response_user = requests.get(users_url.format(user_id))
    response_task1 = requests.get(tasks_url.format(user_id))
    username = response_user.json()['username']
    t_total = len(response_task1.json())
    for tasks in range(t_total):
        dic = {}
        status = response_task1.json()[tasks]['completed']
        task = response_task1.json()[tasks]['title']
        dic["task"] = task
        dic["completed"] = status
        dic["username"] = username
        output_list.append(dic)
    output[user_id] = output_list
    json_object = json.dumps(output)
    with open(file, "w") as outfile:
        outfile.write(json_object)
