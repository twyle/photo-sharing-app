"""adds the activate_account

Revision ID: a9992d316bd3
Revises: 234270c17f39
Create Date: 2023-03-08 16:28:54.935214

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a9992d316bd3"
down_revision = "234270c17f39"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(sa.Column("account_activated", sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_column("account_activated")

    # ### end Alembic commands ###
