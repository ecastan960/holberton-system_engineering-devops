#!/usr/bin/python3
import requests
import json
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'
    response = requests.get(users_url.format(user_id))
    name = response.json()['name']
    print("Employee {} is done with tasks({}/{}):".format(name, 8, 20))
