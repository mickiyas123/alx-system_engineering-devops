#!/usr/bin/python3
""" Python script that, using the REST API
    https://jsonplaceholder.typicode.com/, for a given employee ID,
    returns information and save it to json file.
"""

if __name__ == '__main__':
    import json
    import requests
    import sys

    userId = sys.argv[1]

    response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(userId))

    EmployeeId = response.json().get("id")
    UserName = response.json().get("username")
    FileName = userId + "." + "json"

    response1 = requests.get("https://jsonplaceholder.typicode.com/todos")

    FinalDict = {}
    AllList = []
    for todo in response1.json():
        if int(userId) == todo.get("userId"):
            SingleDict = {}
            SingleDict.update({"task": todo.get("title")})
            SingleDict.update({"completed": todo.get("completed")})
            SingleDict.update({"username": UserName})
            AllList.append(SingleDict)
    FinalDict.update({EmployeeId: AllList})

    with open(FileName, "w") as jsonfile:
        json.dump(FinalDict, jsonfile)
