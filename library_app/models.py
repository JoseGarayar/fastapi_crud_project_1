from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from .database import Base

import enum

class CategoryEnum(enum.Enum):
    EARTH_SCIENCES = 'Earth Sciences'
    ECONOMICS = 'Economics'
    POLITICAL_SCIENCE = 'Political Science'
    LAW = 'Law'
    COMPUTER_SCIENCE = 'Computer Science'
    ASTRONOMY = 'Astronomy'
    UNIVERSAL_LITERATURE = 'Universal Literature'
    ART_AND_DESIGN = 'Art and Design'


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    publisher_name = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    category = Column(Enum(CategoryEnum), index=True)

    author = relationship("Author", back_populates="books")


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer, nullable=True)

    books = relationship("Book", back_populates="author")


