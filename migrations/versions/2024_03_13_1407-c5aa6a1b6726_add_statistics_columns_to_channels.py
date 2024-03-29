"""add statistics columns to Channels

Revision ID: c5aa6a1b6726
Revises: a19c60f3f2bb
Create Date: 2024-03-13 14:07:25.776574

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5aa6a1b6726'
down_revision: Union[str, None] = 'a19c60f3f2bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('channels', sa.Column('viewCount', sa.Integer(), nullable=True), schema='youtube')
    op.add_column('channels', sa.Column('videoCount', sa.Integer(), nullable=True), schema='youtube')
    op.add_column('channels', sa.Column('published_at', sa.DateTime(), nullable=False), schema='youtube')
    op.add_column('channels', sa.Column('country', sa.String(length=255), nullable=True, server_default=""), schema='youtube')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('channels', 'viewCount', schema='youtube')
    op.drop_column('channels', 'videoCount', schema='youtube')
    op.drop_column('channels', 'published_at', schema='youtube')
    op.drop_column('channels', 'country', schema='youtube')
    # ### end Alembic commands ###
