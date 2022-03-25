"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
##Se extraen los datos del archivo
def getData():
    file=open('data.csv',mode='r',encoding='utf-8').readlines()
    data=[rows.replace("\n","").split("\t") for rows in file]
    return data


#Hice una función que tomara una fila en especifico
def getColumn(number):
    data = getData()
    myList=list()
    for row in data:
        myList.append(row[number])
    return myList

##Hice otra función que retorna los máximos y los mínimos de una lista/tupla que tenga 2 elementos
def findMinMax(equivalent):
    dictionary=dict()
    for element in equivalent:
        keyUse=element[0]
        valueUse=int(element[1])
        if keyUse in dictionary.keys():        
            #Para encontar el máximo
            if valueUse>dictionary[keyUse]["top"]:
                dictionary[keyUse]["top"]=valueUse    
            #Para encontrar el minimo
            if valueUse<dictionary[keyUse]["bottom"]:
                dictionary[keyUse]["bottom"]=valueUse
        else:
            dictionary[keyUse]={
                "top":valueUse,
                "bottom":valueUse
            }
    return dictionary

def pregunta_01():

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    solution=sum(int(x) for x in getColumn(1))
    return solution


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    letterCount=dict()
    for letter in sorted(getColumn(0)):
        if letter in letterCount.keys():
            letterCount[letter]+=1
        else:
            letterCount[letter]=1
    return sorted(letterCount.items())

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    dictionary=dict()
    columns=zip(getColumn(0),getColumn(1))
    for row in columns:
        if row[0] in dictionary.keys():
            dictionary[row[0]]+=int(row[1])
        else:
            dictionary[row[0]]=int(row[1])
    return sorted(dictionary.items())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    dictionary=dict()
    months=[date.split("-")[1] for date in getColumn(2)]
    for month in months:
        if month in dictionary.keys():
            dictionary[month]+=1
        else:
            dictionary[month]=1
    return sorted(dictionary.items())


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    dictionary=dict()
    answer=list()
    equivalent=zip(getColumn(0),getColumn(1))

    dictionary=findMinMax(equivalent)

    for element in sorted(dictionary.items()):
        answer.append( (element[0],element[1]["top"], element[1]["bottom"]))
    return answer


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    column5=getColumn(4)
    list_column5=list()
    answer=list()
    for elements in column5:
        for values in elements.split(","):
            list_column5.append(values.split(":"))
    dictionary=findMinMax(list_column5)
    for element in sorted(dictionary.items()):
        answer.append( (element[0],element[1]['bottom'],element[1]['top']) )
    return answer


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    column0=getColumn(0)
    column1=getColumn(1)
    dictionary=dict()
    for index in range(len(column1)):
        key=int(column1[index])
        value=column0[index]
        if key not in dictionary.keys():
            dictionary[key]=list()
        dictionary[key].append(value)
    return sorted(dictionary.items())


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    column0=getColumn(0)
    column1=getColumn(1)
    dictionary=dict()
    for index in range(len(getColumn(0))):
        key=int(column1[index])
        value=column0[index]
        if key not in dictionary.keys():
            dictionary[key]=list()
        if value not in dictionary[key]:
            dictionary[key].append(value)
    for element in dictionary:
        dictionary[element]=sorted(dictionary[element])
    return sorted(dictionary.items())


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    column5=getColumn(4)
    list_column5=list()
    dictionary=dict()
    for elements in column5:
        for values in elements.split(","):
            list_column5.append(values.split(":"))
    
    for elements in list_column5:
        key=elements[0]
        if key in dictionary.keys():
            dictionary[key]+=1
        else:
            dictionary[key]=1

    return dict(sorted(dictionary.items(),key=lambda item: item[0]))


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    answer=list()
    column5=getColumn(4)
    column4=getColumn(3)
    column1=getColumn(0)
    for index in range(0,len(column1)):
        letter=column1[index]
        element4=len(column4[index].split(","))
        element5=len(column5[index].split(","))
        answer.append( (letter,element4,element5) )
    return answer


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    column4=getColumn(3)
    column2=getColumn(1)
    dictionary=dict()
    for index in range(0,len(column2)):
        tuple_key=column4[index].split(",")
        value=int(column2[index])
        for key in tuple_key:
            if key in dictionary.keys():
                dictionary[key]+=value
            else:
                dictionary[key]=value
    return dict(sorted(dictionary.items()))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    column1=getColumn(0)
    column5=[subList.split(",") for subList in getColumn(4)]
    dictionary=dict()
    for i in range(0,len(column1)):
        key=column1[i]
        subList=column5[i]
        for element in subList:
            number=int(element.split(":")[1])
            if key in dictionary.keys():
                dictionary[key]+=number
            else:
                dictionary[key]=number
    return dict(sorted(dictionary.items() ))
