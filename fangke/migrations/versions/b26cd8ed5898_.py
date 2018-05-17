"""empty message

Revision ID: b26cd8ed5898
Revises: 
Create Date: 2018-05-17 14:17:19.996919

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b26cd8ed5898'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    op.drop_index('phone', table_name='fk_invit_person')
    op.alter_column(u'fk_invitation', 'full_name',
               existing_type=mysql.VARCHAR(length=32),
               nullable=True)
    op.drop_index('phone', table_name='fk_invitation')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('phone', 'fk_invitation', ['phone'], unique=True)
    op.alter_column(u'fk_invitation', 'full_name',
               existing_type=mysql.VARCHAR(length=32),
               nullable=False)
    op.create_index('phone', 'fk_invit_person', ['phone'], unique=True)
    op.drop_table('fk_visitor')
    # ### end Alembic commands ###