"""creating posts

Revision ID: af4cc6a4a431
Revises: 
Create Date: 2025-10-01 10:10:44.292094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af4cc6a4a431'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts",sa.Column("id",sa.Integer,nullable=False,primary_key=True),
                    sa.Column("title",sa.String,nullable=False))
   

def downgrade() -> None:
    """Downgrade schema."""
    pass
