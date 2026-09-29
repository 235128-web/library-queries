import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price INTEGER,
    stock INTEGER
);
INSERT INTO books VALUES
(1, 'Clean Code', 'Non-Fiction', 1200, 10),
(2, 'The Silent Patient', 'Fiction', 1350, 2),
(3, 'Data Science Basics', 'Non-Fiction', 1450, 7),
(4, 'Atomic Habits', 'Self-Help', 950, 15),
(5, 'The Alchemist', 'Fiction', 800, 3),
(6, 'Sapiens', 'Non-Fiction', 1100, 6),
(7, 'It Ends with Us', 'Fiction', 700, 1),
(8, 'Rich Dad Poor Dad', 'Finance', 650, 20);
""")
conn.commit()

print("Part a - Books above Rs.1000 (sorted):")
cur.execute("""
SELECT title, price
FROM books
WHERE price > 1000
ORDER BY price DESC;
""")
for row in cur.fetchall():
    print(row)

print("Part b - With alias book_title:")
cur.execute("""
SELECT title AS book_title, price
FROM books
WHERE price > 1000
ORDER BY price DESC;
""")
for row in cur.fetchall():
    print(row)

print("Part c - Low-stock Fiction books:")
cur.execute("""
SELECT title, genre, price, stock
FROM books
WHERE genre = 'Fiction' AND stock < 5;
""")
for row in cur.fetchall():
    print(row)

conn.close()