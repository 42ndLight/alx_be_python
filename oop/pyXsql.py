import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user ="root",
    password="sqlpass",
    database="library_db"
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE  IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), ISBN VARCHAR(255)) "
)

sql = "INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)"
val = []
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")

mycursor.execute("SELECT * FROM books")
myresult = mycursor.fetchall()

for row in myresult:
    print(f"BOOK: {row[1]}, AUTHOR: {row[2]}, ISBN: {row[3]}")

srch = input("Enter book title to search: ")
mycursor.execute("SELECT * FROM books WHERE title LIKE %s", (srch,))
myresult = mycursor.fetchone()

print(myresult)

del_book = input("Enter book title to delete: ")
mycursor.execute("DELETE FROM books WHERE id = %s", (del_book,))
mydb.commit()

print(mycursor.rowcount, "record(s) deleted.")

# Close connections
mycursor.close()
mydb.close()

print("Database connection closed.")