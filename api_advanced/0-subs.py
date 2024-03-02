#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function that fetches number_of_subscribers"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        if RESPONSE.status_code == 200:
            return RESPONSE.json().get("data").get("subscribers")
        else:
            return 0

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return 0
    except Exception as e:
        print("Unexpected error:", e)
        return 0

