import random
n = int(input('¿Cuántos números desea ingresar?: '))

lista = []

for i in range(n):
    num = int(input(f'{i+1}. Ingrese un número: '))
    lista.append(num)

def bubble_sort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2]

        menores = [x for x in lista if x < pivot]
        iguales = [x for x in lista if x == pivot]
        mayores = [x for x in lista if x > pivot]

        return quick_sort(menores) + iguales + quick_sort(mayores)

def selection_sort():
def selection_sort(lista):
    for i in range (len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j]<lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

def esta_ordenada(lista):
    return all(lista[i]<= lista[i+1] for i in range(len(lista)-1))

def bogo_sort(lista):
    intentos = 0
    while not esta_ordenada(lista):
        random.shuffle(lista)
        intentos += 1
    print(f"Ordenada después de {intentos} intentos")
    return lista

while True:
    print('Opciones: ')
    print('1. Bubble Sort')
    print('2. Selection Sort')
    print('3. Quick Sort')
    print('4. Bogo Sort')
    print('5. Desordenar lista')
    print('6. Salir')

    option = input('Ingrese la opción deseada: ')

    match option:
        case '1':
            bubble_sort(lista)
            print(lista)

        case '2':
            pass

        case '3':
            lista = quick_sort(lista)
            print(lista)

        case '4':
            pass

        case '5':
            pass

        case '6':
            print('Saliendo del programa...')
            break

        case _:
            print('Opción incorrecta. Intente nuevamente.\n')