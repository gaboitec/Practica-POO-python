class Estudiante:
    def __init__(self, nombre, carne, carrera, nota_final):
        self.__nombre = nombre
        self.__carne = carne
        self.__carrera = carrera
        self.__nota_final = nota_final

    def get_estudiante(self):
        return f"Nombre: {self.__nombre} Carne: {self.__carne} Carrera: {self.__carrera} Nota final: {self.__nota_final}"
