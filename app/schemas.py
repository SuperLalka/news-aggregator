from pydantic import BaseModel


# USER
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


# CITY
class CityBase(BaseModel):
    name: str
    description: str | None = None
    country_id: int | None = None


class CityCreate(CityBase):
    pass


class City(CityBase):
    id: int

    class Config:
        orm_mode = True


# COUNTRY
class CountryBase(BaseModel):
    name: str


class ItemCreate(CountryBase):
    pass


class Item(CountryBase):
    id: int

    class Config:
        orm_mode = True
