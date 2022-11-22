from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker, scoped_session

engine = create_engine("sqlite+pysqlite:///local.db", echo=True, future=True, connect_args={"check_same_thread": False})
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


# Dependency
def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()
