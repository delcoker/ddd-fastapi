from pydantic import BaseModel


class UserDto(BaseModel):
    id: int
    username: str
    email: str

    def __repr__(self):
        return f'<User {self.username}>'

    class Config:
        from_attributes = True
