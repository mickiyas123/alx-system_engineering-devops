#!/usr/bin/python3
"""A module that queries the Reddit API"""


def top_ten(subreddit):
    """A function that returns top 10 hot post of a subreddit
       (not active users, total subscribers) for a given subreddit.
       If an invalid subreddit is given, the function returns 0
    """
    import requests

    limit = 10
    root_url = "https://www.reddit.com/r"

    base_url = "{}/{}/hot/.json?limit={}".format(root_url, subreddit, limit)
    response = requests.get(
            base_url,
            headers={'User-Agent': '0-subs:v0.0.0 (by /u/xyz_abc4890)'},
            allow_redirects=False)
    if response.status_code != 200:
        print("None")
    else:
        response = response.json()
        for post in response.get("data").get("children"):
            print(post.get("data").get("title"))
