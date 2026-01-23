"""dataseeding

Revision ID: 1051e1dc5d14
Revises: 9c00574219b6
Create Date: 2026-01-23 18:41:34.547221

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1051e1dc5d14'
down_revision: Union[str, Sequence[str], None] = '9c00574219b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
