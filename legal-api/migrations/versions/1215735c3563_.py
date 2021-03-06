"""empty message

Revision ID: 1215735c3563
Revises: b826412a6a65
Create Date: 2019-06-24 12:13:06.662550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1215735c3563'
down_revision = '4ee6f0abb797'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses_version',
                    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('address_type', sa.String(length=4096), autoincrement=False, nullable=True),
                    sa.Column('street', sa.String(length=4096), autoincrement=False, nullable=True),
                    sa.Column('street_additional', sa.String(length=4096), autoincrement=False, nullable=True),
                    sa.Column('city', sa.String(length=4096), autoincrement=False, nullable=True),
                    sa.Column('region', sa.String(length=4096), autoincrement=False, nullable=True),
                    sa.Column('country', sa.String(length=2), autoincrement=False, nullable=True),
                    sa.Column('postal_code', sa.String(length=10), autoincrement=False, nullable=True),
                    sa.Column('delivery_instructions', sa.String(length=4096), autoincrement=False, nullable=True),
                    sa.Column('business_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'transaction_id')
                    )
    op.create_index(op.f('ix_addresses_version_address_type'), 'addresses_version', ['address_type'], unique=False)
    op.create_index(op.f('ix_addresses_version_business_id'), 'addresses_version', ['business_id'], unique=False)
    op.create_index(op.f('ix_addresses_version_end_transaction_id'), 'addresses_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_addresses_version_operation_type'), 'addresses_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_addresses_version_street'), 'addresses_version', ['street'], unique=False)
    op.create_index(op.f('ix_addresses_version_transaction_id'), 'addresses_version', ['transaction_id'], unique=False)
    op.create_table('addresses',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('address_type', sa.String(length=4096), nullable=True),
                    sa.Column('street', sa.String(length=4096), nullable=True),
                    sa.Column('street_additional', sa.String(length=4096), nullable=True),
                    sa.Column('city', sa.String(length=4096), nullable=True),
                    sa.Column('region', sa.String(length=4096), nullable=True),
                    sa.Column('country', sa.String(length=2), nullable=True),
                    sa.Column('postal_code', sa.String(length=10), nullable=True),
                    sa.Column('delivery_instructions', sa.String(length=4096), nullable=True),
                    sa.Column('business_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['business_id'], ['businesses.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_addresses_address_type'), 'addresses', ['address_type'], unique=False)
    op.create_index(op.f('ix_addresses_business_id'), 'addresses', ['business_id'], unique=False)
    op.create_index(op.f('ix_addresses_street'), 'addresses', ['street'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_addresses_street'), table_name='addresses')
    op.drop_index(op.f('ix_addresses_business_id'), table_name='addresses')
    op.drop_index(op.f('ix_addresses_address_type'), table_name='addresses')
    op.drop_table('addresses')
    op.drop_index(op.f('ix_addresses_version_transaction_id'), table_name='addresses_version')
    op.drop_index(op.f('ix_addresses_version_street'), table_name='addresses_version')
    op.drop_index(op.f('ix_addresses_version_operation_type'), table_name='addresses_version')
    op.drop_index(op.f('ix_addresses_version_end_transaction_id'), table_name='addresses_version')
    op.drop_index(op.f('ix_addresses_version_business_id'), table_name='addresses_version')
    op.drop_index(op.f('ix_addresses_version_address_type'), table_name='addresses_version')
    op.drop_table('addresses_version')
    # ### end Alembic commands ###
