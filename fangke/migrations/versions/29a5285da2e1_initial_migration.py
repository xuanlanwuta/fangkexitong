"""initial migration

Revision ID: 29a5285da2e1
Revises: 
Create Date: 2018-05-17 16:50:44.917527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29a5285da2e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fk_applicant',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=32), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('ap_company', sa.String(length=32), nullable=False),
    sa.Column('company', sa.String(length=32), nullable=False),
    sa.Column('invit_name', sa.String(length=32), nullable=False),
    sa.Column('reason', sa.String(length=100), nullable=False),
    sa.Column('visit_time', sa.Date(), nullable=False),
    sa.Column('leave_data', sa.Date(), nullable=True),
    sa.Column('user_id', sa.String(length=32), nullable=False),
    sa.Column('state', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fk_invit_open',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inperson_id', sa.String(length=32), nullable=False),
    sa.Column('inperson_name', sa.String(length=32), nullable=False),
    sa.Column('invite_id', sa.String(length=32), nullable=False),
    sa.Column('user_id', sa.String(length=32), nullable=False),
    sa.Column('user_name', sa.String(length=32), nullable=False),
    sa.Column('user_comp', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fk_invit_person',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('open_id', sa.String(length=32), nullable=False),
    sa.Column('full_name', sa.String(length=32), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('id_type', sa.String(length=32), nullable=False),
    sa.Column('id_num', sa.String(length=20), nullable=False),
    sa.Column('company', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id_num')
    )
    op.create_table('fk_invitation',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=32), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('visitor_count', sa.String(length=2), nullable=False),
    sa.Column('visit_time', sa.Date(), nullable=False),
    sa.Column('leave_data', sa.Date(), nullable=False),
    sa.Column('position', sa.String(length=32), nullable=False),
    sa.Column('reason', sa.String(length=100), nullable=False),
    sa.Column('image_url', sa.String(length=256), nullable=True),
    sa.Column('check_in', sa.String(length=32), nullable=True),
    sa.Column('user_id', sa.String(length=32), nullable=False),
    sa.Column('state', sa.String(length=32), nullable=False),
    sa.Column('flag', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fk_users',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('password', sa.String(length=32), nullable=False),
    sa.Column('full_name', sa.String(length=32), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('company', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('fk_visitor',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=32), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('id_type', sa.Enum('\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81', '\xe5\x86\x9b\xe5\xae\x98\xe8\xaf\x81'), nullable=True),
    sa.Column('id_num', sa.String(length=20), nullable=False),
    sa.Column('company', sa.String(length=32), nullable=False),
    sa.Column('inperson_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['inperson_id'], ['fk_invit_person.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id_num')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fk_visitor')
    op.drop_table('fk_users')
    op.drop_table('fk_invitation')
    op.drop_table('fk_invit_person')
    op.drop_table('fk_invit_open')
    op.drop_table('fk_applicant')
    # ### end Alembic commands ###
