class Nodo:
    def __init__(self, nombre, derrotado_por, descripcion=""):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.descripcion = descripcion
        self.capturada_por = None
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, derrotado_por, descripcion=""):
        if not self.raiz:
            self.raiz = Nodo(nombre, derrotado_por, descripcion)
        else:
            self._insertar(self.raiz, nombre, derrotado_por, descripcion)

    def _insertar(self, actual, nombre, derrotado_por, descripcion):
        if nombre < actual.nombre:
            if actual.izquierda is None:
                actual.izquierda = Nodo(nombre, derrotado_por, descripcion)
            else:
                self._insertar(actual.izquierda, nombre, derrotado_por, descripcion)
        else:
            if actual.derecha is None:
                actual.derecha = Nodo(nombre, derrotado_por, descripcion)
            else:
                self._insertar(actual.derecha, nombre, derrotado_por, descripcion)

    def listar_inorden(self, nodo):
        if nodo:
            self.listar_inorden(nodo.izquierda)
            print(f"Criatura: {nodo.nombre}, Derrotado por: {nodo.derrotado_por}")
            self.listar_inorden(nodo.derecha)

    def cargar_descripcion(self, nombre, descripcion):
        nodo = self.buscar(nombre)
        if nodo:
            nodo.descripcion = descripcion

    def mostrar_informacion(self, nombre):
        nodo = self.buscar(nombre)
        if nodo:
            print(f"Nombre: {nodo.nombre}")
            print(f"Derrotado por: {nodo.derrotado_por}")
            print(f"Descripción: {nodo.descripcion}")
        else:
            print(f"{nombre} no se encontró en el árbol.")

    def derrotadores_top(self):
        derrotadores = {}
        self._contar_derrotadores(self.raiz, derrotadores)
        top_derrotadores = sorted(derrotadores.items(), key=lambda x: x[1], reverse=True)[:3]
        for derrotador, cantidad in top_derrotadores:
            print(f"{derrotador}: {cantidad} criaturas derrotadas")

    def _contar_derrotadores(self, nodo, derrotadores):
        if nodo:
            if nodo.derrotado_por:
                if nodo.derrotado_por in derrotadores:
                    derrotadores[nodo.derrotado_por] += 1
                else:
                    derrotadores[nodo.derrotado_por] = 1
            self._contar_derrotadores(nodo.izquierda, derrotadores)
            self._contar_derrotadores(nodo.derecha, derrotadores)

    def listar_derrotadas_por(self, nombre):
        self._listar_derrotadas_por(self.raiz, nombre)

    def _listar_derrotadas_por(self, nodo, nombre):
        if nodo:
            self._listar_derrotadas_por(nodo.izquierda, nombre)
            if nodo.derrotado_por == nombre:
                print(nodo.nombre)
            self._listar_derrotadas_por(nodo.derecha, nombre)

    def listar_no_derrotadas(self):
        self._listar_no_derrotadas(self.raiz)

    def _listar_no_derrotadas(self, nodo):
        if nodo:
            self._listar_no_derrotadas(nodo.izquierda)
            if nodo.derrotado_por == "":
                print(nodo.nombre)
            self._listar_no_derrotadas(nodo.derecha)

    def capturar_por_heracles(self):
        criaturas = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
        for criatura in criaturas:
            nodo = self.buscar(criatura)
            if nodo:
                nodo.capturada_por = "Heracles"

    def buscar(self, nombre):
        return self._buscar(self.raiz, nombre)

    def _buscar(self, actual, nombre):
        if not actual or actual.nombre == nombre:
            return actual
        if nombre < actual.nombre:
            return self._buscar(actual.izquierda, nombre)
        else:
            return self._buscar(actual.derecha, nombre)

    def eliminar(self, nombre):
        self.raiz = self._eliminar(self.raiz, nombre)

    def _eliminar(self, nodo, nombre):
        if not nodo:
            return nodo
        if nombre < nodo.nombre:
            nodo.izquierda = self._eliminar(nodo.izquierda, nombre)
        elif nombre > nodo.nombre:
            nodo.derecha = self._eliminar(nodo.derecha, nombre)
        else:
            if not nodo.izquierda:
                return nodo.derecha
            if not nodo.derecha:
                return nodo.izquierda
            temp = self._buscar_min(nodo.derecha)
            nodo.nombre = temp.nombre
            nodo.derecha = self._eliminar(nodo.derecha, temp.nombre)
        return nodo

    def _buscar_min(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def modificar_nombre(self, nombre_viejo, nombre_nuevo):
        nodo = self.buscar(nombre_viejo)
        if nodo:
            nodo.nombre = nombre_nuevo
        else:
            print(f"{nombre_viejo} no se encontró en el árbol.")

    def listar_por_nivel(self):
        if not self.raiz:
            return
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            print(actual.nombre)
            if actual.izquierda:
                cola.append(actual.izquierda)
            if actual.derecha:
                cola.append(actual.derecha)

    def mostrar_capturadas_por(self, capturador):
        print(f"Criaturas capturadas por {capturador}:")
        self._mostrar_capturadas_por(self.raiz, capturador)

    def _mostrar_capturadas_por(self, nodo, capturador):
        if nodo:
            self._mostrar_capturadas_por(nodo.izquierda, capturador)
            if nodo.capturada_por == capturador:
                print(nodo.nombre)
            self._mostrar_capturadas_por(nodo.derecha, capturador)

if __name__ == "__main__":
    arbol = Arbol()
    arbol.insertar("Ceto", "", "Monstruo marino")
    arbol.insertar("Tifón", "Zeus", "Serpiente gigante con múltiples cabezas")
    arbol.insertar("Equidna", "Argos Panoptes", "")
    arbol.insertar("Dino", "", "")
    arbol.insertar("Pefredo", "", "")
    arbol.insertar("Enio", "Gerión", "")
    arbol.insertar("Escila", "", "")
    arbol.insertar("Caribdis", "", "")
    arbol.insertar("Euríale", "Átropos", "")
    arbol.insertar("Esteno", "Minotauro de Creta", "")
    arbol.insertar("Medusa", "Perseo", "")
    arbol.insertar("Ladón", "Heracles", "")

    print("Listado en orden de criaturas y quienes las derrotaron:")
    arbol.listar_inorden(arbol.raiz)

    arbol.cargar_descripcion("Talos", "Gigante de bronce que protege Creta")

    print("\nInformación de Talos:")
    arbol.mostrar_informacion("Talos")

    print("\nLos 3 héroes o dioses que derrotaron más criaturas:")
    arbol.derrotadores_top()

    print("\nCriaturas derrotadas por Heracles:")
    arbol.listar_derrotadas_por("Heracles")

    print("\nCriaturas no derrotadas:")
    arbol.listar_no_derrotadas()

    arbol.capturar_por_heracles()

    print("\nBuscar criatura Escila:")
    arbol.mostrar_informacion("Escila")

    arbol.eliminar("Basilisco")
    arbol.eliminar("Sirenas")

    print("\nListado final de criaturas:")
    arbol.listar_inorden(arbol.raiz)

   
