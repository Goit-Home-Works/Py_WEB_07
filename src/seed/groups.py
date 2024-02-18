import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from models.db import session
from models.models import Group
import logging

package_name="hw"
logger = logging.getLogger(f"{package_name}.{__name__}")

GROUPS = [
    "M88-1/8",
    "M88-2/8",
    "M89-1/8",
    "M89-2/8",
    "C88-1/8",
    "C88-2/8",
    "C89-1/8",
    "C89-2/8",
    "P88-1/8",
    "P88-2/8",
    "P89-1/8",
    "P89-2/8",
]

def erase_groups():
    deleted_groups = session.query(Group).delete()
    logger.info(f"{deleted_groups=}")


def create_groups():
    erase_groups()
    for group_name in GROUPS:
        group = Group(
            name=group_name,
        )
        session.add(group)
    session.commit()


if __name__ == "__main__":
    create_groups()
