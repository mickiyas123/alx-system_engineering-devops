#!/usr/bin/python3
""" Python script that, using the REST API
    https://jsonplaceholder.typicode.com/, for a given employee ID,
    returns information about his/her TODO list progress.
"""

if __name__ == '__main__':
    import requests
    import sys

    userId = sys.argv[1]

    response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(userId))

    EmployeeName = response.json().get("name")

    response1 = requests.get("https://jsonplaceholder.typicode.com/todos")

    allTasks = 0
    completeTasks = 0
    completeTasksList = []
    for todo in response1.json():
        if int(userId) == todo.get("userId"):
            allTasks += 1
            if todo.get("completed"):
                completeTasks += 1
                completeTasksList.append(todo.get("title"))

    print(
            "Employee {} is done with tasks({}/{}):"
            .format(EmployeeName, completeTasks, allTasks))

    for task in completeTasksList:
        print("\t {}".format(task))
