def imprimir_tablero(tablero):
    for i in range(9):
        for j in range(9):
            print(tablero[i][j], end=" ")
        print()

def encontrar_vacios(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return (i, j)
    return None

def validar(tablero, num, pos):
    # Validar fila
    for i in range(9):
        if tablero[pos[0]][i] == num and pos[1] != i:
            return False

    # Validar columna
    for i in range(9):
        if tablero[i][pos[1]] == num and pos[0] != i:
            return False

    # Validar subcuadrícula
    cuadrante_x = pos[1] // 3
    cuadrante_y = pos[0] // 3

    for i in range(cuadrante_y * 3, cuadrante_y * 3 + 3):
        for j in range(cuadrante_x * 3, cuadrante_x * 3 + 3):
            if tablero[i][j] == num and (i, j) != pos:
                return False

    return True

def resolver_sudoku(tablero):
    vacio = encontrar_vacios(tablero)
    if not vacio:
        return True
    else:
        fila, columna = vacio

    for num in range(1, 10):
        if validar(tablero, num, (fila, columna)):
            tablero[fila][columna] = num

            if resolver_sudoku(tablero):
                return True

            tablero[fila][columna] = 0

    return False

# Ejemplo de uso
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if resolver_sudoku(tablero):
    imprimir_tablero(tablero)
else:
    print("No se pudo resolver el Sudoku.")