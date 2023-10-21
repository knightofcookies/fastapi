"""add content column to posts table

Revision ID: 1ca4a758b1b1
Revises: cb4c72867370
Create Date: 2023-10-21 15:43:36.722678

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '1ca4a758b1b1'
down_revision: Union[str, None] = 'cb4c72867370'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
