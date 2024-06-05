# Импортируем из библитеки SqlAlchemy нужные функции и классы
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, CheckConstraint
from sqlalchemy import Integer, String, Boolean, DateTime, Numeric, SmallInteger

# Импортируем из подмодуля ORM функции и классы, предназначенные для
# высокоуровневой работы с базой данных посредством построения объектной модели ORM
# (ORM ~ object-relational model)
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


# Так просто надо сделать
class Basis(DeclarativeBase):
    pass


class User(Basis):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    gender = Column(String, nullable=False)

    messages_sent = relationship("Message", foreign_keys="[Message.sender_id]", back_populates="sender")
    messages_received = relationship("Message", foreign_keys="[Message.receiver_id]", back_populates="receiver")

    def __str__(self):
        return f"<{self.id}> {self.first_name} {self.last_name} aka {self.username}"

    def __repr__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Message(Basis):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String)

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])


engine = create_engine("sqlite:///My Database/mail.db?echo=True")

Basis.metadata.create_all(engine)

factory = sessionmaker(bind=engine)
