#!/usr/bin/python3
""" script that returns employee info on tasks progress """

import json
from sys import argv
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user = "{}/{}".format(users_url, argv[1])
    response = requests.get(user)
    res_json = response.json()
    user_id = argv[1]
    user_name = res_json.get('username')

    todos = "{}?userId={}".format(todos_url, argv[1])
    res = requests.get(todos)
    tasks = res.json()
    row_tasks = []

    user_dict = {}
    for task in tasks:
        completed = task.get('completed')
        title = task.get('title')
        row_tasks.append({"task": title,
                          "completed": completed,
                          "username": user_name
                          })
    user_dict = {str(user_id): row_tasks}

    filename = "{}.json".format(user_id)
    with open(filename, "w", encoding="UTF8") as f:
        json_str = json.dumps(user_dict)
        f.write(json_str)
        f.close()
