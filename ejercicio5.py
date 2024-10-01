class Nodo:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe 
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None


    def insertar(self, nombre, es_heroe):
        if self.raiz is None:
            self.raiz = Nodo(nombre, es_heroe)
        else:
            self._insertar_recursivo(self.raiz, nombre, es_heroe)


    def _insertar_recursivo(self, nodo, nombre, es_heroe):
        if nombre < nodo.nombre:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(nombre, es_heroe)
            else:
                self._insertar_recursivo(nodo.izquierda, nombre, es_heroe)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(nombre, es_heroe)
            else:
                self._insertar_recursivo(nodo.derecha, nombre, es_heroe)

    # a) 
    def listar_villanos(self, nodo):
        if nodo:
            self.listar_villanos(nodo.izquierda)
            if not nodo.es_heroe:
                print(nodo.nombre)
            self.listar_villanos(nodo.derecha)

    # b) 
    def listar_superheroes_con_c(self, nodo):
        if nodo:
            self.listar_superheroes_con_c(nodo.izquierda)
            if nodo.es_heroe and nodo.nombre.startswith('C'):
                print(nodo.nombre)
            self.listar_superheroes_con_c(nodo.derecha)

    # c) 
    def contar_superheroes(self, nodo):
        if nodo is None:
            return 0
        cuenta = self.contar_superheroes(nodo.izquierda) + self.contar_superheroes(nodo.derecha)
        if nodo.es_heroe:
            cuenta += 1
        return cuenta

    # d)
    def corregir_doctor_strange(self, nodo, nombre_incorrecto, nombre_correcto):
        if nodo is None:
            return
        if nodo.nombre == nombre_incorrecto:
            nodo.nombre = nombre_correcto
            return
        self.corregir_doctor_strange(nodo.izquierda, nombre_incorrecto, nombre_correcto)
        self.corregir_doctor_strange(nodo.derecha, nombre_incorrecto, nombre_correcto)

    # e)
    def listar_superheroes_descendente(self, nodo):
        if nodo:
            self.listar_superheroes_descendente(nodo.derecha)
            if nodo.es_heroe:
                print(nodo.nombre)
            self.listar_superheroes_descendente(nodo.izquierda)

    # f) 
    def separar_bosque(self, nodo, arbol_heroes, arbol_villanos):
        if nodo:
            if nodo.es_heroe:
                arbol_heroes.insertar(nodo.nombre, nodo.es_heroe)
            else:
                arbol_villanos.insertar(nodo.nombre, nodo.es_heroe)
            self.separar_bosque(nodo.izquierda, arbol_heroes, arbol_villanos)
            self.separar_bosque(nodo.derecha, arbol_heroes, arbol_villanos)

    # g) 
    def contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar_nodos(nodo.izquierda) + self.contar_nodos(nodo.derecha)

    def listar_en_orden(self, nodo):
        if nodo:
            self.listar_en_orden(nodo.izquierda)
            print(nodo.nombre)
            self.listar_en_orden(nodo.derecha)

if __name__ == "__main__":
    arbol = Arbol()
    arbol.insertar("Iron Man", True)
    arbol.insertar("Thanos", False)
    arbol.insertar("Doctor Strange", True)
    arbol.insertar("Loki", False)
    arbol.insertar("Captain America", True)
    arbol.insertar("Black Widow", True)
    arbol.insertar("Ultron", False)
    arbol.insertar("Red Skull", False)

    print("Villanos en orden alfabético:")
    arbol.listar_villanos(arbol.raiz)
    
    print("\nSuperhéroes que empiezan con 'C':")
    arbol.listar_superheroes_con_c(arbol.raiz)

    print(f"\nCantidad de superhéroes: {arbol.contar_superheroes(arbol.raiz)}")

    print("\nCorrigiendo Doctor Strange...")
    arbol.corregir_doctor_strange(arbol.raiz, "Doctor Strage", "Doctor Strange")
    
    print("\nSuperhéroes en orden descendente:")
    arbol.listar_superheroes_descendente(arbol.raiz)
    
    
    arbol_heroes = Arbol()
    arbol_villanos = Arbol()
    arbol.separar_bosque(arbol.raiz, arbol_heroes, arbol_villanos)

    print(f"\nCantidad de nodos en el árbol de héroes: {arbol_heroes.contar_nodos(arbol_heroes.raiz)}")
    print(f"Cantidad de nodos en el árbol de villanos: {arbol_villanos.contar_nodos(arbol_villanos.raiz)}")

    print("\nHéroes en orden alfabético:")
    arbol_heroes.listar_en_orden(arbol_heroes.raiz)

    print("\nVillanos en orden alfabético:")
    arbol_villanos.listar_en_orden(arbol_villanos.raiz)
