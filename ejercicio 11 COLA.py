from collections import deque

characters_queue = deque([
    {"name": "Leia Organa", "planet": "Alderaan"},
    {"name": "Luke Skywalker", "planet": "Tatooine"},
    {"name": "Han Solo", "planet": "Corellia"},
    {"name": "Yoda", "planet": "Dagobah"},
    {"name": "Jar Jar Binks", "planet": "Naboo"},
    {"name": "Chewbacca", "planet": "Kashyyyk"}
])

def show_characters_from_planets(characters, planets):
    return [char['name'] for char in characters if char['planet'] in planets]

planets_to_show = ["Alderaan", "Endor", "Tatooine"]
characters_from_planets = show_characters_from_planets(characters_queue, planets_to_show)
print("Personajes de Alderaan, Endor y Tatooine:", characters_from_planets)

def find_planet_of_characters(characters, names):
    return {char['name']: char['planet'] for char in characters if char['name'] in names}

names_to_find = ["Luke Skywalker", "Han Solo"]
planets_of_characters = find_planet_of_characters(characters_queue, names_to_find)
print("Planeta natal de Luke Skywalker y Han Solo:", planets_of_characters)

def insert_character_before(characters, new_character, target_name):
    temp_queue = deque()
    inserted = False
    while characters:
        char = characters.popleft()
        if char['name'] == target_name and not inserted:
            temp_queue.append(new_character)
            inserted = True
        temp_queue.append(char)
    return temp_queue

new_character = {"name": "Ahsoka Tano", "planet": "Shili"}
characters_queue = insert_character_before(characters_queue, new_character, "Yoda")
print("Cola después de insertar a Ahsoka Tano antes de Yoda:", list(characters_queue))

def delete_character_after(characters, target_name):
    temp_queue = deque()
    skip_next = False
    while characters:
        char = characters.popleft()
        if skip_next:
            skip_next = False
            continue
        temp_queue.append(char)
        if char['name'] == target_name:
            skip_next = True
    return temp_queue

characters_queue = delete_character_after(characters_queue, "Jar Jar Binks")
print("Cola después de eliminar el personaje después de Jar Jar Binks:", list(characters_queue))
