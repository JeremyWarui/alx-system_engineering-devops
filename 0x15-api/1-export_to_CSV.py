#!/usr/bin/python3
"""script that returns employee info on tasks progress"""

import csv
import requests
from sys import argv


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
    for task in tasks:
        completed = task.get('completed')
        title = task.get('title')
        row_tasks.append([user_id,
                          user_name,
                          completed,
                          title])
    filename = "{}.csv".format(user_id)
    with open(filename, "w", encoding="UTF8") as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in row_tasks:
            writer.writerow(task)
