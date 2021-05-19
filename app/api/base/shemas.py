from pydantic import BaseModel


def to_camel_case(string: str) -> str:
    if string != "__root__":
        words = string.split('_')
        string = words[0] + "".join(word.capitalize() for word in words[1:])
    return string


class OrmBaseModel(BaseModel):
    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        orm_mode = True
