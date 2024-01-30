#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the JSON format.
"""
import json
import sys
from urllib.request import urlopen


def get_username(url, user_id):
    """
    Returns the Name of User with the User_id
    """
    with urlopen(f"{url}/users/{user_id}") as req:
        resp = req.read()
        json_data = resp.decode('utf-8')
        data = json.loads(json_data)
        return (data['username'])


def get_todo_list(url, user_id):
    """
    Returns list of activities to do
    """
    with urlopen(f"{url}/users/{user_id}/todos") as req:
        resp = req.read()
        json_data = resp.decode('utf-8')
        data = json.loads(json_data)
        return (data)


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    name = get_username(url, user_id)
    total_list = get_todo_list(url, user_id)
    new_list = []
    file_name = f"{user_id}.json"

    for task in total_list:
        new_list.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": name
            })
    with open(file_name, 'w') as json_file:
        json.dump({user_id: new_list}, json_file)
