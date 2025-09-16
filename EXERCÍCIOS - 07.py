#Exercício 1
clientes = []
count = 0
while True:
    escolha = int(input('\n1-Cadastar\n2-Alterar\n3-Excluir\n4-Listar\n5-Sair\nEscolha a opção: '))
    if escolha <6:
        match escolha:
            case 1:
                nomes = input('\nDigite o nome do cliente: ').capitalize()
                clientes.append(nomes)
            
            case 2:
                print(clientes)
                alterar = input('Qual cliente gostaria de atualizar: ').capitalize()
                if alterar in clientes:
                    novo_cliente = input('Qual o novo cliente: ').capitalize()
                else:
                    print('Cliente não encontrado!')
                    continue

                while alterar in clientes:
                    if clientes[count] == alterar:
                        clientes[count] = novo_cliente
                    else:
                        count += 1

            case 3:
                print(clientes)
                excluir = input('Qual cliente deseja excluir: ').capitalize()
                if excluir in clientes:
                    novo_cliente = input('Qual o novo cliente: ').capitalize()
                else:
                    print('Cliente não encontrado!')
                    continue
                    
                while excluir in clientes:
                    if clientes[count] == excluir:
                        clientes.remove(clientes[count])
                    else:
                        count += 1
            case 4:
                print(clientes)

            case 5:
                break
    if escolha >5 or escolha == '':
        print('\nEscolha Invalida!')
        continue

# EXERCÍCIO 2

perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? "
]
classificacao = []
positivas = 0

for pergunta in perguntas:
    resposta = input(pergunta).lower()
    if resposta == "sim":
        positivas += 1
    elif resposta == 'nao':
        continue

if positivas == 2:
    classificacao.append("Suspeita")
elif 3 <= positivas <= 4:
    classificacao.append("Cúmplice")
elif positivas == 5:
    classificacao.append("Assassino")
else:
    classificacao.append("Inocente")

print("\nClassificação:", classificacao)

# EXERCÍCIO 3
qualificados = 0
nao_qualificados = 0
soma_tempo = 0
total_funcionarios = 0

while True:
    id = input('Qual sua matrícula: ')
    if id == '':
        break

    nascimento = int(input('Data de nascimento (ano): '))
    ingresso = int(input('Ano que ingressou: '))
    idade = 2025 - nascimento
    trabalhado = 2025 - ingresso

    soma_tempo += trabalhado
    total_funcionarios += 1

    if idade > 65:
        print('Requerer aposentadoria\n')
        qualificados += 1
    elif trabalhado >= 30:
        print('Requerer aposentadoria\n')
        qualificados += 1
    elif idade >= 60 and trabalhado >= 25:
        print('Requerer aposentadoria\n')
        qualificados += 1
    else:
        print('Não requer aposentadoria\n')
        nao_qualificados += 1

if total_funcionarios > 0:
    media_tempo = soma_tempo / total_funcionarios
    print(f"\nMédia de tempo de serviço de todos os funcionários: {media_tempo:.2f} anos")

if qualificados > 0:
    media_qualificados = soma_tempo / qualificados
    print(f"Média de tempo de serviço dos qualificados: {media_qualificados:.2f} anos")
else:
    print("Nenhum funcionário qualificado para aposentadoria.")

# EXERCÍCIO 4

alunos = []
notas = []
aprovados = []
reprovados = []

while True:
    nome = input('\nDigite o nome do aluno: ')
    alunos.append(nome)
    if nome == '':
        break

    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    exame = float(input('Digite a nota do exame semestral: '))
    print('Notas Salvas!')

    media = (n1*0.2) + (n2*0.35) + (exame*0.45)
    notas.append(media)

    if media >= 5:
        aprovados.append(nome)
    else:
        reprovados.append(nome)

maior_media = max(notas)
menor_media = min(notas)
total_aprovados = len(aprovados)
total_reprovados = len(reprovados)    
media_turma = sum(notas) / len(notas)

print(f'Aluno com maior média: {alunos[notas.index(maior_media)]} com {maior_media}')
print(f'Aluno com menor média: {alunos[notas.index(menor_media)]} com {menor_media}')    
print(f'\nTotal de alunos aprovados: {total_aprovados}')
print(f'Total de alunos reprovados: {total_reprovados}')
print(f'\nMédia geral da turma: {media_turma}')