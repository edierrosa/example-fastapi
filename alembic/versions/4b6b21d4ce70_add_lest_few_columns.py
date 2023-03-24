"""add lest few columns

Revision ID: 4b6b21d4ce70
Revises: 16a2d6089794
Create Date: 2023-03-24 10:05:00.749779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b6b21d4ce70'
down_revision = '16a2d6089794'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(),
                  nullable=False, server_default="TRUE"),)
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text("NOW()")),)
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
