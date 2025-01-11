import sqlite3

connection = sqlite3.connect('module_14_4.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')
    connection.commit()

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    data = cursor.fetchall()
    return data

def add_products():
    for i in range (1,5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Продукт{i}', f'Описание{i}', f'{100*i}'))
    connection.commit()


if __name__ == '__main__':
  initiate_db()
  add_products()
  connection.close()