import numpy as np

def criar_matriz():
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Dgite o número de colunas: "))

    matriz = []
    print("Insira os elementos da matriz: ")
    for i in range(linhas):
        linha = list(map(float, input(f"Digite os elementos da linha {i + 1}, separados por espaço: ").split()))
        while len(linha) != colunas:
            print((f"A linha deve ter {colunas} elementos. Tente novamente."))
            linha = list(map(float, input(f"Digite os elementos da linha {i + 1}, separados por espaço:").split()))
        matriz.append(linha)

    return np.array(matriz)

