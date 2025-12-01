
from mi_biblioteca import *
from validaciones import *

menu = """
==================================
MENÚ PRINCIPAL
1. Cargar datos de los estudiantes // Mostrar datos cargados
2. Mostrar datos de estudiantes activos
3. Mostrar promedios de estudiantes
4. Mostrar promedios ordenados
5. Mostrar materia con mayor promedio
6. Buscar estudiante por legajo
7. Mostrar cantidad de repeticiones de notas
8. Salir
==================================
Opcion: """


def mostrar_menu(menu):
    matriz = []
    lista_promedios = []
    while True:
        opcion_seleccionada = input(menu)
        if len(matriz) == 0 and opcion_seleccionada != "1" and opcion_seleccionada != "8":
            print("Primero debe ingresar los datos en la opcion 1: ")
            continue
        match opcion_seleccionada:
            case "1":
                mostrar_datos_hardcodeados(lista_estudiantes, lista_genero, lista_legajos, lista_estados, lista_notas)
                #cargar_datos(lista_estudiantes, lista_legajos, lista_genero, lista_notas, lista_estados)
                matriz = inicializar_matriz(30,5,None)
                cargar_notas_en_matriz(matriz)
            case "2":
                mostrar_estudiantes_activos(lista_estudiantes, lista_genero, lista_legajos,lista_estados, lista_notas)
                mostrar_un_estudiante(lista_estudiantes, lista_genero, lista_legajos, -1, lista_estados, lista_notas) #el indice -1 indica que debo pedir el legajo
            case "3":
                print("Promedios de los estudiantes:")
                lista_promedios = calcular_promedios(matriz, lista_estudiantes)
            case "4":
                print("Promedios ordenados: ")
                mostrar_promedios_ordenados(lista_estudiantes, lista_genero, lista_legajos, lista_estados, lista_notas, lista_promedios,"asc")
            case "5":
                identificar_materia_mayor_promedio(matriz)
            case "6":
                indice_encontrado = buscar_por_legajo(lista_legajos)
                if indice_encontrado != -1:
                    datos_estudiantes = devolver_estudiante(indice_encontrado, lista_promedios)
                    mostrar_estudiante_encontrado(datos_estudiantes)
                else:
                    print("Error legajo no existente")
            case "7":
                mostrar_repeticion_de_notas(matriz)
            case "8":
                print("Fin del programa")
                break
            case _:
                print("Opcion no valida. Ingrese una opcion nuevamente: ")

mostrar_menu(menu)
        
                




