"""Add YTFormat table

Revision ID: a19c60f3f2bb
Revises: 4ec20d78a345
Create Date: 2024-03-11 21:52:26.312768

"""

from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a19c60f3f2bb"
down_revision: Union[str, None] = "4ec20d78a345"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Добавляем таблицу video_formats
    op.create_table(
        'video_formats',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('format_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('ext', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('resolution', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('fps', sa.Float(), nullable=True),
        sa.Column('audio_channels', sa.Integer(), nullable=True),
        sa.Column('filesize', sa.BigInteger(), nullable=True),
        sa.Column('tbr', sa.Float(), nullable=True),
        sa.Column('protocol', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('vcodec', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('acodec', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('asr', sa.Integer(), nullable=True),
        sa.Column('format', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('format_note', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('width', sa.Integer(), nullable=True),
        sa.Column('height', sa.Integer(), nullable=True),
        sa.Column('dynamic_range', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('language', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column('quality', sa.Integer(), nullable=True, default=0),
        sa.Column('has_drm', sa.Boolean(), nullable=True, default=False),
        sa.Column('filesize_approx', sa.BigInteger(), nullable=True),
        sa.Column('file_path', sa.String(), nullable=True),
        sa.Column('is_downloaded', sa.Boolean(), nullable=False, default=False),
        sa.Column('video_id', sa.UUID(as_uuid=True), sa.ForeignKey("youtube.videos.id")),
        schema='youtube'
    )

    # Удаляем поля video_path и is_downloaded из таблицы videos
    op.drop_column("videos", "video_path", schema="youtube")
    op.drop_column("videos", "is_downloaded", schema="youtube")


def downgrade():
    # Удаляем таблицу video_formats
    op.drop_table("video_formats", schema="youtube")

    # Восстанавливаем поля video_path и is_downloaded в таблице videos
    op.add_column(
        "videos", sa.Column("video_path", sqlmodel.sql.sqltypes.AutoString(), nullable=True), schema="youtube"
    )
    op.add_column("videos", sa.Column("is_downloaded", sa.Boolean(), nullable=False, default=False), schema="youtube")
