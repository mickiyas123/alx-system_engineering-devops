#!/usr/bin/python3
""" Python script that, using the REST API
    https://jsonplaceholder.typicode.com/, for all employees,
    returns information and save it to json file.
"""

if __name__ == '__main__':
    import json
    import requests
    import sys

    response = requests.get(
            "https://jsonplaceholder.typicode.com/users")

    response1 = requests.get("https://jsonplaceholder.typicode.com/todos")

    users = response.json()
    todos = response1.json()
    filename = "todo_all_employees.json"

    AllTask = {}

    for user in users:
        TaskList = []
        for task in todos:
            if task.get("userId") == user.get('id'):
                TaskDict = {"username": user.get("username"),
                            "task": task.get("title"),
                            "completed": task.get("completed")}
                TaskList.append(TaskDict)
        AllTask[user.get("id")] = TaskList

    with open(filename, "w") as jsonfile:
        json.dump(AllTask, jsonfile)
