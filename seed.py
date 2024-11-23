import psycopg2
from faker import Faker
import random

connection = psycopg2.connect(
    dbname="annaivanova",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()

fake = Faker()


def seed_users(n=10):
    emails = set()  # Створюємо унікальні email
    for _ in range(n):
        fullname = fake.name()
        email = fake.email()

        while email in emails:
            email = fake.email()
        emails.add(email)
        cursor.execute(
            "INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))


# Додавання випадкових завдань
def seed_tasks(n=30):
    cursor.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT id FROM status")
    status_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(n):
        title = fake.sentence(nb_words=5)
        description = fake.text(max_nb_chars=200) if random.choice(
            [True, False]) else None
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        cursor.execute(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
            (title, description, status_id, user_id)
        )


# Заповнення таблиць
seed_users(10)
seed_tasks(30)

connection.commit()
cursor.close()
connection.close()
