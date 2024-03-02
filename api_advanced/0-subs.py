#!/usr/bin/python3
"""Return number of subscribers for a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except (requests.RequestException, KeyError):
        return 0

# Example usage:
subreddit_name = "learnpython"
subscribers = number_of_subscribers(subreddit_name)
if subscribers != 0:
    print(f"The subreddit r/{subreddit_name} has {subscribers} subscribers.")
else:
    print(f"The subreddit r/{subreddit_name} is invalid or does not exist.")

