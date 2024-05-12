import datetime as dt


from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Boolean, DateTime

from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


class Basis(DeclarativeBase):
    pass


class Student(Basis):
    __tablename__ = "students"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True, index=True)
    year = Column(Integer())
    count_credit = Column(Integer())
    created_on = Column(DateTime(), default=dt.datetime.now)
    updated_on = Column(DateTime(), default=dt.datetime.now, onupdate=dt.datetime.now)

    credits = relationship("Credit", back_populates="student")

    def __str__(self):
        return f"<{self.id}> {self.first_name} {self.last_name} aka {self.username}"

    def __repr__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Credit(Basis):
    __tablename__ = "credits"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False, default="(нема инфы)")
    content = Column(String())
    student_id = Column(Integer(), ForeignKey('students.id'))
    is_private = Column(Boolean(), default=True, nullable=False)
    created_on = Column(DateTime(), default=dt.datetime.now)
    updated_on = Column(DateTime(), default=None, onupdate=dt.datetime.now)

    student = relationship("Student", back_populates="credits")
    categories = relationship("Category", back_populates="credits", secondary="credits_categories")

    def __str__(self):
        return f"<{self.id}> {self.title}: {self.content[:20]}"

    def __repr__(self):
        return f"<{self.id}> {self.title}"


class Category(Basis):
    __tablename__ = "categories"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    credits = relationship("Credit", back_populates="categories", secondary="credits_categories")


class CreditCategory(Basis):
    __tablename__ = "credits_categories"
    story_id = Column(Integer(), ForeignKey('credits.id'), primary_key=True)
    category_id = Column(Integer(), ForeignKey('categories.id'), primary_key=True)



engine = create_engine("sqlite:///My Database/Staff.db?echo=True")

Basis.metadata.create_all(engine)

factory = sessionmaker(bind=engine)
