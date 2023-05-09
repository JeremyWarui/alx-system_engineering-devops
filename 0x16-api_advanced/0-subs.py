#!/usr/bin/python3
"""function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns total number of subscribers of given subreddit"""
    header = {"User-Agent": "Mozilla/5.0"}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url=url, headers=header)
    res_json = response.json()
    if "data" not in res_json:
        return 0
    if "subscribers" not in res_json.get("data"):
        return 0
    else:
        data = res_json.get("data")
        no_of_subs = data.get("subscribers")
        return no_of_subs
