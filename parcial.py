
from MiBiblioteca import *

# Variables necesarias para acceder a ciertos puntos
numero_seleccionado_en_A = None
lista_mayusculas_B = None
filas_seleccionada_en_F = None
columnas_seleccionada_en_F = None
matriz = None

while True:
    
    opcion_seleccionada = generar_menu( "ABCDEFGHI",
        ["Ingresar numero", "Generar lista", "Mostrar lista", "Ingresar una letra",
         "Ordenar lista", "Ingresar tamaño de matriz", "Generar matriz", 
         "Mostrar matriz", "Salir"],
         mensaje_error="[ERROR] Debe seleccionar una de las opciones disponibles."
        )
    
    match opcion_seleccionada:
        case "A":
            numero_seleccionado_en_A = solicitar_y_validar_numero_entero_en_rango(
                "Ingrese un número entero entre 3 y 15: ", minimo=3, maximo=15
                )
        case "B":
            if numero_seleccionado_en_A != None:

                lista_mayusculas_B = generar_lista_aleatoria_letras_mayusculas(
                        cantidad_elementos=numero_seleccionado_en_A,
                        minimo=65, maximo=90
                    )
                print("LISTA GENERADA CORRECTAMENTE")
            elif numero_seleccionado_en_A == None:
                print("------------------------------------------------------------------")
                print("[REQUERIDO] Antes debe ingresar un número con la opción A")        
        case "C":
            if lista_mayusculas_B != None:
                print("Lista de letras mayúsculas generadas: ")
                mostrar_lista(lista_mayusculas_B)
            elif lista_mayusculas_B == None:
                print("------------------------------------------------------------------")
                print(f"[REQUERIDO] Antes debe generar la lista con la opcion B")
        case "D":
            if lista_mayusculas_B != None:
                letra_seleccionada_en_D = solicitar_y_validar_cadena(
                    "Ingrese UNA sola letra(A-Z): ", 
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1
                )
                indices_elementos_coincidentes_con_B = buscar_elemento_en_lista(
                    lista_mayusculas_B, letra_seleccionada_en_D
                    )
                if indices_elementos_coincidentes_con_B != None:
                    print(f"\n\n")
                    print("------------------------------------------------------------------")
                    print("La letra se encuentra en la lista, en la/s posición/es: ")
                    mostrar_lista(indices_elementos_coincidentes_con_B)
                elif indices_elementos_coincidentes_con_B == None:
                    print(f"\n\n")
                    print("------------------------------------------------------------------")
                    print("La letra no se encuentra dentro de la lista generada en B. ")
            elif lista_mayusculas_B == None:
                print("------------------------------------------------------------------")
                print(f"[REQUERIDO] Antes debe generar la lista con la opcion B")
        case "E":
            if lista_mayusculas_B != None:
                orden_seleccionado_en_E = solicitar_y_validar_cadena(
                    "[ASC] Ascendentemente\n[DESC] Descendientemente\nOrdenar: ", 
                    ["ASC","DESC"]
                )
                copia_lista_mayusculas_B = lista_mayusculas_B[ : ]
                ordenar_lista(copia_lista_mayusculas_B, orden_seleccionado_en_E)
                print(f"\n\n")
                print("------------------------------------------------------------------")
                mostrar_lista(copia_lista_mayusculas_B, "Elementos Ordenados: ")
            elif lista_mayusculas_B == None:
                print("------------------------------------------------------------------")
                print("[REQUERIDO] Antes debe generar la lista con la opción B")  
        case "F":
            for i in range(2):
                entero_validado = solicitar_y_validar_numero_entero_en_rango(
                "Ingrese un número entero entre 3 y 10: ", minimo=3, maximo=10
                )
                if i == 0:
                    filas_seleccionada_en_F = entero_validado
                elif i == 1:
                    columnas_seleccionada_en_F = entero_validado         
        case "G":
            if (filas_seleccionada_en_F != None) and (columnas_seleccionada_en_F != None):
                matriz = crear_matriz(filas_seleccionada_en_F,columnas_seleccionada_en_F,0)
                llenar_matriz_aleatoriamente(matriz, 1, 9)
                print("MATRIZ GENERADA CORRECTAMENTE") 
            else:
                print("------------------------------------------------------------------")
                print("[REQUERIDO] Antes debe indicar filas y columnas con la opción F")  
        case "H":
            if matriz != None:
                mostrar_matriz(matriz)
            elif numero_seleccionado_en_A == None:
                print("------------------------------------------------------------------")
                print("[REQUERIDO] Antes debe generar la matriz con la opción G")  
        case "I":
            break
        case _:
            print("[ERROR] Opcion inválida")

