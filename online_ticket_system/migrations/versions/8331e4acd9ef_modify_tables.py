"""modify tables

Revision ID: 8331e4acd9ef
Revises: 345006c9bf03
Create Date: 2024-10-07 14:52:56.252042

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8331e4acd9ef'
down_revision = '345006c9bf03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('concerts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('concert_name', sa.String(length=255), nullable=False),
    sa.Column('artist', sa.String(length=255), nullable=False),
    sa.Column('venue', sa.String(length=255), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('concert_date', sa.DateTime(), nullable=False),
    sa.Column('ticket_price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flights',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flight_number', sa.String(length=50), nullable=False),
    sa.Column('departure_city', sa.String(length=100), nullable=False),
    sa.Column('destination_city', sa.String(length=100), nullable=False),
    sa.Column('departure_time', sa.DateTime(), nullable=False),
    sa.Column('arrival_time', sa.DateTime(), nullable=False),
    sa.Column('airline', sa.String(length=100), nullable=False),
    sa.Column('ticket_price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_title', sa.String(length=255), nullable=False),
    sa.Column('cinema_name', sa.String(length=255), nullable=False),
    sa.Column('hall', sa.String(length=100), nullable=False),
    sa.Column('show_time', sa.DateTime(), nullable=False),
    sa.Column('ticket_price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('concert_tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('concert_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('seat_number', sa.String(length=10), nullable=True),
    sa.Column('ticket_price', sa.Float(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('purchase_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['concert_id'], ['concerts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flight_tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flight_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('seat_number', sa.String(length=10), nullable=True),
    sa.Column('ticket_price', sa.Float(), nullable=False),
    sa.Column('cabin_class', sa.String(length=50), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('purchase_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['flight_id'], ['flights.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie_tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('seat_number', sa.String(length=10), nullable=True),
    sa.Column('ticket_price', sa.Float(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('purchase_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('orders')
    op.drop_table('tickets')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tickets',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('departure', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('destination', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('departure_time', mysql.DATETIME(), nullable=False),
    sa.Column('price', mysql.FLOAT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('orders',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('ticket_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('status', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('created_on', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['ticket_id'], ['tickets.id'], name='orders_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='orders_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('movie_tickets')
    op.drop_table('flight_tickets')
    op.drop_table('concert_tickets')
    op.drop_table('movies')
    op.drop_table('flights')
    op.drop_table('concerts')
    # ### end Alembic commands ###