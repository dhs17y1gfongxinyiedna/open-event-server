"""empty message

Revision ID: 884774042071
Revises: 5b37561a6d2b
Create Date: 2016-06-27 05:27:22.710083

"""

# revision identifiers, used by Alembic.
revision = '884774042071'
down_revision = '5b37561a6d2b'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('received_at', sa.DateTime(), nullable=True),
    sa.Column('has_read', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notification')
    ### end Alembic commands ###
