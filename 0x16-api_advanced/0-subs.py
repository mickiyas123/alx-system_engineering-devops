#!/usr/bin/python3
"""A module that queries the Reddit API"""


def number_of_subscribers(subreddit):
    """A function that returns the number of subscribers
       (not active users, total subscribers) for a given subreddit.
       If an invalid subreddit is given, the function returns 0
    """
    import requests
    import json

    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(
            base_url,
            headers={'User-Agent': '0-subs:v0.0.0 (by /u/xyz_abc4890)'})
    if response.status_code != 200:
        return 0
    else:
        response = response.json()
        subscribers = response.get("data").get("subscribers")
        return subscribers
