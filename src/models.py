from sqlalchemy import String, Integer, create_engine
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, sessionmaker

DATABASE_URL = 'sqlite:///instance/alembictest2.db'

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class User(Base):
    """User model"""
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f'<User(id={self.id}, name={self.name})>'