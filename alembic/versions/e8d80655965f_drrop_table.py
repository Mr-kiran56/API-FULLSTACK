"""drrop_table

Revision ID: e8d80655965f
Revises: af4cc6a4a431
Create Date: 2025-10-01 10:29:55.887623

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8d80655965f'
down_revision: Union[str, Sequence[str], None] = 'af4cc6a4a431'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_table("posts")
