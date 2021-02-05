#!/usr/bin/python3
'''function that queries the Reddit API'''
import pprint
import requests
import json

BASE_URL = 'http://reddit.com/r/{}/hot.json'


def top_ten(subreddit):
    '''function that queries the Reddit API'''
    headers = {'User-agent': 'Unix:0-subs:v1'}
    response = requests.get(BASE_URL.format(subreddit),
                            headers=headers)
    data = response.json().get('data', {}).get('children', {})
    if response.status_code != 200 or not data:
        return print("None")
    for post in data[0:10]:
        print(post.get('data', {}).get('title'))
