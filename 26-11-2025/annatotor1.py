from pydantic import BaseModel

class Shetty(BaseModel):
    id : int
    name : str

e_data = {
    "id": 1,
    "name": "Alice",
    "details": {
      "age": 25,
      "city": "NY"
    }
  }
js = Shetty(**e_data)
print(js.name)