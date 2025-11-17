"""
Database models for the application.

This module defines the SQLAlchemy models for the app.
Currently, we have a single model:

- Register: Represents a collection or register in the system.

Notes for Students:
- Each class represents a table in the database.
- Each attribute of the class represents a column in the table.
- SQLAlchemy's ORM maps Python classes to database tables so we can
  work with Python objects instead of raw SQL.
"""

import uuid
from typing import TYPE_CHECKING

# PostgreSQL UUID type for database columns
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app import db

# TYPE_CHECKING is used to avoid circular import problems when
# using type hints in Python. It allows hints to be checked only
# during static analysis, not at runtime.
if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model
else:
    # Use db.Model as the base class for our models
    Model = db.Model


class Register(Model):
    """
    Represents a Register record in the database.

    Attributes
    ----------
    id : uuid.UUID
        Primary key for the Register. Automatically generated using uuid4.
    name : str
        A human-readable name for the register.
        Must be unique and cannot be null. Indexed for faster lookups.

    Notes for Students
    -----------------
    - `mapped_column` defines a column in the database table.
    - `UUID(as_uuid=True)` ensures the database column stores a UUID
      and SQLAlchemy converts it to a Python `uuid.UUID` object.
    - `primary_key=True` makes this column the table's primary key.
    - `default=uuid.uuid4` automatically generates a new UUID when
      a Register is created.
    - `nullable=False` ensures this field must always have a value.
    - `unique=True` prevents two registers from having the same name.
    - `index=True` creates a database index on this column to make
      queries faster.
    """

    # Primary key column using UUID
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),  # Store as UUID in PostgreSQL
        primary_key=True,  # Primary key
        default=uuid.uuid4,  # Auto-generate a UUID
    )

    # Name column for the register
    name: Mapped[str] = mapped_column(
        nullable=False,  # Cannot be empty
        unique=True,  # Each register name must be unique
        index=True,  # Database index for faster search
    )
