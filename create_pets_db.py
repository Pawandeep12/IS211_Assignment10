import sqlite3

def create_database():
    connection = sqlite3.connect('pets.db')
    cursor = connection.cursor()

    # Create the tables for person, pet, and person_pet
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pet (
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT,
        age INTEGER,
        dead INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS person_pet (
        person_id INTEGER,
        pet_id INTEGER,
        FOREIGN KEY (person_id) REFERENCES person(id),
        FOREIGN KEY (pet_id) REFERENCES pet(id)
    )
    ''')

    connection.commit()
    connection.close()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_database()
