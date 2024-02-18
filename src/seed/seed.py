# import sys
# import os

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))

try:
    from seed.teachers import create_teachers
    from seed.subjects import create_subjects
    from seed.groups import create_groups
    from seed.students import create_students
    from seed.grades import create_grades
except ImportError:
    from teachers import create_teachers
    from subjects import create_subjects
    from groups import create_groups
    from students import create_students
    from grades import create_grades

import logging

package_name="hw"
logger = logging.getLogger(f"{package_name}.{__name__}")


def create_data():
    create_teachers()
    create_subjects()
    create_groups()
    create_students()
    create_grades()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    create_data()