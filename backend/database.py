from dotenv import load_dotenv
import os
from sqlmodel import Session, create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    connect_args={"ssl": {}}
)


def get_session():
    with Session(engine) as session:
        yield session