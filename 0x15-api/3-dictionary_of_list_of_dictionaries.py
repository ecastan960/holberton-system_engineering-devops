#!/usr/bin/python3
"""Python script that uses a REST API
"""
import json
import requests


if __name__ == "__main__":
    output = {}
    file = "todo_all_employees.json"
    users_url = 'https://jsonplaceholder.typicode.com/users/'
    tasks_url = 'https://jsonplaceholder.typicode.com/todos/'
    response_user = requests.get(users_url)
    number_users = len(response_user.json())
    response_task1 = requests.get(tasks_url)
    t_total = len(response_task1.json())
    t_total = t_total / number_users
    tasks = 0
    limit = tasks + int(t_total)
    for users in range(number_users):
        output_list = []
        user = users + 1
        while tasks < limit:
            dic = {}
            username = response_user.json()[users]['username']
            status = response_task1.json()[tasks]['completed']
            task = response_task1.json()[tasks]['title']
            dic["username"] = username
            dic["task"] = task
            dic["completed"] = status
            output_list.append(dic)
            tasks += 1
        limit = tasks + int(t_total)
        output[user] = output_list
    json_object = json.dumps(output)
    with open(file, "w") as outfile:
        outfile.write(json_object)
