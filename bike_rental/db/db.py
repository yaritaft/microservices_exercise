from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.models import Base, User


def _create_session():
    # db_url = environ.get('DATABASE_URL')
    engine = create_engine(
        'postgresql+psycopg2://myuser:mypass@0.0.0.0:5432/my_micro_db'
    )
    Base.metadata.create_all(engine)
    create_session = sessionmaker(bind=engine)
    return create_session()


session = _create_session()


class UserRepository:
    def set_user(name, fullname, nickname):
        ed_user = User(name=name, fullname=fullname, nickname=nickname)
        session.add(ed_user)
        session.commit()

    def get_user_by_name(name):
        our_user = session.query(User).filter_by(name=name).first() 
        return our_user
