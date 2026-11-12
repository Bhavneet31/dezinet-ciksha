from pydantic import ValidationError

from schemas import User

user_data = {
    "name": "Neet",
    "age": -5,
    "email": "neet@example.com"
}

try:
    user = User.model_validate(user_data)
    print(user.model_dump())

except ValidationError as e:
    print("Invalid user data!")

    for error in e.errors():
        print("Field:", error["loc"])
        print("Message:", error["msg"])