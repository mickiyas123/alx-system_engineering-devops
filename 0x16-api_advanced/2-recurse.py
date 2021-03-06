#!/usr/bin/python3
"""A module that queries the Reddit API"""


def recurse(subreddit, hot_list=[]):
    """A function that returns top 10 hot post of a subreddit
       (not active users, total subscribers) for a given subreddit.
       If an invalid subreddit is given, the function returns 0
    """
    import requests

    count = 0
    root_url = "https://www.reddit.com/r"
    if len(hot_list) == 0 and count == 0:
        base_url = "{}/{}/hot/.json?limit=100".format(root_url, subreddit)
    else:
        base_url = "{}/{}/hot/.json?limit=100&after={}".format(
                root_url, subreddit, hot_list[-1])
    response = requests.get(
            base_url,
            headers={'User-Agent': '0-subs:v0.0.0 (by /u/xyz_abc4890)'},
            allow_redirects=False)
    if response.status_code != 200:
        return "{}".format("OK")
    else:
        lst = []
        title_list = []
        response = response.json()
        for item in response.get('data').get('children'):
            lst.append(item['kind'] + '_' + item['data']['id'])
        for post in response.get("data").get("children"):
            title_list.append(post.get("data").get("title"))
        return title_list
    count = count + 1

    recurse(subreeddit, lst)
