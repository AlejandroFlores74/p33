"""         TRABAJO PRÁCTICO N°3:
    MATERIA: ALGORITMOS Y ESTRUCTURAS DE DATOS
    Curso: 1K15
    Año: 2022
    Participantes:
    Barreto Juan Manuel, 77643, [1K15]
    Carrizo Nahuel, 87557, [1K15]
    Flores Principe Alejandro Hernan, 79059, [1K15] """

from registro import *
import string
import random


def mostrar_menu():
    print("\n==================================================================================")
    print("\t\t\t\t\t\t\tMenu de Búsqueda")
    print("==================================================================================")
    print('\t1- Cargar proyectos', end=' | ')
    print('2- Listar proyectos', end=' | ')
    print('3- Actualizar proyecto')
    print('\t4- Resumen por lenguaje', end=' | ')
    print('5- Resumen por año', end=' | ')
    print('6- Filtrar lenguaje')
    print('\t' * 3, '7- Productividad:', end=' | ')
    print('8- Salir del Programa', end=' | ')
    print("\n==================================================================================")

# 111

def convert_leng():
    lenguajes = ['Python', 'Java', ' C++ ', 'Javascript', 'Shell', 'HTML', 'Ruby',
                 'Swift', 'C#', 'VB', 'Go']
    return lenguajes


def crear_proyecto(vec, n):
    for i in range(n):
        # el numero debe aparecer UNA SOLA vez
        numero = random.randrange(1, 100)
        fecha = random.randint(1, 100)
        titulo = random.sample(string.ascii_letters, 1)
        lenguaje = random.choice(convert_leng())
        cant_lineas = random.randint(500, 800)
        proyecto = Proyecto(numero, fecha, titulo, lenguaje, cant_lineas)
        vec.append(proyecto)


# Número de proyecto
# Título
# Fecha de actualización con el formato dd-mm-yyyy validando que el año esté entre 2000 y 2022
# Lenguaje (siendo 0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8: C#, 9:VB, 10:Go)
# Cantidad de líneas de código


def ordenar_proyecto(vec):
    n = len(vec)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if vec[i].titulo > vec[j].titulo:
                vec[i], vec[j] = vec[j], vec[i]


def mostrar_proyecto(vec):
    for proyecto in vec:
        print(proyecto)


def busqueda_secuencial(vec, x):
    res = None
    for i in range(len(vec)):
        if vec[i].numero == x:
            res = i
            break

    return res



def principal():
    vec = []
    op = -1
    while op != -2:
        mostrar_menu()
        op = int(input('\ningrese un valor 1-6:'))
        if op == 1:
            n = int(input('ingrese la cantidad de proyectos a cargar:'))
            if n > 0:
                crear_proyecto(vec, n)
                # mostrar_proyecto(vec)
                print('proyecto/s cargados...')
            else:
                print("\n==================================================================================")
                print('ERROR, ingrese cantidad mayor a 0')
        elif op == 2:
            if vec != []:
                print("\n==================================================================================")
                ordenar_proyecto(vec)
                mostrar_proyecto(vec)
            else:
                print("\n==================================================================================")
                print("El proyecto no esta cargado")
        elif op == 3:
            x = int(input('ingrese valor a buscar:'))
            busqueda_secuencial(vec, x)
            if x > 0:
                print("\n==================================================================================")
                print('el valor fue encontrado', str(vec[x]))
            else:
                print("\n==================================================================================")
                print('el valor no se encuentra')
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            pass
        else:
            print("==================================================================================")
            print('\t' * 6, 'PROGRAMA FINALIZADO')
            print("==================================================================================")
            break


if __name__ == '__main__':
    principal()
