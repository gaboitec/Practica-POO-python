import Clases

def menu():
    print("\nREGISTRO DE ESTUDIANTES")
    print("\n1. Registrar un nuevo estudiante")
    print("2. Mostrar a todos los estudiantes")
    print("3. Buscar a un estudiante por carné")
    print("4. Calcular el promedio de notas de todos los estudiantes")

while True:
    menu()
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nuevo_estudiante = Estudiante(input("Nombre del estudiante: "), input("Carné del estudiante: "), input("Carrera del estudiante: "), input("Nota final del estudiante: "))
