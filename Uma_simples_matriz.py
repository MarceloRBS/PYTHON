print('\033[33mLEGENDA: [col, lin]\033[m\n')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spares = 0
for c in range(3):
    for l in range(3):
        matriz[c][l] = int(input(f'Digíte um valor para [{c + 1}, {l + 1}]: '))
        if matriz[c][l] % 2 == 0:
            spares += matriz[c][l]
print('- ' * 22)
for c in range(3):
    for l in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('- ' * 22)
print(f'* A soma dos valores pares: {spares}')
print(f'* A soma dos valores da terceira coluna: {sum(matriz[2])}')
print(f'* O maior valor da 2ª linha: {max([matriz[0][1], matriz[1][1], matriz[2][1]])}')
