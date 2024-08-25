from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func, Float
from app import db, app
from sqlalchemy.orm import relationship
import dao


class Book(db.Model):
    __tablename__ = 'books'

    ISBN = Column(String(13), primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    year_of_publication = Column(Integer)
    publisher = Column(String(255))
    image_url_s = Column(String(255))
    image_url_m = Column(String(255))
    image_url_l = Column(String(255))
    rant_id = relationship('Rating', backref='book', lazy=True)

    __table_args__ = {'extend_existing': True}


class User(db.Model):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    location = Column(String(255))
    age = Column(Float)
    rant_id = relationship('Rating', backref='user', lazy=True)
    __table_args__ = {'extend_existing': True}


class Rating(db.Model):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.user_id), nullable=False)
    isbn = Column(String(13), ForeignKey(Book.ISBN), nullable=False)
    book_rating = Column(Integer)


    __table_args__ = {'extend_existing': True}


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    dao.import_books_from_excel('C:/Users/MinhQuan/OneDrive/Desktop/DoAn/DoAn/app/static/data/Book1.xlsx')
