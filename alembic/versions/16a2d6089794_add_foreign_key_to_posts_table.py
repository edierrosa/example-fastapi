"""add foreign-key to posts table

Revision ID: 16a2d6089794
Revises: 078d55a2fd7b
Create Date: 2023-03-24 09:52:45.643583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16a2d6089794'
down_revision = '078d55a2fd7b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", local_cols=[
                          "owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
