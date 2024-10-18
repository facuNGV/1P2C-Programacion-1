import random


'''
Interacción con Usuario
'''
def solicitar_y_validar_cadena(
        mensaje:str, opciones:list|str, longitud:int=None, 
        mensaje_error:str="[Error]"
        )->str:
    """
    Esta función pide al usuario que ingrese una cadena, valida que el usuario
    ingrese un dato dentro de las opciones disponibles, y de la longitud que se
    indique por parametro si es el caso.
    Recibe: El mensaje a mostrar al usuario, un iterable con las opciones
    disponibles, y opcionalmente una longitud para la cadena
    Retorna: El dato elegido por el usuario validado.
    """
    cadena = input(mensaje)
    if longitud != None:
        while medir_coleccion(cadena) != longitud:
            cadena = input(f"{mensaje_error} {mensaje}")

    while (cadena in opciones) == False:
        cadena = input(f"{mensaje_error}\n{mensaje}")
    
    return cadena


def generar_menu(
        items:str, opciones:list,
        mensaje:str=f"\nSeleccione una de las opciones disponibles: "
        ):
    """
    Esta función muestra por consola un menú de opciones que el usuario puede
    seleccionar, y solicita al usuario que seleccione una de las disponibles.
    Recibe: Los items de cada una de las opciones, las opciones en sí, y un 
    mensaje que mostrar al usuario.
    Retorna: La opcion seleccionada por el usuario una vez validada.
    """
    print("-------------------------MENÚ-------------------------------------")
    for i in range(len(opciones)):
        print(f"|               {items[i]}) {opciones[i]}")
    print("------------------------------------------------------------------")
    opcion_seleccionada = solicitar_y_validar_cadena(mensaje,items,1)
    print("------------------------------------------------------------------")
    print(f"\n\n")
    return opcion_seleccionada


def solicitar_y_validar_numero_entero_en_rango(
        mensaje:str, minimo:int, maximo:int
        )->int:
    """
    Esta función pide un entero al usuario y valida que se encuentre
    dentro de un rango numérico determinado (inclusive)
    Recibe: Un mensaje que se imprimira al usuario, un rango numérico
    Retorna: El mismo número validado y casteado
    """
    numero = input(mensaje)
    while (comprobar_numero_dentro_de_rango(numero, minimo, maximo) != True) or (
            determinar_numero(numero) != 'int'
            ):
        numero = input(f"[ERROR] {mensaje}")
    numero = castear_dato(numero)
    return numero



'''
Situacionales de Funcionalidad
'''

def comprobar_numero_dentro_de_rango(
        numero:int|float, minimo:int|float, maximo:int|float
        )->bool:
    """
    Esta función valida si un determinado numero se encuentra dentro de un 
    rango determinado (inclusive)
    Recibe: Un numero, un determinado rango numérico
    Retorna: True en caso de que el numero se encuentre dentro del rango
    False caso contrario o None caso de que no se haya ingresado un numero
    """
    retorno = None
    if determinar_numero(numero) != False:
        numero = castear_dato(numero)
        if numero >= minimo and numero <= maximo: 
            retorno = True
        else:
            retorno = False
    return retorno


def determinar_numero(dato:str)->bool|str:
        '''
        Esta función determina si el dato ingresado es un número y su tipo.
        Permite la coma o el punto para decimales indistintamente (cuidado en los flaots).
        Recibe: un str cualquiera
        Retorna: el tipo de dato en caso de que sea un número, caso contrario
        devuelve False
        '''
        retorno = False
        # Verificar si se ingreso algo o no se ingreso nada
        if not dato:
            return False
        # Variables para controlar mas adelante si tiene coma y digitos
        tiene_coma = False
        tiene_digitos = False
        # Contador de Iteraciónes
        pos = 0
        # Recorrer cada carácter en la cadena
        dato = str(dato)
        for char in dato:
            if char == '-':
                # Si el signo negativo no está primero no es un número
                if pos != 0:
                    return False
            elif char == ',' or char == ".":
                # La coma no puede estar al principio, ni al final, no pueden
                # haber dos y el caracter anterior no puede ser "-"
                if pos == 0 or pos == (len(dato)-1) or tiene_coma == True or caracter_anterior == "-":
                    return False
                tiene_coma = True
            # Todos los demás caracteres deben ser dígitos.
            elif ord(char) >= 48 and ord(char)<= 57:
                tiene_digitos = True
            else:
                return False
            pos += 1
            caracter_anterior = char
        # Determinar que tipo es
        if tiene_digitos == True and tiene_coma == True:
            retorno = "float"
        elif tiene_digitos == True and tiene_coma == False:
            retorno = "int"
        return retorno


def castear_dato(dato:str|int|float)->str|int|float:
    """
    Esta función castea un dato determinado al tipo que le corresponda
    Recibe: un dato
    Retorna: el mismo dato casteado a su tipo correspondiente
    """
    retorno = None
    # determinar_numero devolverá float aunque el decimal tenga un punto (.) o una coma (,)
    # Transformo en un punto (.) independientemente de como este el decimal:
    if determinar_numero(dato) == "float":
        float_coma_string = str(dato)
        float_punto_string = ""
        for digito in float_coma_string:
            if digito == ",":
                float_punto_string += "."
            else:
                float_punto_string += digito
        retorno = float(float_punto_string)
    elif determinar_numero(dato) == "int":
        retorno = int(dato)
    elif type(dato) == str:
        retorno = str(dato)
    elif type(dato) == bool:
        retorno = bool(dato)

    return retorno


def medir_coleccion(coleccion:str|list)->int:
    """
    Esta función determina de cuantos caracteres esta compuesto un iterable
    Recibe: un iterable cualquiera
    Retorna: el número de caracteres que compone el iterable
    """
    contador = 0
    for _ in coleccion:
        contador += 1
    return contador

# listas
def buscar_elemento_en_lista(lista:list, dato:int)->list|None:
    '''
    Esta función determina si un elemento se encuentra dentro de una lista
    Recibe: Una lista, un elemento a buscar dentro de la lista.
    Retorna: Los índices de la lista en donde se encuentra el elemento buscado.
    O "None" en caso de no encontrar coincidencias.
    '''
    coincidencias = []
    for i in range(medir_coleccion(lista)):
        if dato == lista[i]:
            coincidencias += [i]
    if medir_coleccion(coincidencias) == 0:
        coincidencias = None
    return coincidencias


def generar_lista_aleatoria_letras_mayusculas(
        cantidad_elementos:int, minimo:int, maximo:int
        )->list:
    """
    Esta función genera una lista de elementos aleatorios, utilizando código
    ASCII.
    Recibe: cantidad de elementos a generar, y entre qué rango numérico se
    encuentran los caracteres que queremos generar según código ASCII.
    Retorna: La lista generada
    """
    lista_elementos_aleatorios = []
    for _ in range(cantidad_elementos):
        numero_aleatorio = random.randint(minimo, maximo)
        elemento = chr(numero_aleatorio)
        lista_elementos_aleatorios += [elemento]
    return lista_elementos_aleatorios


def mostrar_lista(lista:list, mensaje:str="")->None:
    """
    Esta función muestra una lista al usuario
    Recibe: Una lista a mostrar, un mensaje opcional a mostrar
    Retorna: None
    """
    if mensaje != "":
        print(mensaje)
    for elemento in lista:
        if elemento == lista[-1]:
            print(elemento)
        else:
            print(f"{elemento}", end=" , ")


def ordenar_lista(lista:list, criterio:str="ASC")->bool:
    '''
    Esta función ordena una lista en base a un criterio determinado
    Recibe: Una lista a ordenar, el criterio por el cual ordenar la lista.
    Retorna: Verdadero en caso de haber ordenado, caso contrario; Falso.
    '''
    bandera = False
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if (criterio == "ASC" and lista[i] > lista[j]) or (
                criterio == "DESC" and lista[i] < lista[j]
                ):
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
                bandera = True
    return bandera

# Matrices
def crear_matriz(
        cantidad_filas:int, cantidad_columnas:int, valor_inicial:any=0
        )->list:
    """
    Esta función se encarga de crear una matriz vacía
    Recibe: la cantidad de filas y columnas que va a tener la matriz, y un valor
    inicial opcional que llenara la matriz
    Retorna: la matriz 
    """
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]

    return matriz


def llenar_matriz_aleatoriamente(matriz_vacia:list, desde:int, hasta:int)->None:
    '''
    Esta función se encarga de llenar una matriz vacia con números aleatorios
    Recibe: la matriz a llenar, un rango numérico aceptable como elementos de la
    matriz.
    Retorna: None
    '''
    for i in range(len(matriz_vacia)):
        for j in range(len(matriz_vacia[i])):
            matriz_vacia[i][j] = str(random.randint(desde,hasta))


def mostrar_matriz(matriz:list)->None:
    """
    Esta función se encarga de darle un formato a la matriz y mostrarla.
    Recibe: Una matriz
    Retorna: None
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j < (len(matriz[i])-1):
                print(f"{matriz[i][j]}", end="|")
            else:
                print(f"{matriz[i][j]}", end="")
        print()
        
        if i < (len(matriz)-1):
            print (("-" * len(matriz[i]))*2)



























