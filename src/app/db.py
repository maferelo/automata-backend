"""Database module.""" ""
import databases
import ormar
import sqlalchemy

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    """Base metadata for all models."""

    metadata = metadata
    database = database


class User(ormar.Model):
    """User model."""

    class Meta(BaseMeta):
        """Meta class.""" ""

        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    active: bool = ormar.Boolean(default=True, nullable=False)


class Readers(ormar.Model):
    """Readers model."""

    class Meta(BaseMeta):
        """Meta class."""

        tablename = "readers"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=128, unique=False, nullable=False)
    lastname: str = ormar.String(max_length=128, unique=False, nullable=True)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)


class Books(ormar.Model):
    """Books model."""

    class Meta(BaseMeta):
        """Meta class."""

        tablename = "books"

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=128, unique=True, nullable=False)
    author: str = ormar.String(max_length=128, unique=False, nullable=False)


class BooksReaders(ormar.Model):
    """BooksReaders model."""

    class Meta(BaseMeta):
        """Meta class."""

        tablename = "books_readers"
        constraints = [ormar.UniqueColumns("book", "reader")]

    id: int = ormar.Integer(primary_key=True)
    book: Books = ormar.ForeignKey(Books, nullable=False, indexed=True)
    reader: Readers = ormar.ForeignKey(Readers, nullable=False, indexed=True)
