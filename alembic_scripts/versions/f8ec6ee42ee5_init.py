"""init

Revision ID: f8ec6ee42ee5
Revises: 
Create Date: 2020-02-19 18:36:07.149951

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy.sql.functions import current_timestamp

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
        sa.Column('profile_id', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('created_datetime', sa.TIMESTAMP, server_default=current_timestamp()),
        sa.Column('updated_datetime', sa.TIMESTAMP,
                  server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    )

    op.create_table(
        "profile",
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('username', sa.String(64), nullable=False, server_default=''),
        sa.Column('created_datetime', sa.DateTime, server_default=current_timestamp()),
        sa.Column('updated_datetime', sa.DateTime,
                  server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    )


def downgrade():
    op.drop_table("account")
    op.drop_table("profile")
