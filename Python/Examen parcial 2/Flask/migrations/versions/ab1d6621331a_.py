"""empty message

Revision ID: ab1d6621331a
Revises: 
Create Date: 2023-04-21 07:22:44.361996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab1d6621331a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gabinete',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Marca', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mouse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Marca', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pantalla',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Marca', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('silla',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Marca', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teclado',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Marca', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teclado')
    op.drop_table('silla')
    op.drop_table('pantalla')
    op.drop_table('mouse')
    op.drop_table('gabinete')
    # ### end Alembic commands ###
