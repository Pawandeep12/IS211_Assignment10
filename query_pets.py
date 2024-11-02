import sqlite3

def query_pets():
    connection = sqlite3.connect('pets.db')
    cursor = connection.cursor()

    while True:
        person_id = input("Enter person ID (-1 to exit): ")
        
        if person_id == '-1':
            print("Exiting.")
            break

        cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
        person = cursor.fetchone()

        if person:
            first_name, last_name, age = person
            print(f"{first_name} {last_name}, {age} years old")

            cursor.execute("""
                SELECT pet.name, pet.breed, pet.age, pet.dead
                FROM pet
                JOIN person_pet ON pet.id = person_pet.pet_id
                WHERE person_pet.person_id = ?
            """, (person_id,))
            pets = cursor.fetchall()

            if pets:
                for name, breed, age, dead in pets:
                    status = "deceased" if dead == 1 else "alive"
                    print(f"  - {name}, a {breed}, {age} years old, is {status}.")
            else:
                print("  No pets found.")
        else:
            print("Person not found.")

    connection.close()

if __name__ == "__main__":
    query_pets()
