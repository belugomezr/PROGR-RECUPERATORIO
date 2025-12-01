
def validar_nombre(lista, i):
    """
    La funcion solicita y valida el ingreso del nombre y apellido de un estudiante y asegura que el mismo no este vacio.

    Args:
    - lista (list): Lista donde se almacenan los nombres de los estudiantes.
    - i (int): Índice de la lista donde se guardará el nombre ingresado.

    """

    while True:
        nombre = input("Ingrese nombre y apellido del estudiante: ")
        if nombre == "":
            print("No puede estar vacío. Ingrese nuevamente.")
            continue

        valido = True
        for caracter in range(len(nombre)):
            ascii_val = ord(nombre[caracter])
            if not ((ascii_val >= 97 and ascii_val <= 122) or ascii_val == 32):
                valido = False
                break

        if valido:
            break
        else:
            print("Solo se permiten letras minúsculas.")

    lista[i] = nombre


def validar_genero(lista:list, i:int):
    """
    La funcion solicita y valida el ingreso del género de un estudiante.

    Args:
    - lista (list): Lista donde se almacenan los géneros de los estudiantes.
    - i (int): Índice de la lista donde se guardará el género ingresado.

    """
    genero = input("Ingrese el genero M, F, X: ")
    while genero != "M" and genero != "F" and genero != "X":
        genero = input("Dato incorrecto. Ingrese nuevamente el genero: ")
    lista[i] = genero 

def validar_legajos(lista:list, i:int):
    """
    La funcion solicita y valida el ingreso del número de legajo de un estudiante.
    
    Args:
    - lista (list): Lista donde se almacenan los números de legajo de los estudiantes.
    - i (int): Índice de la lista donde se guardará el legajo ingresado.

    """
    legajos = int(input("Ingrese el numero de legajo: "))
    while legajos < 100000 or legajos > 999999:
        legajos = int(input("Error. Ingrese un legajo de 6 digitos: "))
    lista[i] = legajos

def validar_estados(lista:list, i:int):
    """
    La funcion solicita y valida el ingreso del estado de un estudiante.

    Args:
    - lista (list): Lista donde se almacenan los estados de los estudiantes.
    - i (int): Índice de la lista donde se guardará el estado ingresado.

    """
    estados = int(input("Ingresar el estado 0 O 1: "))
    while estados != 0 and estados != 1:
        estados = int(input("Error. Ingrese un numero valido 0 o 1: "))
    lista[i] = estados

def validar_notas(lista:list, i:int):
    """
    La funcion solicita y valida el ingreso de una nota para un estudiante.

    Args:
    - lista (list): Lista donde se almacenan las notas de los estudiantes.
    - i (int): Índice de la lista donde se guardará la nota ingresada.
    
    """
    nota = int(input("Ingresa la nota: "))
    while nota <= 0 or nota > 10:
        nota = int(input("Error. Ingrese un numero entre 1 y 10:"))
    lista[i] = nota

def cargar_datos(lista_estudiantes, lista_legajos, lista_genero, lista_notas, lista_estados):
    """
    Solicita y valida la carga completa de datos de los estudiantes.

    Args:
    - lista_estudiantes (list): Lista donde se almacenan los nombres de los estudiantes.
    - lista_legajos (list): Lista donde se almacenan los legajos de los estudiantes.
    - lista_genero (list): Lista donde se almacenan los géneros de los estudiantes.
    - lista_notas (list): Lista de listas donde se almacenan las notas de cada estudiante.
    - lista_estados (list): Lista donde se almacenan los estados de los estudiantes.

    """
    print("CARGA DE DATOS DE ESTUDIANTES\n")
    for i in range(3):  
        print(f"--- Estudiante {i+1} ---")
        validar_nombre(lista_estudiantes, i)
        validar_legajos(lista_legajos, i)
        validar_genero(lista_genero, i)
        validar_estados(lista_estados, i)
   
        for j in range(5): 
            validar_notas(lista_notas[i], j)  
    print("Carga finalizada correctamente.\n")


"---"



