n = int(input('¿Cuántos números desea ingresar?: '))

lista = []

for i in range(n):
    num = int(input(f'{i+1}. Ingrese un número: '))
    lista.append(num)


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
            pass

        case '2':
            pass

        case '3':
            pass

        case '4':
            pass

        case '5':
            pass

        case '6':
            print('Saliendo del programa...')
            break

        case _:
            print('Opción incorrecta. Intente nuevamente.\n')