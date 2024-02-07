from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from alembic.config import Config
from alembic import command


from src.models import User\

def test_add_user():
    # arrange

    DATABASE_URL = 'sqlite:///:memory:'
    # DATABASE_URL = 'sqlite:///tests/test_db.db'

    alembic_cfg = Config()
    alembic_cfg.set_main_option("script_location", "src/alembic")
    alembic_cfg.set_main_option("sqlalchemy.url", DATABASE_URL)
    command.upgrade(alembic_cfg, "head")

    engine = create_engine(DATABASE_URL, echo=True)

    new_user = User(id=1, name='test_user')

    #act
    with Session(engine) as session:
        session.add(new_user)
        session.commit()

    # act
    # db = SessionLocal()
    # db.add(new_user)
    # db.commit()

    # assert
        db_user = session.query(User).filter(User.id == 1).first()
    assert db_user.id == 1
    assert db_user.name == 'test_user'


