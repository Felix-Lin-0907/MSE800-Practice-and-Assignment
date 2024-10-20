"""Rename Ticket to EventBooking

Revision ID: b71a93c3e9dd
Revises: dd490825c662
Create Date: 2024-10-18 16:27:26.579462

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b71a93c3e9dd'
down_revision = 'dd490825c662'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('purchase_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('ticket')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ticket',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('event_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('quantity', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('purchase_date', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], name='ticket_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='ticket_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('event_booking')
    # ### end Alembic commands ###
