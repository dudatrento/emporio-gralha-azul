"""ativa RLS nas tabelas

Revision ID: d7f4ec0385d8
Revises: 89256fe7d3c7
Create Date: 2026-11-14 15:53:17.148479

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7f4ec0385d8'
down_revision: Union[str, Sequence[str], None] = '89256fe7d3c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


TABELAS = ["categories", "producers", "products", "alembic_version"]


def upgrade() -> None:
    for tabela in TABELAS:
        op.execute(f"ALTER TABLE {tabela} ENABLE ROW LEVEL SECURITY")


def downgrade() -> None:
    for tabela in TABELAS:
        op.execute(f"ALTER TABLE {tabela} DISABLE ROW LEVEL SECURITY")