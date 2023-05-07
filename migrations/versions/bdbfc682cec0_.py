"""empty message

Revision ID: bdbfc682cec0
Revises: 8337b429ee9e
Create Date: 2023-05-05 19:16:24.750331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdbfc682cec0'
down_revision = '8337b429ee9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.Column('episode_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['episode_id'], ['episode.id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('episode', schema=None) as batch_op:
        batch_op.drop_constraint('episode_user_id_fkey', type_='foreignkey')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.drop_constraint('location_user_id_fkey', type_='foreignkey')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_constraint('people_user_id_fkey', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('people_user_id_fkey', 'user', ['user_id'], ['id'])

    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('location_user_id_fkey', 'user', ['user_id'], ['id'])

    with op.batch_alter_table('episode', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('episode_user_id_fkey', 'user', ['user_id'], ['id'])

    op.drop_table('favourites')
    # ### end Alembic commands ###