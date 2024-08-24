import sqlite3

def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products

# Функция для добавления продуктов (используйте ее для наполнения базы данных)
def add_product(title, description, price):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (title, description, price))
    conn.commit()
    conn.close()

# Вызовите эту функцию один раз для заполнения базы данных
def populate_db():
    initiate_db()
    add_product("Витамины 1", "Описание витаминов 1", 100)
    add_product("Витамины 2", "Описание витаминов 2", 200)
    add_product("Витамины 3", "Описание витаминов 3", 300)
    add_product("Витамины 4", "Описание витаминов 4", 400)

# Раскомментируйте следующую строку при первом запуске для заполнения базы данных
# populate_db()