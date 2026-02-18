from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = "sqlite:///./finance.db"

engine = create_engine(
    database_url,
    connect_args={"check_same_threads": False}
)

SesssionLocal = sessionmaker(autocommit = False, autoFlush = False, bind=engine)

base = declarative_base()

def get_db():
    db = SesssionLocal()
    try:
        yield db
    finally:
        db.close()
