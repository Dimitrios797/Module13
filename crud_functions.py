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
def get_all_products():
    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Получение всех записей из таблицы Products
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    # Закрытие соединения
    conn.close()

    return products

def add_user(username, email, age):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Проверка существования пользователя по имени
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    if existing_user is None:
        # Вставка нового пользователя
        cursor.execute('''
        INSERT INTO Users (username, email, age, balance) 
        VALUES (?, ?, ?, ?)''', (username, email, age, 1000))
        conn.commit()
    else:
        print(f"Пользователь с именем '{username}' уже существует.")

    conn.close()

def is_included(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()

    conn.close()

    return user is not None