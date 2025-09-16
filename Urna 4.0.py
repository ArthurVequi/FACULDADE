candidatos=['Maria','Joao','Jose']
votos=[0,0,0]
count = 0
vencedor = []

while True:
    print(f'\nLista de Candidatos:\n1 - Maria: \n2 - João: \n3 - José:')
    escolha = input('Escreva seu voto: ')

    if escolha == '':
        break
    escolha = int(escolha)

    if escolha > len(candidatos) or escolha == 0:
        print('\nEscolha inválida. Tente novamente.')
        continue

    votos[escolha-1] += 1

print(f'\nMaria teve {votos[0]} votos \nJoao teve {votos[1]} votos \nJose teve {votos[2]} votos')

while True:
    maior_voto = 0
    if votos[count] > maior_voto:
        vencedor = candidatos[count]
        maior_voto = votos[count]
        print(f'\nO vencedor da eleição foi: {vencedor} com {maior_voto} votos')
        break
    count += 1