from typing import Annotated
from fastapi import Depends
from sqlmodel import Field, SQLModel, Session, create_engine, select

ngrok_adress = "0.tcp.eu.ngrok.io:13777"
mysql_name = "db_users"
mysql_url = f"mysql+pymysql://coavr:0000@{ngrok_adress}/{mysql_name}"


engine = create_engine(mysql_url, echo=True)


# def get_session():
#     with Session(engine) as session:
#         yield session

# SessionDep = Annotated[Session, Depends(get_session)]

session=Session(engine)

class Users_Test(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str | None = None
    hashed_password: str | None = None

    def create_users(self):
        session.add(self)
        session.commit()

    def read_users():
        statement = select(Users_Test)
        results = session.exec(statement)
        for user in results:
            print(user)

    def get_user(username: str):
        statement = select(Users_Test).where(Users_Test.username == username)
        results = session.exec(statement)
        user = results.first()
        return user

    def update_users(self):
        statement = select(Users_Test).where(Users_Test.id == self.id)
        results = session.exec(statement)
        user = results.one()

        user = self
        session.add(user)
        session.commit()
        session.refresh(user)

# TODO update and delete
