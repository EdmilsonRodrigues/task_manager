from datetime import datetime
from sys import argv
from json import dump, load
import os
from typing import Callable


FUNCTIONS = {
    "add",
    "update",
    "delete",
    "mark-in-progress",
    "mark-done",
    "mark-todo",
    "list",
}
JSON_PATH = os.path.join(os.getcwd(), "tasks.json")

if not os.path.exists(JSON_PATH):
    dump([], open(JSON_PATH, "w"))

tasks = load(open(JSON_PATH))


class WrongArguments(Exception):
    pass


class WrongFunctionArguments(Exception):
    pass


def argparser() -> tuple[str, list]:
    if len(argv) < 2:
        raise WrongArguments

    func = argv[1]

    if func not in FUNCTIONS:
        raise WrongArguments

    func = func.replace("-", "_")

    arguments = argv[2:]

    return func, arguments


def add(description: str) -> None:
    if len(tasks) >= 1:
        id = tasks[-1]["id"] + 1
    else:
        id = 1
    tasks.append(
        {
            "id": id,
            "status": "todo",
            "description": description,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        }
    )


def main():
    func, arguments = argparser()
    function = globals()[func]

    try:
        function(arguments)
    except Exception:
        raise WrongFunctionArguments(function)


if __name__ == "__main__":
    try:
        main()
    finally:
        dump(tasks, open(JSON_PATH, "w"))
