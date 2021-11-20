from pydantic.main import BaseModel


class User(BaseModel):
    full_name: str
    address: str
    phone_number: str