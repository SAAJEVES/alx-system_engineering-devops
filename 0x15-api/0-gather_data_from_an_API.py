#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import sys
from urllib.request import urlopen


def get_name(url, user_id):
    """
    Returns the Name of User with the User_id
    """
    with urlopen(f"{url}/users/{user_id}") as req:
        resp = req.read()
        json_data = resp.decode('utf-8')
        data = json.loads(json_data)
        return (data['name'])


def get_todo_list(url, user_id):
    """
    Returns list of activities to do
    """
    with urlopen(f"{url}/users/{user_id}/todos") as req:
        resp = req.read()
        json_data = resp.decode('utf-8')
        data = json.loads(json_data)
        return (data)


def get_list_info(the_list):
    """
    Return some vital information about todolist
    """
    num_list = len(the_list)
    completed_list = 0
    list_title = []

    for val in the_list:
        if val['completed'] is True:
            completed_list += 1
            list_title.append(val['title'])
    return (completed_list, num_list, list_title)


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    name = get_name(url, user_id)
    total_list = get_todo_list(url, user_id)
    val1, val2, val3 = get_list_info(total_list)

    print(f"Employee {name} is done with tasks ({val1}/{val2}):")
    for _ in val3:
        print(f"\t {_}")
