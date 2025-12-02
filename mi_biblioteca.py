

lista_estudiantes = ["dario villanustre", "belen gomez", "kymbo sanchez", "martina lopez", "juan perez","carlos ferreyra",
                    "romina valdez", "luciano bazan","sofia martinez", "alejandro rios", "micaela godoy","santiago gimenez",
                    "valentina rojas", "tomas escobar", "agustina reyes", "federico barros", "camila silva", "rodrigo acosta",
                    "melina flores", "nicolas vera", "alma castro", "daniel mendez", "maria lugo", "ignacio pardo", "julieta soria",
                    "bautista medina", "aylen bravo", "franco salazar", "lucia ramirez","enrique morales"]

lista_genero = ["M", "F", "X",  "F", "M", "M", "F", "M", "F", "M","F", "M", "F", "X", "F", "M","F", "X", "F", "M", "F", "M","F", "M", 
                "F", "M", "F", "M","F", "M"]

lista_legajos = [125620, 124289, 125945, 126001, 126015, 126022, 126034, 126048, 126059, 126063, 126070, 126081, 126095, 126104,
                  126115, 126129, 126130, 126142, 126153, 126167, 126170, 126181, 126195, 126205, 126219, 126223, 126234, 126248,
                  126259, 126260 ]

lista_estados = [1, 0, 1,   1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]

lista_notas = [ [9,8,10,9,10], 
                [9,6,7,6,10], 
                [9,6,7,8,10],
                [8,7,9,8,7],
                [6,5,7,8,9],
                [7,6,5,6,7],
                [10,9,8,9,10],
                [8,8,7,6,7],
                [6,5,6,5,6],
                [9,9,10,9,8],

                [7,8,9,7,8],
                [5,6,6,6,7],
                [8,8,8,9,9],
                [9,7,8,7,9],
                [10,9,9,10,10],
                [6,6,7,6,5],

                [8,7,8,7,8],
                [9,8,7,8,7],
                [6,6,5,6,5],
                [7,7,7,8,8],
                [9,10,9,10,9],
                [5,6,4,5,6],

                [8,9,8,9,8],
                [7,7,6,7,6],
                [10,10,9,10,10],
                [6,5,6,5,6],
                [8,7,8,7,8],
                [9,9,9,9,9],
                [7,6,7,6,7],
                [10,9,10,9,10]]

# lista_estudiantes = [""] * 3
# lista_genero = [""] * 3
# lista_legajos = [0] * 3
# lista_notas = [[0]*5 for _ in range(3)]
# lista_estados = [0] * 3

def mostrar_datos_hardcodeados(lista_estudiantes, lista_genero, lista_legajos, lista_estados, lista_notas):
    """
    La funcion muestra todos los datos cargados de los estudiantes
    
    Args: 
        lista_estudiantes (list): Lista que contiene los nombres de los estudiantes.
        lista_genero (list): Lista con el género de cada estudiante.
        lista_legajos (list): Lista con los números de legajo de cada estudiante.
        lista_estados (list): Lista con los estados de cada estudiante (1 = activo, 0 = inactivo).
        lista_notas (list): Matriz/lista de listas donde cada sublista contiene 
                            las notas de un estudiante en las distintas materias.
        
    """
    print("\n------DATOS CARGADOS-----\n")

    for i in range(len(lista_estudiantes)):
        print("Nombre del estudiante:", lista_estudiantes[i])
        print("Genero:", lista_genero[i])
        print("Numero de legajo:", lista_legajos[i])
        print("Estado:", lista_estados[i])

        notas = lista_notas[i]
        print("Notas:", end=" ")

        for j in range(len(notas)):
            print(notas[j], end="")
            if j < len(notas) - 1:
                print(" - ", end="")   

        print("\n")  
        print("-" * 30)

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any)-> list: 
    """
    La funcion crea e inicializa una matriz con un valor determinado

    Args: 
        cantidad_filas (int): Numero de filas que tendra la matriz.
        cantidad_columnas (int): Numero de columnas que tendra la matriz.
        valor_inicial (any): Valor con el que se inicializará cada posición de la matriz.

    Returns:
        list: Una matriz donde cada elemento está inicializado con 'valor_inicial'.
    
    """
    
    matriz = [] #inicializo la matriz en 0
    for indice in range(cantidad_filas): 
        fila = [valor_inicial] * cantidad_columnas 
        matriz += [fila] 
        
    return matriz

def cargar_notas_en_matriz(matriz:list)->list: #le paso por parametro la matriz 
    """
    Carga en la matriz las notas correspondientes a cada estudiante

    Args:   
        matriz: matriz inicializada en donde se almacenaran las notas 
       
    Return:
         list: La matriz actualizada con todas las notas cargadas.

    """
    for indice in range (len(matriz)): #recorre las filas (0,1,2,etc)
        for j in range(len(matriz[indice])): 
            matriz[indice][j] = lista_notas [indice][j] 
    return matriz

def mostrar_matriz(matriz:list): 
    for indice in range(len(matriz)):
        for j in range(len(matriz[indice])):
                print(matriz[indice][j], end = " ") 
        print(" ")

def mostrar_un_estudiante(estudiantes:list, generos:list, legajos:list, indice:int, estados:list, notas:list):
    """
    La funcion mestra los datos completos de un estudiante.

    Args:
        estudiantes (list): Lista con los nombres de los estudiantes.
        generos (list): Lista con los géneros correspondientes.
        legajos (list): Lista con los números de legajo.
        indice (int): indice del estudiante a mostrar. 
                      Si se envía -1, la función solicitará un legajo por teclado.
        estados (list): Lista con el estado de cada estudiante (1 = activo, 0 = inactivo).
        notas (list): Matriz donde cada sublista contiene las notas del estudiante.
    """

    indice_encontrado = -1

    if indice == -1:
        legajo_buscado = int(input("Ingrese el numero de legajo: "))

        for i in range(len(legajos)):
            if legajos[i] == legajo_buscado:
                indice_encontrado = i
                break
    else:
        indice_encontrado = indice


    if indice_encontrado != -1:
        if estados[indice_encontrado] == 1:  # solo si está activo
            print("-" * 30)
            print("DATOS DEL ESTUDIANTE ENCONTRADO: ")
            print("Nombre del estudiante:", estudiantes[indice_encontrado])
            print("Genero:", generos[indice_encontrado])
            print("Numero de legajo:", legajos[indice_encontrado])
            print("Estado:", estados[indice_encontrado])
            print("Notas:", end=" ")
            for j in range(len(notas[indice_encontrado])):
                print(notas[indice_encontrado][j], end="")
                if j < len(notas[indice_encontrado]) - 1:
                    print(" - ", end="")
            print("\n" + "-" * 30)       
    else:
        print("No se encontró ningún estudiante con ese legajo.")


def mostrar_estudiantes_activos(estudiantes:list, generos:list, legajos:list, estados:list, notas:list ):
    """
    La funcion muestra los datos de todos los estudiantes que se encuentran activos.

    Args:
        estudiantes (list): Lista con los nombres de los estudiantes.
        generos (list): Lista con los generos correspondientes.
        legajos (list): Lista con los numeros de legajo.
        estados (list): Lista que indica el estado de cada estudiante (1 = activo, 0 = inactivo).
        notas (list): Matriz/lista de listas que contiene las notas de cada estudiante. 
         
    """
    for indice in range(len(estudiantes)):
        if estados[indice] == 1: #solo muestra los activos 
            mostrar_un_estudiante(estudiantes, generos, legajos, indice, estados, notas)

def calcular_promedios(matriz:list, estudiantes:list):
    """
    La funcion calcula el promedio de notas de cada estudiante y los muestra junto a su nombre.

    Args:
        matriz (list): Matriz donde cada fila representa a un estudiante y cada columna una materia. Contiene las notas como números enteros.
        estudiantes (list): Lista con los nombres de los estudiantes en el mismo orden que las filas de la matriz.

    Returns:
        list: Lista que contiene el promedio de cada estudiante.
    """

    lista_notas = [] 
    for indice in range(len(matriz)): 
        acumulador = 0
        for j in range(len(matriz[indice])): 
            acumulador += matriz[indice][j]
        lista_promedio = acumulador / len(matriz[indice]) 
        lista_notas += [lista_promedio]
    
    for i in range(len(lista_notas)):
        print(lista_estudiantes[i], ":", lista_notas[i])

    return lista_notas
  

def mostrar_promedios_ordenados(estudiantes:list, generos:list, legajos:list, estados:list, notas:list, lista_notas:list, criterio:str = "asc"):
    """
    La funcion ordena y muestra los promedios de los estudiantes junto con todos sus datos, aplicando el criterio indicado (ascendente o descendente)
   
    Args: 
        estudiantes (list): Lista con los nombres de los estudiantes.
        generos (list): Lista con los géneros correspondientes.
        legajos (list): Lista con los números de legajo.
        estados (list): Lista con los estados del estudiante (1 = activo, 0 = inactivo).
        notas (list): Matriz/lista de listas con las notas de cada estudiante.
        lista_notas (list): Lista con los promedios ya calculados.
        criterio (str): Define el orden del listado:
                        - "asc"  para orden ascendente (menor a mayor).
                        - "desc" para orden descendente (mayor a menor).    
      """

    n = len(lista_notas) 


    for indice in range(n):
        for j in range(0, n - indice - 1):
            if (criterio == "asc" and lista_notas[j] > lista_notas[j + 1]) or (criterio == "desc" and lista_notas[j] < lista_notas[j + 1]):
                # Intercambiar promedios
                aux = lista_notas[j]
                lista_notas[j] = lista_notas[j + 1]
                lista_notas[j + 1] = aux

                # Intercambiar datos correspondientes
                aux = estudiantes[j]
                estudiantes[j] = estudiantes[j + 1]
                estudiantes[j + 1] = aux

                aux = generos[j]
                generos[j] = generos[j + 1]
                generos[j + 1] = aux

                aux = legajos[j]
                legajos[j] = legajos[j + 1]
                legajos[j + 1] = aux

                aux = estados[j]
                estados[j] = estados[j + 1]
                estados[j + 1] = aux

                aux = notas[j]
                notas[j] = notas[j + 1]
                notas[j + 1] = aux

    for i in range(n):
        print("-" * 30)
        print("Nombre:", estudiantes[i])
        print("Género:", generos[i])
        print("Legajo:", legajos[i])
        print("Estado:", estados[i])
        print("Notas:", end=" ")
        for k in range(len(notas[i])):
            print(notas[i][k], end="")
            if k < len(notas[i]) - 1:
                print(" - ", end="")
        print("\nPromedio:", lista_notas[i])
    print("-" * 30)


def identificar_materia_mayor_promedio(matriz_cargada:list)->float:
    """
    La funcion dentifica que materia (columna) tiene el mayor promedio de notas. Luego muestra esa materia junto
    con su promedio utilizando la función `mostrar_una_materia`.

    Args:
        matriz_cargada (list): Matriz de notas donde cada fila representa un estudiante y cada columna una materia.

    Returns:
        float: El promedio correspondiente a la materia con mayor promedio.
    """
    print("MATERIA CON MAYOR PROMEDIO: ")
    lista_notas_acumuladas = [0] * 5
    lista_notas = [0] * 5

    for i in range(len(matriz_cargada)):
        for j in range(len(matriz_cargada[i])):
             lista_notas_acumuladas[j] += matriz_cargada[i][j]
    
    for i in range(len(lista_notas_acumuladas)):
         lista_promedio = lista_notas_acumuladas[i] / len(matriz_cargada)
         lista_notas[i] = lista_promedio
    
    print("-" * 30)

    indice_mayor_promedio = 0
    promedio_mayor = lista_notas[0]
    for i in range(1, len(lista_notas)):
        if lista_notas[i] > promedio_mayor:
            promedio_mayor = lista_notas[i]
            indice_mayor_promedio = i

    mostrar_una_materia(indice_mayor_promedio, promedio_mayor)
    return promedio_mayor


def mostrar_una_materia(i, lista_notas):
     print("Materia_", i+1,":", lista_notas)


def buscar_por_legajo(legajos:list)->int:
    """
    La funcion busca un estudiante en la lista de legajos ingresando un número por teclado.

    Args:
        legajos (list): Lista de números de legajo, ordenados de la misma forma 
                        que el resto de los datos de los estudiantes.

    Returns:
        int: El índice donde se encontró el legajo buscado.
             Devuelve -1 si no existe ningún estudiante con ese legajo.
    
    """
     
    legajo_buscado = int(input("Ingrese el número de legajo del estudiante que desea buscar: "))

    for indice in range(len(legajos)):
        if legajos[indice] == legajo_buscado:
               return indice
    
    return -1 #no encontro ningun legajo con ese numero
          
def devolver_estudiante(indice_encontrado:int, lista_promedio:list)->list:
    """
    La funcion devuelve todos los datos de un estudiante a partir de su índice.

    Args:
    - indice_encontrado (int): índice del estudiante dentro de las listas cargadas. 
                               Si el valor es -1, significa que no se encontró el legajo.
    - lista_promedio (list): lista que contiene los promedios de todos los estudiantes.

    Retorna:
    - list: una lista con los datos del estudiante en el siguiente orden:
            [nombre_apellido, estado, genero, notas_del_estudiante, promedio].
            Si el índice no coincide con ningún estudiante, retorna una lista vacía.
    """
    datos_de_un_estudiante = []
    for i in range (len(lista_estudiantes)):
        if i == indice_encontrado:
            datos_de_un_estudiante = [lista_estudiantes[i], lista_estados[i], lista_genero[i], lista_notas[i], lista_promedio[i]]

    return datos_de_un_estudiante

def mostrar_estudiante_encontrado(datos:list):
    """
    Muestra por pantalla todos los datos de un estudiante previamente buscado.

    Args:
    - datos (list): lista que contiene la información del estudiante en el siguiente orden:
                    [nombre_apellido, estado, genero, lista_notas, promedio].
    """
    print("-" * 30)
    print("DATOS DEL ESTUDIANTE ENCONTRADO: ")
    print("Nombre:",datos[0])
    print("estado:",datos[1])
    print("Genero:",datos[2])
    print("Notas:" , end=" ")
    for i in range(len(datos[3])):
        if i < len(datos[3]) - 1:
            print(datos[3][i], end=" - ")
        else:
            print(datos[3][i]) 
    print("Promedio: ", datos[4])


def mostrar_repeticion_de_notas(matriz_cargada:list)->list:
    """
    La funcion calcula y muestra cuántas veces se repite cada nota en una materia específica.

    Args:
        - matriz_cargada (list): Matriz de notas donde cada fila representa un estudiante y cada columna una materia.
    
    Retorna:
        - list: Una lista de 10 elementos donde cada índice i representa la cantidad 
            de veces que se obtuvo la nota i+1 en la materia seleccionada.
    
    """
    indice_materia = int(input("Ingrese el número de materia (1 a 5): "))
    lista_notas = [0] * 10
    for i in range(len(matriz_cargada)):
        nota = matriz_cargada[i][indice_materia-1]
        lista_notas[nota-1] += 1
    for i in range(len(lista_notas)):
        if i == len(lista_notas) - 1:
            print(lista_notas[i])
        else:
            print(lista_notas[i], end= " - ")
    return lista_notas


