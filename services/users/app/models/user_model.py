from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str


sample_users = [
    User(
        id=1,
        username="test_user1"
    ),
    User(
        id=2,
        username="test_user2"
    ),
    User(
        id=3,
        username="test_user3"
    )
]
