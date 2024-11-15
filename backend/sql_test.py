from sqlmodel import Field, SQLModel, Session, create_engine, select
from datetime import datetime
from typing import Optional

ngrok_adress = "2.tcp.eu.ngrok.io:18795"
mysql_name = "db_users"
mysql_url = f"mysql+pymysql://coavr:0000@{ngrok_adress}/{mysql_name}"


engine = create_engine(mysql_url, echo=True)


# def get_session():
#     with Session(engine) as session:
#         yield session
 
# SessionDep = Annotated[Session, Depends(get_session)]

session=Session(engine)

#creating a class for users
class users(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    credential_id: int | None = Field (default=None, primary_key=True)
    user_type: bool = Field(default=False, nullable=False)  
    email: str = Field(max_length=105)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_login: Optional[datetime] = Field(default=None)


#creating a class for books
class books(SQLModel, table=True):
    book_id: int | None = Field(default=None, primary_key=True)
    title: str = Field (max_length=255)
    author: str = Field (max_length=255)
    publisher: str = Field (max_length=255)
    pagecount: Optional[str] = Field (max_length=45)
    category: str = Field (max_length=100)

#creating a class for user_book links
class userbooklink(SQLModel, table=True):
    link_id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="db_users.users.user_id")
    book_id: int = Field(default=None, foreign_key="db_users.books.book_id")

#creating a class for credentials
class credentials(SQLModel, table=True):
    id_credentials: int | None = Field(default=None, primary_key=True)
    username: str = Field (max_length=45)
    password: str = Field (max_length=64)
    
    def create_users(self):
        session.add(self)
        session.commit()

    def read_users():
        statement = select(credentials)
        results = session.exec(statement)
        for user in results:
            print(user)

    def get_user(username: str):
        statement = select(credentials).where(credentials.username == username)
        results = session.exec(statement)
        user = results.first()
        return user