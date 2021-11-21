from pydantic.main import BaseModel


class Category(BaseModel):
    category_name: str
    avg_calories: float
