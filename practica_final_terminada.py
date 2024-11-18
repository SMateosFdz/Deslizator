import re


# Comprueba a partir de la letra y el numero si es un bloque o varios
def comprobacion(letra, num):
    contador = 1
    i = 1

    if num == 0:
        while i < 4 and ord(matrix[letra][num]) == ord(matrix[letra][num + i]):
            contador += 1
            i += 1

    elif num == 1:
        if ord(matrix[letra][num]) == ord(matrix[letra][num - 1]):
            contador += 1

        while i < 4 and ord(matrix[letra][num]) == ord(matrix[letra][num + i]):
            contador += 1
            i += 1

    elif num == 2:
        while i < 4 and ord(matrix[letra][num]) == ord(matrix[letra][num + i]):
            contador += 1
            i += 1

        i = 1

        while i < 3 and ord(matrix[letra][num]) == ord(matrix[letra][num - i]):
            contador += 1
            i += 1

    elif num == 7:
        while i < 3 and ord(matrix[letra][num]) == ord(matrix[letra][num + i]):
            contador += 1
            i += 1

        i = 1

        while i < 4 and ord(matrix[letra][num]) == ord(matrix[letra][num - i]):
            contador += 1
            i += 1

    elif num == 8:
        if ord(matrix[letra][num]) == ord(matrix[letra][num + 1]):
            contador += 1

        while i < 4 and ord(matrix[letra][num]) == ord(matrix[letra][num - i]):
            contador += 1
            i += 1

    elif num == 9:
        while i < 4 and ord(matrix[letra][num]) == ord(matrix[letra][num - i]):
            contador += 1
            i += 1

    else:
        while i < 4 and ord(matrix[letra][num]) == ord(matrix[letra][num + i]):
            contador += 1
            i += 1

        i = 1

        while i < 4 and ord(matrix[letra][num]) == ord(matrix[letra][num - i]):
            contador += 1
            i += 1

    return contador


def movem(letra, num, mov):
    bloque = comprobacion(letra, num)
    print(bloque)

    if bloque == 1:
        if mov == '<':
            while matrix[letra][num - 1] == ' ':
                matrix[letra][num - 1] = matrix[letra][num]
                matrix[letra][num] = ' '
                if num > 1:
                    num -= 1

        elif mov == '>':
            while matrix[letra][num + 1] == ' ':
                matrix[letra][num + 1] = matrix[letra][num]
                matrix[letra][num] = ' '
                if num < len(matrix[letra]) - 2:
                    num += 1

    elif bloque == 2:
        if mov == '<':
            if matrix[letra][num - 1] == matrix[letra][num]:
                while matrix[letra][num - 2] == ' ':
                    matrix[letra][num - 2] = matrix[letra][num]
                    matrix[letra][num] = ' '
                    if num > 1:
                        num -= 1

            else:
                while matrix[letra][num - 1] == ' ':
                    matrix[letra][num - 1] = matrix[letra][num + 1]
                    matrix[letra][num + 1] = ' '
                    if num > 1:
                        num -= 1

        elif mov == '>':
            if matrix[letra][num + 1] == matrix[letra][num]:
                while matrix[letra][num + 2] == ' ':
                    matrix[letra][num + 2] = matrix[letra][num]
                    matrix[letra][num] = ' '
                    if num < len(matrix[letra]) - 3:
                        num += 1

            else:
                while matrix[letra][num + 1] == ' ':
                    matrix[letra][num + 1] = matrix[letra][num]
                    matrix[letra][num - 1] = ' '
                    if num < len(matrix[letra]) - 3:
                        num += 1

    elif bloque == 3:
        if mov == '<':
            if matrix[letra][num - 1] == matrix[letra][num]:
                if matrix[letra][num - 2] == matrix[letra][num]:
                    while matrix[letra][num - 3] == ' ':
                        matrix[letra][num - 3] = matrix[letra][num]
                        matrix[letra][num] = ' '
                        if num > 1:
                            num -= 1

                else:
                    while matrix[letra][num - 2] == ' ':
                        matrix[letra][num - 2] = matrix[letra][num]
                        matrix[letra][num + 1] = ' '
                        if num > 1:
                            num -= 1

            else:
                while matrix[letra][num - 1] == ' ':
                    matrix[letra][num - 1] = matrix[letra][num]
                    matrix[letra][num + 2] = ' '
                    if num > 1:
                        num -= 1

        elif mov == '>':
            if matrix[letra][num + 1] == matrix[letra][num]:
                if matrix[letra][num + 2] == matrix[letra][num]:
                    while matrix[letra][num + 3] == ' ':
                        matrix[letra][num + 3] = matrix[letra][num]
                        matrix[letra][num] = ' '
                        if num < len(matrix[letra]) - 4:
                            num += 1

                else:
                    while matrix[letra][num + 2] == ' ':
                        matrix[letra][num + 2] = matrix[letra][num]
                        matrix[letra][num - 1] = ' '
                        if num < len(matrix[letra]) - 4:
                            num += 1

            else:
                while matrix[letra][num + 1] == ' ':
                    matrix[letra][num + 1] = matrix[letra][num - 1]
                    matrix[letra][num - 2] = ' '
                    if num < len(matrix[letra]) - 4:
                        num += 1

    elif bloque == 4:
        if mov == '<':
            if matrix[letra][num - 1] == matrix[letra][num]:
                if matrix[letra][num - 2] == matrix[letra][num]:
                    if matrix[letra][num - 3] == matrix[letra][num]:

                        while matrix[letra][num - 4] == ' ':
                            matrix[letra][num - 4] = matrix[letra][num]
                            matrix[letra][num] = ' '
                            if num > 1:
                                num -= 1

                    else:
                        while matrix[letra][num - 3] == ' ':
                            matrix[letra][num - 3] = matrix[letra][num]
                            matrix[letra][num + 1] = ' '
                            if num > 1:
                                num -= 1

                else:
                    while matrix[letra][num - 2] == ' ':
                        matrix[letra][num - 2] = matrix[letra][num]
                        matrix[letra][num + 2] = ' '
                        if num > 1:
                            num -= 1

            else:
                while matrix[letra][num - 1] == ' ':
                    matrix[letra][num - 1] = matrix[letra][num + 1]
                    matrix[letra][num + 3] = ' '
                    if num > 1:
                        num -= 1

        elif mov == '>':
            if matrix[letra][num + 1] == matrix[letra][num]:
                if matrix[letra][num + 2] == matrix[letra][num]:
                    if matrix[letra][num + 3] == matrix[letra][num]:

                        while matrix[letra][num + 4] == ' ':
                            matrix[letra][num + 4] = matrix[letra][num]
                            matrix[letra][num] = ' '
                            if num < len(matrix[letra]) - 5:
                                num += 1

                    else:
                        while matrix[letra][num + 3] == ' ':
                            matrix[letra][num + 3] = matrix[letra][num]
                            matrix[letra][num - 1] = ' '
                            if num < len(matrix[letra]) - 5:
                                num += 1

                else:
                    while matrix[letra][num + 2] == ' ':
                        matrix[letra][num + 2] = matrix[letra][num]
                        matrix[letra][num - 2] = ' '
                        if num < len(matrix[letra]) - 5:
                            num += 1

            else:
                while matrix[letra][num + 1] == ' ':
                    matrix[letra][num + 1] = matrix[letra][num - 1]
                    matrix[letra][num - 3] = ' '
                    if num < len(matrix[letra]) - 5:
                        num += 1


def fall():
    i = 0
    j = 0
    while i < len(matrix) - 1:
        while j < len(matrix[i]):
            if matrix[i][j] != ' ':
                bloque = comprobacion(i, j)

                if bloque == 2:
                    if matrix[i + 1][j] == ' ' and matrix[i + 1][j + 1] == ' ':
                        matrix[i + 1][j] = matrix[i][j]
                        matrix[i + 1][j + 1] = matrix[i][j + 1]
                        matrix[i][j] = ' '
                        matrix[i][j + 1] = ' '
                    j += 2

                elif bloque == 3:
                    cont = 0
                    for x in range(0, 3):
                        if matrix[i + 1][j + x] == ' ':
                            cont += 1

                    if cont == 3:
                        for x in range(0, 3):
                            matrix[i + 1][j + x] = matrix[i][j + x]
                            matrix[i][j + x] = ' '

                    j += 3

                elif bloque == 4:
                    cont = 0
                    for x in range(0, 4):
                        if matrix[i + 1][j + x] == ' ':
                            cont += 1

                    if cont == 4:
                        for x in range(0, 4):
                            matrix[i + 1][j + x] = matrix[i][j + x]
                            matrix[i][j + x] = ' '

                    j += 4

                else:
                    if matrix[i + 1][j] == ' ':
                        matrix[i + 1][j] = matrix[i][j]
                        matrix[i][j] = ' '
                    j += 1

            else:
                j += 1

        j = 0
        i += 1


def table():
    numbers = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L'}

    i = 0
    j = 0
    while i < len(matrix):
        print('    +---+---+---+---+---+---+---+---+---+---+')
        print(numbers.get(i), end='   ')

        while j < len(matrix[i]):

            if matrix[i][j] != ' ':
                bloque = comprobacion(i, j)

                if bloque == 1:
                    if ord(matrix[i][j]) == 65 or ord(matrix[i][j]) == 97:
                        print('|$$$', end='')
                    elif ord(matrix[i][j]) == 66 or ord(matrix[i][j]) == 98:
                        print('|###', end='')
                    j += 1

                elif bloque == 2:
                    if ord(matrix[i][j]) == 65 or ord(matrix[i][j]) == 97:
                        print('|$$$$$$$', end='')
                    elif ord(matrix[i][j]) == 66 or ord(matrix[i][j]) == 98:
                        print('|#######', end='')
                    j += 2

                elif bloque == 3:
                    if ord(matrix[i][j]) == 65 or ord(matrix[i][j]) == 97:
                        print('|$$$$$$$$$$$', end='')
                    elif ord(matrix[i][j]) == 66 or ord(matrix[i][j]) == 98:
                        print('|###########', end='')
                    j += 3

                elif bloque == 4:
                    if ord(matrix[i][j]) == 65 or ord(matrix[i][j]) == 97:
                        print('|$$$$$$$$$$$$$$$', end='')
                    elif ord(matrix[i][j]) == 66 or ord(matrix[i][j]) == 98:
                        print('|###############', end='')
                    j += 4
            else:
                print('|   ', end='')
                j += 1

        j = 0
        i += 1
        print('|')

    print('    +---+---+---+---+---+---+---+---+---+---+')
    print('      ', end='')

    for x in range(10):
        print(x, end='   ')

    print()


def clean():
    for i in range(len(matrix)):
        contador = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] != ' ':
                contador += 1
            if contador == len(matrix[i]):
                for x in range(len(matrix[i])):
                    matrix[i][x] = ' '

    for i in range(12):
        fall()


patron = re.compile('[A-L][0-9][<>]')
matrix = []
letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11}
jugar = True
fichero = open('prueba.txt', 'r')

for i in range(12):
    matrix.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])

print("Bienvenido al videojuego")
while jugar:
    linea = fichero.readline()
    if linea == '':
        fichero.close()
        fichero = open('prueba.txt', 'r')
        linea = fichero.readline()
    j = 0
    for i in range(len(matrix[0])):
        matrix[0][i] = linea[j]
        j += 1

    print()
    table()

    print("Escriba la pieza que quiere mover o --- o FIN")
    cadena = input()

    while not patron.match(cadena) and cadena != '---' and cadena != 'FIN':
        print("Escriba la pieza que quiere mover o --- o FIN")
        cadena = input()

    if cadena == '---':
        print("No se mueve ninguna pieza")

    elif cadena == 'FIN':
        jugar = False

    else:
        letra = letters.get(cadena[0])
        num = int(cadena[1])

        if matrix[letra][num] == ' ':
            print("La casilla esta vacia y no se puede mover ninguna pieza")

        elif num == 9 and cadena[2] == '>':
            print("No se puede mover la pieza en esa direccion")

        elif num == 0 and cadena[2] == '<':
            print("No se puede mover la pieza en esa direccion")

        else:
            movem(letra, num, cadena[2])

    if jugar:
        fall()
        table()
        clean()

    for i in range(len(matrix[0])):
        if matrix[0][i] != ' ':
            jugar = False

print("Fin de la partida")
