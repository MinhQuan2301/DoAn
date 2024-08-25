import pandas as pd
from models import Book
from app import db
def import_books_from_csv(file_path):
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        book = Book(
            ISBN=row['ISBN'],
            title=row['Book-Title'],
            author=row['Book-Author'],
            year_of_publication=row['Year-Of-Publication'],
            publisher=row['Publisher'],
            image_url_s=row['Image-URL-S'],
            image_url_m=row['Image-URL-M'],
            image_url_l=row['Image-URL-L']
        )
        db.session.add(book)
    db.session.commit()