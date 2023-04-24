#!/usr/bin/python3
"""script that returns employee info on tasks progress"""
import requests
from sys import argv


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user = "{}/{}".format(users_url, argv[1])
    response = requests.get(user)
    res_json = response.json()
    print("Employee {} is done with tasks".format(
        res_json.get('name')), end="")

    todos = "{}?userId={}".format(todos_url, argv[1])
    res = requests.get(todos)
    tasks = res.json()
    done_tasks = []
    for task in tasks:
        if task.get('completed') is True:
            done_tasks.append(task)
    no_of_tasks = len(tasks)
    no_of_done_tasks = len(done_tasks)

    print("({}/{}:)".format(no_of_done_tasks, no_of_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
