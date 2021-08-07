from humps.camel import case
from pydantic import BaseModel


def to_camel(string: str) -> str:
    result: str = case(string)
    return result


class User(BaseModel):
    first_name: str
    last_name: str
    age: int

    class Config:
        allow_population_by_field_name = True
        alias_generator = to_camel
