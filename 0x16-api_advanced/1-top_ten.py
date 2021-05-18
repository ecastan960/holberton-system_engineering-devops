#!/usr/bin/python3
"""Python script that uses a reddit API
"""
import json
import requests


def top_ten(subreddit):
    """Function that returns titles of first 10
    hot post listed
    """
    url = "https://www.reddit.com/r/{}/hot.json"
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.com'
    }
    r_titles = requests.get(url.format(subreddit), headers=headers)
    if r_titles.status_code == 200:
        data = r_titles.json()['data']['children']
        for x in range(10):
            print(data[x]['data']['title'])
    else:
        print(None)
