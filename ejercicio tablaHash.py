def createHashTable(size):
    return [[] for _ in range(size)]

def hashType(key, size):
    return hash(key) % size

def hashLastDigit(key, size):
    return int(str(key)[-1]) % size

def hashLevel(key, size):
    return key % size

def insert(table, key, value, hashFunction, size):
    index = hashFunction(key, size)
    table[index].append(value)

def searchByLastDigit(table, digits, size):
    result = []
    for digit in digits:
        index = hashLastDigit(digit, size)
        result.extend(table[index])
    return result

def searchByLevel(table, multiples, size):
    result = []
    for i in range(size):
        for pokemon in table[i]:
            if any(pokemon['level'] % multiple == 0 for multiple in multiples):
                result.append(pokemon)
    return result

def searchByType(table, types, size):
    result = []
    for pokeType in types:
        index = hashType(pokeType, size)
        result.extend(table[index])
    return result

size = 10
typeTable = createHashTable(size)
lastDigitTable = createHashTable(size)
levelTable = createHashTable(size)

def loadPokemon(number, name, types, level):
    pokemon = {'number': number, 'name': name, 'types': types, 'level': level}
    for pokeType in types:
        insert(typeTable, pokeType, pokemon, hashType, size)
    insert(lastDigitTable, number, pokemon, hashLastDigit, size)
    insert(levelTable, level, pokemon, hashLevel, size)

loadPokemon(1, "Bulbasaur", ["Planta", "Veneno"], 5)
loadPokemon(4, "Charmander", ["Fuego"], 8)
loadPokemon(7, "Squirtle", ["Agua"], 15)
loadPokemon(25, "Pikachu", ["Eléctrico"], 22)

print("Pokémons con números terminados en 3, 7 y 9:")
print(searchByLastDigit(lastDigitTable, [3, 7, 9], size))

print("Pokémons con niveles múltiplos de 2, 5 y 10:")
print(searchByLevel(levelTable, [2, 5, 10], size))

print("Pokémons de tipos Acero, Fuego, Eléctrico, Hielo:")
print(searchByType(typeTable
