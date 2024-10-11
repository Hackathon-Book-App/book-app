from openai import BaseModel


class UserCreds(BaseModel):
    user_name: str
    password: str