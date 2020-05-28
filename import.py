from csv import DictReader
import sqlite3

def get_author_id(author):
    """Returns author_id of author"""
    cursor.execute("""SELECT id FROM search_author WHERE name = ?""", (author, ))
    auth_id = cursor.fetchone()
    if auth_id is not None:
        return auth_id[0]
    cursor.execute("""INSERT INTO search_author (name) VALUES (?)""", (author, ))
    cursor.execute("""SELECT id FROM search_author WHERE name = ?""", (author, ))
    auth_id = cursor.fetchone()
    return auth_id[0]



dbconnection = sqlite3.connect("db.sqlite3")
cursor = dbconnection.cursor()

with open('books.csv') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        isbn = row["isbn"]
        title = row["title"]
        author = row["author"]
        year = row["year"]
        author_id = get_author_id(author)
        cursor.execute("""INSERT INTO search_book (title, isbn, year, author_id_id)
            VALUES ( ?, ?, ?, ?)""", (title, isbn, year, author_id))

dbconnection.commit()
dbconnection.close()
