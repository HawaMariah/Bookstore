"""empty message

Revision ID: 2c1ba7ef7a83
Revises: 1e4a10de0430
Create Date: 2023-09-07 14:03:30.675432

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c1ba7ef7a83'
down_revision: Union[str, None] = '1e4a10de0430'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
