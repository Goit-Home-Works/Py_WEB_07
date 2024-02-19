"""Create users models

Revision ID: d0145f78abd1
Revises: 594e7abe3ea6
Create Date: 2024-02-19 15:48:37.348638

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0145f78abd1'
down_revision: Union[str, None] = '594e7abe3ea6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
