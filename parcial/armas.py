
class ArmaOneHand:
    def __init__(self,nombre,pAtack,mAtack, tipo, habilidad):
        if not isinstance(tipo,str) or not isinstance(nombre,str) or not isinstance(pAtack,int) or not isinstance(mAtack,int) or not isinstance(habilidad,str):
            raise  TypeError("Uno de los valores ingresados no es correcto")
        self.nombre = nombre
        self.pAtack = pAtack
        self.mAtack = mAtack
        self.tipo = tipo
        self.habilidad = habilidad
    def __str__(self):
        return (f'{self.nombre}:\n    P.Atack = {self.pAtack}\n    M.Atack = {self.mAtack}\n    Tipo: {self.tipo}\n    Habilidad especial = {self.habilidad}')
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.next = None
class ListaEnlazada:
    def __init__(self):
        self.head = None
    def agregar(self,nuevoDato):
        nuevoPersonaje = Nodo(nuevoDato)
        if self.head is None:
            self.head = nuevoPersonaje
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevoPersonaje
    def buscarElemento(self, nombre):
        if not isinstance(nombre,str):
            raise TypeError("Ese nombre no pertenece a la clase de armas buscadas")
        nombre = nombre.lower()
        if self.head is None:
            print("La lista esta vacia.")
            return
      
    def mostrarLista(self):
        actual = self.head
        while actual is not None:
            print(actual.dato.nombre)
        actual = actual.next
    def borrarElemento(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("Ese nombre no pertenece a la clase 'Armas de una mano'")
        nombre= nombre.lower()
            
        if self.head is None:
            print("La lista esta vacia")
            return
        if self.head.dato.nombre.lower() == nombre:
            self.head = self.head.next
            print(f"El arma '{nombre}' ha sido eliminada.")
            return 
        current = self.head
        while current.next and current.next.dato.nombre.lower() != nombre:
            current = current.next
        if not current.next:
            print(f'El arma {nombre} no se encuentra en la lista')
            return
        current.next = current.next.next
        print(f"El arma '{nombre}' ha sido eliminada.")
        
        
rugidoDeAcero = ArmaOneHand("Rugido de Acero", 2,1, "Fist", "Destello mundial")
FiloSusurrante = ArmaOneHand("Filo Susurrante", 3,1,"Daga", "Destello provincial")
cortaViento = ArmaOneHand("Cortaviento", 4,2,"Espada", "Destello municipal")
dagaDeLaNiebla = ArmaOneHand("Daga de la Niebla", 3,1,"Daga", "Destello barrial")
garraDeLasSombras =ArmaOneHand("Garra de Sombras", 5,3, "Fist", "Destello comunal")
destelloDeCarmesi = ArmaOneHand("Destello Carmesí",1,7,"Baston", "Destello interestelar")
golpeDelHalcon = ArmaOneHand("Golpe del Halcón", 10,5, "Fist", "Destello caotico")
mandibulaDelLoBo = ArmaOneHand("Mandíbula del Lobo", 20,10,"Fist", "Destello endosiado")
listaArmasOneHand = ListaEnlazada()
listaPersonajes = ListaEnlazada()
listaArmasOneHand.agregar(rugidoDeAcero)
listaArmasOneHand.agregar(FiloSusurrante)
listaArmasOneHand.agregar(cortaViento)
listaArmasOneHand.agregar(dagaDeLaNiebla)
listaArmasOneHand.agregar(garraDeLasSombras)
listaArmasOneHand.agregar(destelloDeCarmesi)
listaArmasOneHand.agregar(golpeDelHalcon)
listaArmasOneHand.agregar(mandibulaDelLoBo)



"""Amanecer Ardiente
Grito del Dragón
Espina del Sol
Justiciera Fantasmal
Veneno de Sirena
Rompecielos
Tempestad de Cristal
Castigadora Élfica
Ocaso Plateado
Aguijón Celestial
Ígnea de los Ancestros
Desterrador Oscuro
Némesis del Caos
Filo del Inmortal
Colmillo de la Tempestad
Guardiana del Vacío
Juramento del Guerrero
Venganza del Espíritu
Ardiente del Infinito
Trueno de los Titanes
Juicio de los Dioses
"""
