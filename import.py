from csv import DictReader
import sqlite3

def get_author_id(author):
    """Returns author_id of author"""
    cursor.execute("""SELECT id FROM authors WHERE name = ?""", (author, ))
    auth_id = cursor.fetchone()
    if auth_id is not None:
        return auth_id[0]
    cursor.execute("""INSERT INTO authors (name) VALUES (?)""", (author, ))
    cursor.execute("""SELECT id FROM authors WHERE name = ?""", (author, ))
    auth_id = cursor.fetchone()
    return auth_id[0]



dbconnection = sqlite3.connect("testenv.db")
cursor = dbconnection.cursor()

with open('books.csv') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        isbn = row["isbn"]
        title = row["title"]
        author = row["author"]
        year = row["year"]
        author_id = get_author_id(author)
        cursor.execute("""INSERT INTO books (author_id, title, isbn, year)
            VALUES ( ?, ?, ?, ?)""", (author_id, title, isbn, year))

dbconnection.commit()
dbconnection.close()
