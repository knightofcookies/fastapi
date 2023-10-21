"""add last few columns to posts table

Revision ID: cb4c72867370
Revises: 5a36b071e5c0
Create Date: 2023-10-21 15:32:00.536836

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'cb4c72867370'
down_revision: Union[str, None] = '5a36b071e5c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(table_name='posts',
                  column=sa.Column('published', sa.Boolean(), nullable=False,
                                   server_default='TRUE'), )
    op.add_column(table_name='posts',
                  column=sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                   nullable=False,
                                   server_default=sa.text('NOW()')), )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
