from decimal import Decimal

from sqlalchemy import Boolean, CheckConstraint, ForeignKey, Numeric, Text, text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base



class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(Text, unique=True)
    slug: Mapped[str] = mapped_column(Text, unique=True)
    descricao: Mapped[str | None] = mapped_column(Text)


class Producer(Base):
    __tablename__ = "producers"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(Text)
    slug: Mapped[str] = mapped_column(Text, unique=True)
    perfil: Mapped[str | None] = mapped_column(Text)
    cidade: Mapped[str] = mapped_column(Text)
    regiao: Mapped[str] = mapped_column(Text)
    resumo: Mapped[str] = mapped_column(Text)
    historia: Mapped[str | None] = mapped_column(Text)
    foto_url: Mapped[str | None] = mapped_column(Text)
    destaque: Mapped[bool] = mapped_column(Boolean, server_default=text("false"))

class Product(Base):
    __tablename__ = "products"
    __table_args__ = (
        CheckConstraint("estoque >= 0", name="ck_products_estoque_nao_negativo"),
        CheckConstraint(
            "conservacao IN ('ambiente', 'resfriado', 'congelado')",
            name="ck_products_conservacao_valida",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(Text)
    slug: Mapped[str] = mapped_column(Text, unique=True)
    descricao: Mapped[str] = mapped_column(Text)
    preco: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    apresentacao: Mapped[str] = mapped_column(Text)
    foto_url: Mapped[str | None] = mapped_column(Text)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    producer_id: Mapped[int | None] = mapped_column(ForeignKey("producers.id"))

    subgrupo: Mapped[str | None] = mapped_column(Text)
    conservacao: Mapped[str] = mapped_column(Text)
    sob_encomenda: Mapped[bool] = mapped_column(Boolean, server_default=text("false"))
    prazo_encomenda_horas: Mapped[int | None] = mapped_column()
    venda_adultos: Mapped[bool] = mapped_column(Boolean, server_default=text("false"))

    estoque: Mapped[int] = mapped_column()
    destaque: Mapped[bool] = mapped_column(Boolean, server_default=text("false"))
    ativo: Mapped[bool] = mapped_column(Boolean, server_default=text("true"))

