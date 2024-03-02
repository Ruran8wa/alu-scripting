#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers
"""
import requests
import sys


def number_of_subscribers(subreddit):
    agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    reddit = response.json()
    if 'data' not in reddit:
        return 0
    if 'subscribers' not in reddit.get('data'):
        return 0
    return response.json()['data']['subscribers']
