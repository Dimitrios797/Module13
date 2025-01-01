import sqlite3

# Путь к базе данных
DB_PATH = 'products.db'


def initiate_db():
    """Создает таблицу Products, если она еще не создана."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')

    conn.commit()
    conn.close()


def get_all_products():
    """Возвращает все записи из таблицы Products."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()

    return products


def add_sample_products():
    """Добавляет тестовые продукты в таблицу Products."""
    products = [
        ('Продукт1', 'Описание продукта 1', 100),
        ('Продукт2', 'Описание продукта 2', 200),
        ('Продукт3', 'Описание продукта 3', 300),
        ('Продукт4', 'Описание продукта 4', 400),
    ]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)

    conn.commit()
    conn.close()


# Вызовите эту функцию один раз, чтобы добавить продукты
add_sample_products()
