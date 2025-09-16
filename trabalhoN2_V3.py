import os
import random as R
mysL = []
erros = []

with open('palavras.txt', "r") as arquivo:
        palavras = arquivo.readlines()
        Tamanho = len(palavras)

def carregar_moedas():
    moedas = int(palavras[0].strip())
    return moedas

def salvar_saldo(saldo):
    palavras[0] = f'{saldo}\n'
    with open('palavras.txt', "w") as arquivo:
        arquivo.writelines(palavras)

def ocultarPalavra(n):
    if n == 1:
        mysL.append('_')
        return '_'
    mysL.append('_')
    return f'{ocultarPalavra(n-1)}_'

def desocultarPalavra(n):
    if n == 0:
        return mysL[n]
    return f'{desocultarPalavra(n-1)}{mysL[n]}'

def ocultarErros(n):
    if n == 0:
        return f'{erros[n]}'
    return f'{ocultarErros(n-1)},{erros[n]}'

def sortear_numeros():
    sorteados = []
    for i in range(3):
        numeros = R.randint(1, 9)
        sorteados.append(numeros)
    return sorteados

def sequencia(sorteio):
    lst_ordenada = sorted(sorteio)
    if lst_ordenada[1] == lst_ordenada[0]+1 and lst_ordenada[2] == lst_ordenada[1]+1:
        return lst_ordenada
    
def iguais(sorteio):
    if sorteio[0] == sorteio[1] == sorteio[2]:
        return sorteio[0]

def PalavraAleatoria():
    numeroAleatorio = R.randint(1,Tamanho - 1)
    palavra = palavras[R.randint(1,numeroAleatorio)]
    palavra = palavra.strip()
    return palavra

def Cassino_UCL():
    print('\n\033[35mBem Vindo ao Cassino UCL!')
    saldo = carregar_moedas()
    while saldo > 0:
        aposta = input((f'\n\033[mSeu saldo atual é de \033[31m{saldo}\033[m moedas!\nQuantas deseja apostar: '))

        if aposta == '' or aposta == '0':
            print('\nVolte Sempre!')
            break

        aposta = int(aposta)
        if aposta > saldo or aposta < 0:
            print('\nSaldo insuficiente ou Inválido!')
            continue

        else:
            sorteio = sortear_numeros()
        os.system('cls')
        print(f'\n[{sorteio[0]}] [{sorteio[1]}] [{sorteio[2]}]')

        if sequencia(sorteio):
                media = sum(sorteio)//3
                premio = (aposta*2)+media
                saldo += premio
                print('\n\033[92m PARABÉNS, VOCÊ ACERTOU UMA SEQUÊNCIA!')
            
        elif iguais(sorteio):
                aposta += sorteio[0]
                saldo += aposta
                print('\n\033[92m PARABÉNS, VOCÊ ACERTOU UMA COMBINAÇÃO!')
        else:
            saldo = saldo - aposta
            print('\n\033[31m Infelizmente nenhuma combinação foi obtida, mas não desista!')
        
        salvar_saldo(saldo)

        if saldo == 0:
            print('\n\033[mAparentemente você está sem saldo!')
            print('Fim de Jogo!')
            with open('palavras.txt', "r") as arquivo:
                linhas = arquivo.readlines()
                linhas[0] = '100\n'
            with open('palavras.txt', "w") as arquivo:
                arquivo.writelines(linhas)
    
    return 100

  
def Forca(Tipo):
    if Tipo == 'defina':
        palavra = input('Entre com a palavra que vai ser descoberta:').upper()
    else:
        palavra = PalavraAleatoria().upper()
    misterio = ocultarPalavra(len(palavra))
    ganhou = False
    tentativa = 10
    temLetra = False
    os.system('cls')
    erradas = ''
    while True:
        os.system('cls')
        misterio = desocultarPalavra(len(palavra)-1)
        print(f'JOGO DA FORCA\nNumero de Tentativas: {tentativa}\nLetras Erradas: {erradas}\nPalavra: {misterio}')
        escolha = input('Entre com uma Letra: ').upper()
        if len(escolha) != 1 and escolha != ' ':
            continue
        for i in range(len(palavra)):
            if escolha == palavra[i]:
                mysL[i] = escolha
                temLetra = True
        if temLetra == False and escolha not in erros:
            tentativa -= 1
            erros.append(escolha)
            erradas = ocultarErros(len(erros)-1)
        temLetra = False
        if tentativa == 0:
            break
        if '_' not in mysL:
            ganhou = True
            break
        
    os.system('cls')
    match ganhou:
        case False:
            print(f'JOGO DA FORCA\nVoce Perdeu!\nA palavra era "{palavra}"')
        case True:
            print(f'JOGO DA FORCA\nParabens você ganhou!\nA palavra era "{palavra}"')

def Jogo():
    while True:
        escolha = input('\033[mMENU\nEscolha o Jogo:\n1 - Jogo da Forca\n2 - Caça Níquel\n')
        if escolha != '1' and escolha != '2':
            continue
        print(escolha)
        if escolha == '1' or '2':
            break
    os.system('cls')
    match escolha:
        case '1':
            os.system('cls')
            escolha = input('MENU\nQual Forca?:\n1 - Defina a palavra\n2 - Palavra Aleatoria\n')
            match escolha:
                case '1':
                    Forca('defina')
                    Jogo()
                case '2':
                    Forca('aleatoria')
                    Jogo()
        case '2':
            Cassino_UCL()
            
            Jogo()
Jogo()