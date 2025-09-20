"""crud - create, read, update, delete, edit"""

from users.schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:
    user = user_in.model_dump()
    return {"Success": "true", "user": user}
