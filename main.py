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

def operacao_elemento(matriz, operacao):
    valor = float(input("Digite o valor para realizar a operação: "))

    if operacao == "somar":
        return matriz + valor
    elif operacao == "subtrair":
        return matriz - valor
    elif operacao == "multiplicar":
        return matriz * valor
    elif operacao == "dividir":
        return matriz / valor
    else:
        print("Operação inválida.")
        return matriz
    
def operacao_soma_total(matriz, operacao):
    soma_total = matriz.sum()
    valor = float(input("Digite o valor para realizar a operação: "))

    if operacao == "somar":
        return soma_total + valor
    elif operacao == "subtrair":
        return soma_total - valor
    elif operacao == "multiplicar":
        return soma_total * valor
    elif operacao == "dividir":
        return soma_total / valor
    else:
        print("Operação inválida.")
        return soma_total
    
def menu():
    print("\nMenu de Operações: ")
    print("1. Criar uma matriz")
    print("2. Operações em cada elemento da matriz")
    print("3. Operações com a soma total da matriz")
    print("4. Exibir matriz")
    print("5; Sair")

def main():
    matriz = None

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            natriz = criar_matriz()
            print("Matriz criada com sucesso")

        elif opcao == "2":
            if matriz is None:
                print("Crie uma matriz primeiro. ")
            else:
                print("\nOperacões em cada elemento: ")
                print("a. Somar")
                print("b. Subtrair")
                print("c. Multiplicar")
                print("d. Dividir")
                oper = input("Escolha a operação (a/bc/d): ").strip().lower()

            



    
