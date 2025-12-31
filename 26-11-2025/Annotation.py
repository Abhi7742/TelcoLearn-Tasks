from typing import Annotated
from annotated_types import Gt
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    age: Annotated[int, Gt(18)]

try:
    user_input = input("Enter your age: ")

    # Pass the string directly → Pydantic converts automatically
    user = User(age=user_input)

    print("Valid age:", user.age)

except ValidationError as e:
    print("Validation error:", e)
