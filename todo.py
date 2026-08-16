import argparse
import json
import os

DEFAULT_STORAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks(path=DEFAULT_STORAGE_PATH):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


def save_tasks(tasks, path=DEFAULT_STORAGE_PATH):
    with open(path, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, text):
    next_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": next_id, "text": text, "done": False}
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    raise ValueError(f"No task with id {task_id}")


def remove_task(tasks, task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            return tasks.pop(i)
    raise ValueError(f"No task with id {task_id}")


def format_task(task):
    mark = "x" if task["done"] else " "
    return f"[{mark}] {task['id']}: {task['text']}"


def build_parser():
    parser = argparse.ArgumentParser(description="A simple CLI todo app")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("text", help="Task description")

    subparsers.add_parser("list", help="List all tasks")

    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="Task id")

    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("id", type=int, help="Task id")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    tasks = load_tasks()

    try:
        if args.command == "add":
            task = add_task(tasks, args.text)
            save_tasks(tasks)
            print(f"Added: {format_task(task)}")
        elif args.command == "list":
            if not tasks:
                print("No tasks yet.")
            for task in tasks:
                print(format_task(task))
        elif args.command == "done":
            task = complete_task(tasks, args.id)
            save_tasks(tasks)
            print(f"Completed: {format_task(task)}")
        elif args.command == "remove":
            task = remove_task(tasks, args.id)
            save_tasks(tasks)
            print(f"Removed: {format_task(task)}")
    except ValueError as e:
        print(f"Error: {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
