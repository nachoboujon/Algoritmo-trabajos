from collections import deque

characters_queue = deque([
    {"real_name": "Tony Stark", "superhero_name": "Iron Man", "gender": "M"},
    {"real_name": "Steve Rogers", "superhero_name": "Capitán América", "gender": "M"},
    {"real_name": "Natasha Romanoff", "superhero_name": "Black Widow", "gender": "F"},
    {"real_name": "Scott Lang", "superhero_name": "Ant-Man", "gender": "M"},
    {"real_name": "Carol Danvers", "superhero_name": "Capitana Marvel", "gender": "F"},
    {"real_name": "Wanda Maximoff", "superhero_name": "Scarlet Witch", "gender": "F"}
])

def find_real_name_of_superhero(characters, superhero_name):
    for char in characters:
        if char["superhero_name"] == superhero_name:
            return char["real_name"]
    return None

real_name_captain_marvel = find_real_name_of_superhero(characters_queue, "Capitana Marvel")
print("El nombre del personaje de Capitana Marvel es:", real_name_captain_marvel)

def get_female_superheroes(characters):
    return [char["superhero_name"] for char in characters if char["gender"] == "F"]

female_superheroes = get_female_superheroes(characters_queue)
print("Superhéroes femeninos:", female_superheroes)

def get_male_real_names(characters):
    return [char["real_name"] for char in characters if char["gender"] == "M"]

male_real_names = get_male_real_names(characters_queue)
print("Nombres de personajes masculinos:", male_real_names)

def find_superhero_of_real_name(characters, real_name):
    for char in characters:
        if char["real_name"] == real_name:
            return char["superhero_name"]
    return None

superhero_of_scott_lang = find_superhero_of_real_name(characters_queue, "Scott Lang")
print("El superhéroe de Scott Lang es:", superhero_of_scott_lang)

def get_characters_starting_with(characters, letter):
    return [char for char in characters if char["real_name"].startswith(letter) or char["superhero_name"].startswith(letter)]

characters_starting_with_S = get_characters_starting_with(characters_queue, "S")
print("Personajes cuyos nombres comienzan con S:", characters_starting_with_S)

def check_character_in_queue(characters, real_name):
    for char in characters:
        if char["real_name"] == real_name:
            return char["superhero_name"]
    return None

superhero_of_carol_danvers = check_character_in_queue(characters_queue, "Carol Danvers")
if superhero_of_carol_danvers:
    print(f"Carol Danvers está en la cola, y su nombre de superhéroe es: {superhero_of_carol_danvers}")
else:
    print("Carol Danvers no está en la cola.")
