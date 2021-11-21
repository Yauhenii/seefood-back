from pydantic.main import BaseModel


class User(BaseModel):
    login_name: str
    full_name: str
    address_name: str
    phone_number: str
