class Estudiante:
    def __init__(self, nombre, carne, carrera, nota_final):
        self.__nombre = nombre
        self.__carne = carne
        self.__carrera = carrera
        self.__nota_final = nota_final

    def get_estudiante(self):
        return f"Nombre: {self.__nombre} Carne: {self.__carne} Carrera: {self.__carrera} Nota final: {self.__nota_final}"

    def get_nota(self):
        return self.__nota_final
        
    def get_carne(self):
        return self.__carne

class ListaEstudiantes:
    def __init__(self):
        self.lista = []

    def agregar_estudiante(self, estudiante: Estudiante):
        self.lista.append(estudiante)

    def mostrar_lista(self):
        try:
            for estudiante in self.lista:
                print(estudiante.get_estudiante())
        except Error:
            print("Ningun estudiante agregado")

    def buscar(self, carne)
        for estudiante in self.lista:
            if carne == estudiante.get_carne():
                return estudiante
            
    def get_promedios(self):
        promedios = 0
        try:
            for estudiante in self.lista:
                promedios += estudiante.get_nota()
            
            return promedios / len(self.lista)
        except error:
            print("Ningun estudiante agregado")

listaEstudiantes = ListaEstudiantes()