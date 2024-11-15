"""empty message

Revision ID: 8fb71d82c1e7
Revises: 561bdf73025e
Create Date: 2023-09-22 13:06:21.213537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8fb71d82c1e7"
down_revision = "561bdf73025e"
branch_labels = None
depends_on = None


def upgrade(op):
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("ecs_challenge", "guide")
    op.add_column(
        "ecs_challenge",
        sa.Column("guide", sa.Text(), nullable=False, server_default=""),
    )
    # ### end Alembic commands ###


def downgrade(op):
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("ecs_challenge", "guide")
    op.add_column("ecs_challenge", sa.Column("guide", sa.Text(), nullable=True))
    # ### end Alembic commands ###
