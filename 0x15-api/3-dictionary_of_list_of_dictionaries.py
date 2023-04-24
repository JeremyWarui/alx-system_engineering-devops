#!/usr/bin/python3
# script that returns employee info on tasks progress
from sys import argv
import requests
import json


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url)
    users_json = users.json()
    user_dict = {}

    for user in users_json:
        user_id = user.get('id')
        user_name = user.get('username')
        todos = "{}?userId={}".format(todos_url, user_id)
        res = requests.get(todos)
        tasks = res.json()
        row_tasks = []
        for task in tasks:
            completed = task.get('completed')
            title = task.get('title')
            row_tasks.append({"username": user_name,
                              "task": title,
                              "completed": completed
                              })
        user_dict[str(user_id)] = row_tasks

    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="UTF8") as f:
        json_str = json.dumps(user_dict)
        f.write(json_str)
        f.close()
