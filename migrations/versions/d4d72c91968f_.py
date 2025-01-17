"""empty message

Revision ID: d4d72c91968f
Revises: 
Create Date: 2021-08-10 11:58:57.464642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4d72c91968f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('songs',
    sa.Column('uri', sa.String(), nullable=False),
    sa.Column('danceability', sa.Float(), nullable=False),
    sa.Column('key', sa.Integer(), nullable=False),
    sa.Column('loudness', sa.Float(), nullable=False),
    sa.Column('mode', sa.Integer(), nullable=False),
    sa.Column('speechiness', sa.Float(), nullable=False),
    sa.Column('acousticness', sa.Float(), nullable=False),
    sa.Column('instrumentalness', sa.Float(), nullable=False),
    sa.Column('liveness', sa.Float(), nullable=False),
    sa.Column('valence', sa.Float(), nullable=False),
    sa.Column('tempo', sa.Float(), nullable=False),
    sa.Column('duration_ms', sa.Integer(), nullable=False),
    sa.Column('time_signature', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('uri')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('authorization_code', sa.String(), nullable=True),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username')
    )
    op.create_table('daily_records',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), autoincrement=False, nullable=False),
    sa.Column('mood', sa.String(), nullable=False),
    sa.Column('song_uri', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['song_uri'], ['songs.uri'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'date')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('daily_records')
    op.drop_table('users')
    op.drop_table('songs')
    # ### end Alembic commands ###
