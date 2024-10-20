"""Add Ticket model

Revision ID: dd490825c662
Revises: 9208d37f483f
Create Date: 2024-10-18 16:24:49.650164

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dd490825c662'
down_revision = '9208d37f483f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ticket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('purchase_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=100),
               type_=sa.String(length=200),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=sa.String(length=200),
               type_=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=100),
               existing_nullable=False)

    op.drop_table('ticket')
    # ### end Alembic commands ###