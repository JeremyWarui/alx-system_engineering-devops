#!/usr/bin/python3
"""script that prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """returns a list of top ten titles"""
    headers = {"User-Agent": "Mozills/5.0"}
    params = {"limit": 10}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url=url, headers=headers, params=params,
                       allow_redirects=False)
    res_json = res.json()
    if res.status_code != 200:
        print(None)
        return
    posts = res_json.get("data").get("children")
    if len(posts) == 0:
        print(None)
    else:
        for post in posts:
            print(post.get("data").get("title"))
