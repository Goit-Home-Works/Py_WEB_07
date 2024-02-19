import argparse
from crud_db import create, read, update, delete
from pprint import pprint

parser = argparse.ArgumentParser(
    description="Perform CRUD operations on database models."
)

# Define command-line arguments
parser.add_argument(
    "-a", "--action", help="Action to perform: 'create', 'list', 'update', or 'remove'."
)
parser.add_argument(
    "-m",
    "--model",
    help="Model name: 'Group', 'Student', 'Professor', 'Subject', 'Grade'.",
)
parser.add_argument(
    "-n", "--name", help="Name to be used for 'create' or 'update' actions."
)
parser.add_argument(
    "-id", "--id", help="ID to be used for 'update' or 'remove' actions."
)

args = parser.parse_args()

action = args.action
model = args.model
name = args.name
id = args.id


def action_func():
    if action == "create":
        return create(model, name)
    elif action == "list":
        return read(model)
    elif action == "update":
        return update(model, id, name)
    elif action == "remove":
        return delete(model, id)
    else:
        return f"Invalid action: {action}. Use 'create', 'list', 'update', or 'remove'."


if __name__ == "__main__":
    try:
        result = action_func()
        pprint(result)
    except Exception as e:
        print(f"Error: {e}")

# python3 src/cli_app.py --action create -m Professor --name 'Boris Jonson' створення вчителя
# python3 src/cli_app.py --action list -m Professor показати всіх вчителів
# python3 src/cli_app.py --action list --model Professor показати всіх вчителів
# python3 src/cli_app.py --action update -m Professor --id 8 --name 'Andry Bezos' оновити дані вчителя з id=3
# python3 src/cli_app.py --action remove -m Professor --id 8 видалити вчителя з id=3
