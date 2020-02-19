"""init

Revision ID: f8ec6ee42ee5
Revises: 
Create Date: 2020-02-19 18:36:07.149951

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f8ec6ee42ee5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "account",
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('name', sa.String(64), nullable=False, server_default=''),
        sa.Column('phone', sa.String(16), nullable=False, server_default=''),
        sa.Column('profile_id', sa.Integer(), nullable=False, server_default='0')
    )

    op.create_table(
        "profile",
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('username', sa.String(64), nullable=False, server_default=''),
    )


def downgrade():
    op.drop_table("account")
    op.drop_table("profile")
