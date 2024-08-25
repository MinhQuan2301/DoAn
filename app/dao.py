import pandas as pd
from models import *
from app import db


def import_books_from_excel(file_path):
    try:
        # Đọc dữ liệu từ tệp Excel
        df = pd.read_excel(file_path, engine='openpyxl')  # Sử dụng 'openpyxl' engine để đọc .xlsx

        for index, row in df.iterrows():
            book = Book(
                ISBN=row['ISBN'],
                title=row['Book Title'],
                author=row['Book-Author'],
                year_of_publication=row['Year-Of-Publication'],
                publisher=row['Publisher'],
                image_url_s=row['Image-URL-S'],
                image_url_m=row['Image-URL-M'],
                image_url_l=row['Image-URL-L']
            )
            db.session.add(book)
        db.session.commit()
        print("Dữ liệu đã được nhập thành công.")
    except Exception as e:
        print(f"Có lỗi xảy ra khi đọc tệp: {e}")
