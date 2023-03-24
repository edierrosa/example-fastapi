"""add user table

Revision ID: 078d55a2fd7b
Revises: ab37d6cbec09
Create Date: 2023-03-23 10:30:01.890453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '078d55a2fd7b'
down_revision = 'ab37d6cbec09'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
