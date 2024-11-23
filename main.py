from pymongo import MongoClient
from bson.objectid import ObjectId


def get_database():
    client = MongoClient(
        "mongodb+srv://annafoxika:12345@cluster0.pen8p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsAllowInvalidCertificates=True)

    return client["cats_db"]


db = get_database()
collection = db["cats"]


# ----------------------- CREATE -----------------------
def create_cat(name, age, features):
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        result = collection.insert_one(cat)
        print(f"Кіт доданий із _id: {result.inserted_id}")
    except Exception as e:
        print(f"Помилка при додаванні кота: {e}")


# ----------------------- READ -----------------------
def get_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Помилка при читанні котів: {e}")


def get_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кота з ім'ям '{name}' не знайдено.")
    except Exception as e:
        print(f"Помилка при пошуку кота: {e}")


# ----------------------- UPDATE -----------------------
def update_cat_age(name, new_age):
    try:
        result = collection.update_one(
            {"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Вік кота '{name}' оновлено до {new_age}.")
        else:
            print(f"Кота з ім'ям '{name}' не знайдено.")
    except Exception as e:
        print(f"Помилка при оновленні віку кота: {e}")


def add_feature_to_cat(name, feature):
    try:
        result = collection.update_one(
            {"name": name}, {"$push": {"features": feature}})
        if result.matched_count > 0:
            print(f"Характеристика '{feature}' додана коту '{name}'.")
        else:
            print(f"Кота з ім'ям '{name}' не знайдено.")
    except Exception as e:
        print(f"Помилка при додаванні характеристики: {e}")


# ----------------------- DELETE -----------------------
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кіт з ім'ям '{name}' видалений.")
        else:
            print(f"Кота з ім'ям '{name}' не знайдено.")
    except Exception as e:
        print(f"Помилка при видаленні кота: {e}")


def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Видалено {result.deleted_count} котів.")
    except Exception as e:
        print(f"Помилка при видаленні котів: {e}")


# ----------------------- MAIN -----------------------
if __name__ == "__main__":

    create_cat("Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat("Murzik", 5, ["грайливий", "чорний", "голосний"])

    print("\nУсі коти в колекції:")
    get_all_cats()

    print("\nЗнайти кота за ім'ям:")
    get_cat_by_name("Barsik")

    print("\nОновлення віку кота:")
    update_cat_age("Barsik", 4)

    print("\nДодати характеристику коту:")
    add_feature_to_cat("Barsik", "дружелюбний")

    print("\nУсі коти після оновлення:")
    get_all_cats()

    print("\nВидалення кота за ім'ям:")
    delete_cat_by_name("Murzik")

    print("\nВидалення всіх котів:")
    delete_all_cats()

    print("\nУсі коти після видалення:")
    get_all_cats()
