#!/usr/bin/python3
#script that returns employee info on tasks progress
from sys import argv
from get import requests


if __name__ == "__main__":
	users_url = "https://jsonplaceholder.typicode.com/users"
	todos_url = "https://jsonplaceholder.typicode.com/todos"
	
	user = "{}/{}".format(users_url, argv[1])
	response = get(user)
	res_json = response.json()
	print("Employee {} is done with tasks".format(res_json.get('name')), end="")

	todos = "{}?userId={}".format(todos_url, argv[1])
	res = get(todos)
	tasks = res.json()
	done_tasks = []
	for task in tasks:
		if task.get('completed') is True:
			done_tasks.append(task)

	
