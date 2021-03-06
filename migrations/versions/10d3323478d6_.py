"""
Adding SimpleInventory and PlayBook tables

Revision ID: 10d3323478d6
Revises: 928100cd270
Create Date: 2015-04-24 18:59:06.121923
"""

# revision identifiers, used by Alembic.
revision = '10d3323478d6'
down_revision = '928100cd270'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('play_book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('filename', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('filename'),
    sa.UniqueConstraint('name')
    )
    op.create_table('simple_inventory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('filename', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('filename'),
    sa.UniqueConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('simple_inventory')
    op.drop_table('play_book')
    ### end Alembic commands ###
