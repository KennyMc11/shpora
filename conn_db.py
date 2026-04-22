import sqlite3

def get_users():
    conn = sqlite3.connect('app.db')
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM users")
        return cursor.fetchall()
    finally:
        conn.close()

# Использование
users = get_users()
print(users)


# 1. ПОДКЛЮЧЕНИЕ
conn = библиотека.connect(**параметры)

# 2. КУРСОР (для SQL-запросов)
cursor = conn.cursor()

# 3. ВЫПОЛНЕНИЕ
cursor.execute("SQL ЗАПРОС")
conn.commit()          # для INSERT/UPDATE/DELETE
result = cursor.fetchall()  # для SELECT

# 4. ЗАКРЫТИЕ (обязательно!)
cursor.close()
conn.close()


#PostgreSQL
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='mydb',
    user='postgres',
    password='123'
)