import Clases

def menu():
    print("\nREGISTRO DE ESTUDIANTES")
    print("\n1. Registrar un nuevo estudiante")
    print("2. Mostrar a todos los estudiantes")
    print("3. Buscar a un estudiante por carné")
    print("4. Calcular el promedio de notas de todos los estudiantes")
    print("0. SALIR")

while True:
    menu()
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nuevo_estudiante = Estudiante(input("Nombre del estudiante: "), input("Carné del estudiante: "), input("Carrera del estudiante: "), input("Nota final del estudiante: "))
        listaEstudiantes.agregar_estudiante(nuevo_estudiante)
    elif opcion == "2":
        print("\nESTUDIANTES REGISTRADOS:")
        listaEstudiantes.mostrar_lista()
    elif opcion == "3":
        print("\nBUSCAR ESTUDIANTE:")
        carneIn = input("Ingrese el carné a buscar: ")
        
        estudiante_encontrado = listaEstudiantes.buscar(carneIn)
        estudiante_encontrado.get_estudiante()
    elif opcion == "4":
        print("\nPROMEDIO DE TODAS LAS NOTAS:")
        print(listaEstudiantes.get_promedio)
    elif opcion == "0":
        break
    else:
        print("\nOpción no válida")
