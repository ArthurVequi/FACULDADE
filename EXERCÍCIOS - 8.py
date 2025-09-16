# EXERCÍCIO 1

def menor(n,m):
    if n <= m:
        return n
    else:
         return m 
print(menor(6,5))

# EXERCÍCIO 2

def numero(n):
    if n > 0:
        print('Positivo')
    else:
        print('Negativo')
numero(-6)

# EXERCÍCIO 3

def absol(n):
    if n > 0:
        return n
    else:
        n = n * -1
        return n
print(absol(-9))

# EXERCÍCIO 4

def ano(n):
    if n % 4 == 0:
        return True
    else:
        return False
print(ano(2024))

# EXERCÍCIO 5

def soma(a,b,limite):
    if a + b > limite:
        return True
    else:
        return False
print(soma(1,2,3))

# EXERCÍCIO 6

def numero(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
numero(5)

# EXERCÍCIO 7

lista = [1,2,3]
def maior(limite,lista):
    for i in range(len(lista)):
        if lista[i] > limite:
            return i
    return -1

print(maior(3,lista))

# EXERCÍCIO 8

n = int(input('Digite um número inteiro: '))
def binario(n):
    n = bin(n)
    return n
print(binario(n))
# Pesquisei no google como transformar para binario e descobri a função 'bin()' e a 'hex()'

# EXERCÍCIO 9

n = int(input('Digite um número inteiro: '))
def BinHex(n):
    escolha = int(input('\nDigite 1 para Binário;\nDigite 2 para Hexadecimal;\n Escolha: '))
    if escolha == 1:
        n = bin(n)
        return n
    else:
        n = hex(n)
        return n
print(BinHex(n))

# EXERCÍCIO 10

import math

def bhaskara(a,b,c):
    delta = b**2-4*a*c
    x1 = -b+math.sqrt(delta)/2*a
    x2 = -b-math.sqrt(delta)/2*a

    if a == 0:
        print('Não é uma equação do segundo grau.')
    elif delta < 0:
        print('Não existem raízes reais.')
    elif delta == 0:
        print(f"Raiz única: x = {x1}")
    elif delta > 0:
        print(f"Duas raízes reais: x1 = {x1:.2}, x2 = {x2:.2}")
bhaskara(1,6,4)

# EXERCÍCIO 11


def cadastrar_candidatos(candidatos):
    while True:
        opcao = input("1 - Cadastrar\n2 - Excluir\n3 - Listar\nEscolha a Opção: ")

        if opcao == "1":

            nome = input("Digite o nome do candidato: ")
            candidatos.append(nome)

        elif opcao == "2":

            nome = input("Digite o nome do candidato para excluir: ")
            if nome in candidatos:
                candidatos.remove(nome)

        elif opcao == "3":

            print("Lista de Candidatos:")
            for i, candidato in enumerate(candidatos, start=1):
                print(f"{i}: {candidato}")

def iniciar_votacao(candidatos):

    if len(candidatos) < 2:
        print("É necessário ter ao menos 2 candidatos cadastrados para iniciar a votação!")
        return
    votos = [0] * len(candidatos)

    while True:
        print("Lista de Candidatos:")
        for i, candidato in enumerate(candidatos, start=1):
            print(f"{i}: {candidato}")
        escolha = input("Escolha seu Candidato: ")

        if escolha == "":
            print("Votação encerrada!")
            break
        
        try:
            escolha = int(escolha)
            if escolha < 1 or escolha > len(candidatos):
                print("Opção inválida!")
            else:
                votos[escolha - 1] += 1
        except ValueError:
            print("Opção inválida!")
    print("Resultados da Votação:")
    for i, (candidato, voto) in enumerate(zip(candidatos, votos), start=1):
        print(f"{i}: {candidato} -> {voto}")
    vencedor = candidatos[votos.index(max(votos))]
    print(f"Vencedor: {vencedor} com {max(votos)} votos")

def main():
    candidatos = []
    while True:
        print("1 - Cadastrar Candidatos")
        print("2 - Iniciar Votação")
        opcao = input("Escolha a Opção: ")
        if opcao == "1":
            cadastrar_candidatos(candidatos)
        elif opcao == "2":
            iniciar_votacao(candidatos)
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
