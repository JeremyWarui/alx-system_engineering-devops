#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of all hot articles"""

    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": "after"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url=url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    res_json = response.json()
    posts = res_json.get("data").get("children")
    if not posts:
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get("title"))

    after = res_json.get("data").get("after")
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
