import sqlite3

def query_person_pets(person_id):
    connection = sqlite3.connect('pets.db')
    cursor = connection.cursor()

    # Query person data
    cursor.execute("SELECT first_name, last_name, age FROM person WHERE id=?", (person_id,))
    person = cursor.fetchone()

    if person:
        print(f"{person[0]} {person[1]}, {person[2]} years old")

        # Query pets for that person
        cursor.execute("""
            SELECT pet.name, pet.breed, pet.age 
            FROM pet
            JOIN person_pet ON pet.id = person_pet.pet_id
            WHERE person_pet.person_id = ?
        """, (person_id,))
        
        pets = cursor.fetchall()
        for pet in pets:
            print(f"{person[0]} owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old.")
    else:
        print("Person not found.")

    connection.close()

if __name__ == "__main__":
    while True:
        person_id = int(input("Enter a person's ID (or -1 to exit): "))
        if person_id == -1:
            break
        query_person_pets(person_id)
