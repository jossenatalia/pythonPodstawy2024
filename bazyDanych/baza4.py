# podejście za pomocą ORM
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, session, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# echo=True logowanie co się dzieje w bazie danych
engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Anna Kowalska", age=20)
session.add(new_user)
session.commit()
session.close()

users = session.query(User).all()
for user in users:
    print(user.name, user.age)

