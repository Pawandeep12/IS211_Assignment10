import sqlite3

def load_data():
    connection = sqlite3.connect('pets.db')
    cursor = connection.cursor()

    # Insert data into person table
    persons = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23),
    ]
    
    cursor.executemany("INSERT INTO person VALUES (?, ?, ?, ?)", persons)

    # Insert data into pet table
    pets = [
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1),
    ]

    cursor.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", pets)

    # Insert data into person_pet table
    person_pets = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6),
    ]

    cursor.executemany("INSERT INTO person_pet VALUES (?, ?)", person_pets)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    load_data()
    print("Data loaded into pets.db.")
