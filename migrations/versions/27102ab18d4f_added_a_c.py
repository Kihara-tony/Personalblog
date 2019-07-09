"""added a c

Revision ID: 27102ab18d4f
Revises: a94563c7369a
Create Date: 2019-07-08 23:02:26.537054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27102ab18d4f'
down_revision = 'a94563c7369a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('blog_title', sa.String(), nullable=True))
    op.add_column('comments', sa.Column('comment', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'comment')
    op.drop_column('blogs', 'blog_title')
    # ### end Alembic commands ###
