"""Initial migration

Revision ID: 3e2afd0f48a5
Revises: 
Create Date: 2025-01-17 10:20:58.289923

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e2afd0f48a5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('donations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('donor_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_donations_donor_name'), 'donations', ['donor_name'], unique=False)
    op.create_index(op.f('ix_donations_id'), 'donations', ['id'], unique=False)
    op.create_index(op.f('ix_donations_item_name'), 'donations', ['item_name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_donations_item_name'), table_name='donations')
    op.drop_index(op.f('ix_donations_id'), table_name='donations')
    op.drop_index(op.f('ix_donations_donor_name'), table_name='donations')
    op.drop_table('donations')
    # ### end Alembic commands ###
