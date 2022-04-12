#!/usr/bin/python3
""" Python script that, using the REST API
    https://jsonplaceholder.typicode.com/, for a given employee ID,
    returns and save to csv file.
"""

if __name__ == '__main__':
    import csv
    import requests
    import sys

    userId = sys.argv[1]

    response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(userId))

    UserName = response.json().get("username")
    FileName = userId + "." + "csv"

    response1 = requests.get("https://jsonplaceholder.typicode.com/todos")

    rows = []
    for todo in response1.json():
        if int(userId) == todo.get("userId"):
            NewList = []
            NewList.append('\"{}\"'.format(todo.get("userId")))
            NewList.append('\"{}\"'.format(UserName))
            NewList.append('\"{}\"'.format(todo.get("completed")))
            NewList.append('\"{}\"'.format(todo.get("title")))
            rows.append(NewList)

    with open(FileName, "w") as csvfile:
        csvwriter = csv.writer(csvfile, quotechar="'")
        csvwriter.writerows(rows)
