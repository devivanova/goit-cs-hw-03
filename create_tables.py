import psycopg2

db_config = {
    'dbname': 'annaivanova',
    'user': 'postgres',
    'password': '12345',
    'host': 'localhost',
    'port': '5432'
}

CREATE_TABLES_SQL = """
-- Створення таблиці users
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Створення таблиці status
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- Створення таблиці tasks
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER REFERENCES status(id) ON DELETE SET NULL,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
"""

try:
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    cur.execute(CREATE_TABLES_SQL)
    conn.commit()
    print("Таблиці успішно створено!")

except Exception as e:
    print(f"Помилка під час створення таблиць: {e}")
finally:
    if conn:
        cur.close()
        conn.close()
