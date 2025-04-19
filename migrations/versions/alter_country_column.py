"""alter country column size

Revision ID: alter_country_column
Revises: 
Create Date: 2024-04-19 10:55:34.779

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'alter_country_column'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Alter the country column to increase its size
    op.alter_column('visit', 'country',
                    existing_type=sa.String(2),
                    type_=sa.String(100),
                    existing_nullable=True)

def downgrade():
    # Revert the country column back to its original size
    op.alter_column('visit', 'country',
                    existing_type=sa.String(100),
                    type_=sa.String(2),
                    existing_nullable=True) 