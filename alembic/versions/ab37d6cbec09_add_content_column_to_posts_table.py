"""add content column to posts table

Revision ID: ab37d6cbec09
Revises: b837df3775b6
Create Date: 2023-03-23 10:22:32.865746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab37d6cbec09'
down_revision = 'b837df3775b6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
