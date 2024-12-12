import sqlite3

connect = sqlite3.connect("bookstore.db")
cursor = connect.cursor()

##############################


# Insert authors
cursor.execute("INSERT INTO authors (name, description) VALUES ('Marcus Aurelius', 'Italy');") # ID 1
cursor.execute("INSERT INTO authors (name, description) VALUES ('Ryan Holiday', 'USA');") # ID 2
cursor.execute("INSERT INTO authors (name, description) VALUES ('Adam Grant', 'USA');") # ID 3
cursor.execute("INSERT INTO authors (name, description) VALUES ('Robin Sharma', 'USA');") # ID 4
cursor.execute("INSERT INTO authors (name, description) VALUES ('Friedrich Nietzsche', 'Germany');") # ID 5
cursor.execute("INSERT INTO authors (name, description) VALUES ('Albert Camus', 'France');") # ID 6

# Insert categories
cursor.execute("INSERT INTO categories (name) VALUES ('Philosophy');") # ID 1
cursor.execute("INSERT INTO categories (name) VALUES ('Non-Fiction');") # ID 2
cursor.execute("INSERT INTO categories (name) VALUES ('Self-Help');") # ID 3

# Insert stores
cursor.execute("INSERT INTO stores (name, address, opening_time, departure_time) VALUES ('Mementos Perisur', '13th ABC Street, Park Avenue', '10:00 am', '9:00 pm');") # ID 1
cursor.execute("INSERT INTO stores (name, address, opening_time, departure_time) VALUES ('Mementos Condesa', '45th EFG Street, Condesa', '12:00 am', '8:00 pm');") # ID 2
cursor.execute("INSERT INTO stores (name, address, opening_time, departure_time) VALUES ('Mementos Coyoacan', '43rd Main Street, Coyoacan', '10:00 am', '9:00 pm');") # ID 3

# Insert Books
cursor.execute("INSERT INTO books (title, author_id, category_id, store_id, price, stock) VALUES ('Meditations', 1, 1, 1, 12.99, 15);")
cursor.execute("INSERT INTO books (title, author_id, category_id, store_id, price, stock) VALUES ('The Obstacle is the Way', 2, 2, 1, 12.99, 15);")
cursor.execute("INSERT INTO books (title, author_id, category_id, store_id, price, stock) VALUES ('The Daily Stoic', 2, 2, 1, 12.99, 15);")
cursor.execute("INSERT INTO books (title, author_id, category_id, store_id, price, stock) VALUES ('The Ego is the Enemy', 2, 2, 1, 12.99, 15);")
cursor.execute("INSERT INTO books (title, author_id, category_id, store_id, price, stock) VALUES ('Stillness is the Key', 2, 2, 1, 12.99, 15);")
cursor.execute("INSERT INTO books (title, author_id, category_id, store_id, price, stock) VALUES ('Think Again', 3, 3, 2, 12.99, 15);")
cursor.execute("INSERT INTO books (title, author_id, category_id, store_id, price, stock) VALUES ('Hidden Gems', 3, 3, 2, 12.99, 15);")
cursor.execute("INSERT INTO books (title, author_id, category_id, store_id, price, stock) VALUES ('The Monk Who Sold His Ferrari', 4, 3, 2, 12.99, 15);")
cursor.execute("INSERT INTO books (title, author_id, category_id, store_id, price, stock) VALUES ('Beyond Good and Evil', 5, 1, 3, 12.99, 15);")
cursor.execute("INSERT INTO books (title, author_id, category_id, store_id, price, stock) VALUES ('Thus Spoke Zarathustra', 5, 1, 3, 12.99, 15);")
cursor.execute("INSERT INTO books (title, author_id, category_id, store_id, price, stock) VALUES ('The Myth of Sisyphus', 6, 1, 3, 12.99, 15);")


##############################

connect.commit()
connect.close()

print("Datos de ejemplo insertados.")