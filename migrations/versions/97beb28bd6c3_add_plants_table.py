"""add_plants_table

Revision ID: 97beb28bd6c3
Revises: c1f1bcb0e48c
Create Date: 2020-10-09 16:26:34.336713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97beb28bd6c3'
down_revision = 'c1f1bcb0e48c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('plants',
    sa.Column('space_id', sa.Integer(), nullable=False),
    sa.Column('plant_id', sa.Integer(), nullable=False),
    sa.Column('move_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['plant_id'], ['plant.id'], name=op.f('fk_plants_plant_id_plant')),
    sa.ForeignKeyConstraint(['space_id'], ['space.id'], name=op.f('fk_plants_space_id_space')),
    sa.PrimaryKeyConstraint('space_id', 'plant_id', name=op.f('pk_plants'))
    )


def downgrade():
    op.drop_table('plants')
