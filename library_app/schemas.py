from pydantic import BaseModel

from library_app.models import CategoryEnum


class BookBase(BaseModel):
    title: str
    publisher_name: str | None


class BookCreate(BookBase):
    category: CategoryEnum


class BookUpdate(BookBase):
    pass


class Book(BookCreate):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    age: int | None


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    books: list[Book] = []

    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True