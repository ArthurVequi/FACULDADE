#Aluno: Arthur Vequi Timoteo
#Exercícios sem-6

print('EXERCÍCIOS SEM-6')
exer = int(input('Digite o exercicio que deseja ver: '))

# 1) Escreva um algoritmo que leia dois números e exiba o maior deles.

if exer == 1:
    print('Exercicio 1')
    n1 = int(input('\nDigite um número: '))
    n2 = int(input('Digite um número: '))

    if n1>n2:
        print('Os números escolhidos foram',n1,'e',n2,'destes, o maior é',n1)
    else:
       print('Os números escolhidos foram',n1,'e',n2,'destes, o maior é',n2)
    print('\nAluno: Arthur Vequi Timoteo')

# # 2) Escreva um algoritmo para ler um número inteiro e retornar se ele é maior, igual ou menor que zero.

if exer == 2:
    print('Exercicio 2')
    num1 = int(input('\nDiga um numero:'))
    zero = int(0)
    if num1 > zero:
         print('Maior que zero')
    if num1 == zero:
        print('Igual a zero')
    else:
        print('Menor que zero')
    print('\nAluno: Arthur Vequi Timoteo')

# # 3) Faça um algoritmo que leia um número inteiro e retorne se o número é par o ímpar.

if exer == 3:
    print('Exercicio 3')
    num = int(input("\nDigite um número inteiro: "))

    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")
    print('\nAluno: Arthur Vequi Timoteo')

# 4) Faça um algoritmo que receba um número e mostre uma mensagem caso este número seja maior que
# 80, menor que 25 ou igual a 40.

if exer == 4:
    print('Exercicio 4')
    idade = int(input('\nDigite sua idade: '))

    if idade >=80:
        print('Aposentado')
    elif 40<=idade<80 :
        print('Ancião')
    elif 25<=idade<39:
        print('ta novo, trabalhe')
    else:
        print('Compre um vectra 97')
    print('\nAluno: Arthur Vequi Timoteo')

# 5) Elabore um algoritmo para testar se uma senha digita é igual a “batata frita”. Se a senha estiver correta
# escreva “Acesso permitido”, do contrário emita a mensagem “Você não tem acesso ao sistema”.

if exer == 5:
    print('Exercicio 5')
    input('\nDigite seu usuario: ')
    senha = input('Digite sua Senha: ')
    if senha =='batata frita':
        print('\nAcesso permitido')
    else:
        print('\nVocê não tem acesso ao sistema')
    print('\nAluno: Arthur Vequi Timoteo')

# 6) escreva um algoritimo que receba tres valores e coloque em ordem crescente 

if exer == 6:
    print('Exercicio 6')
    n1  = int(input('\nDigite um numero: '))
    n2 = int(input('Digite mais um numero: '))
    n3 = int(input('Digite pela ultima vez um numero: '))
    numeros =  [n1, n2, n3]
    numeros.sort()
    print('A ordem dos numoros sao:',numeros)
    print('\nAluno: Arthur Vequi Timoteo')

# 7) Escreva um algoritimo para uma empresa que decida dar em reajuste a seus funcionarios de acordo com os criterios 
#1 - 50% menos de 3 salarios
#2 - 20%  entre 3 e 10  salarios 
#3 - 15% para aqueles que ganham acima de dez até vinte salários mínimos;
#4 - 10% para os demais funcionários.
# Obs: Leia o valor do salário mínimo e imprima os valores dos reajustes obedecendo os critérios

if exer == 7:
    print('Exercicio 7')
    salario  = float(input('\nQual e o valor do seu salario: '))
    valor = salario//1518
    print('Voce recebe aproximadamente', valor,'salarios minimos')
    A1 =  salario * 1.5
    A2 =  salario * 1.2
    A3 =  valor * 1.15
    A4 =  salario * 1.1
    if valor <3:
        print('\nSeu aumento e de 50%')
        print('logo seu salario atual e de :', round(A1))

    if 3<= valor <=10:
        print('\nSeu aumento e de 20%')
        print('Logo seu salario atual e de :', round(A2))

    if 10< valor <=20:
        print('\nSeu aumento e de 15%')
        print('Logo seu salario atual e de :', round(A3))

    if valor >20:
        print('\nSeu aumento e de 10%')
        print('Logo seu salario atual e de :', round(A4))
    print('\nAluno: Arthur Vequi Timoteo')

# 8) Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for
# menor que R$ 20,00; caso contrário, o lucro será de 30%. Elabore um algoritmo que leia o valor do
# produto e imprima o valor de venda para o produto.

if exer == 8:
    print('Exercicio 8')
    custo = int(input('\nQual é o custo do produto: '))
    venda1 = custo * 1.45
    venda2 = custo * 1.20

    if custo < 20:
        lucro1 = venda1 - custo
        print('\nO valor do lucro é :',round(lucro1,2))
        print('O valor de venda do produto e de :',round(venda1,2))
    else:
        lucro2 = venda2 - custo
        print('\nO valor do lucro sera de:',round(lucro2,2))
        print('O valor de venda do produto e de :',round(venda2,2))
    print('\nAluno: Arthur Vequi Timoteo')

# 9) A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos com desconto.
# Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente. O
# desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%.

if exer == 9:
    print('Exercicio 9')
    ValorCarro = float(input('\nQual e o valor inicial do veículo? '))
    Ano = int(input('Qual e o ano do veículo? '))

    Desconto1 = ValorCarro * 0.12
    Desconto2 = ValorCarro * 0.07
    vtotal1 = ValorCarro - Desconto1
    vtotal2 = ValorCarro - Desconto2

    if Ano <=2000:
        print('\nSeu desconto e de :',round(Desconto1,2))
        print('O valor do seu veiculo ja com o desvonto e de:',round(vtotal1,2))
    else:
        print('\nSeu desconto e de :',round(Desconto2,2))
        print('O valor do seu veiculo ja com o desvonto e de:',round(vtotal2,2))
    print('\nAluno: Arthur Vequi Timoteo')

#10) Faça um algoritmo que receba um número e diga se este número está no intervalo entre 100 e 200.

if exer == 10:
    print('Exercicio 10')
    numero = int(input('\nDigite um número dentro do intervalo - 100 à 200: '))

    if 100<=numero<=200:
        print('O valor está dentro do intervalo')
    else:
        print('O valor não está dentro do intervalo')
    print('\nAluno: Arthur Vequi Timoteo')

# 11) O Botafogo Futebol Clube deseja aumentar o salário de seus jogadores. O reajuste deve obedecer a
# seguinte tabela:

# SALÁRIO ATUAL / (R$) AUMENTO
# 0,00 a 5.000,00 / 20%
# 5.000,01 a 15.000,00 / 10%
# acima de 15.000,00 / 0%

# Escreva um algoritmo que leia o nome e o salário atual de um jogador, e exiba o nome, o salário atual e o
# salário reajustado.

if exer == 11:
    print('Exercicio 11')
    nome = input('\nDigite seu nome: ')
    salario = float(input('Digite seu salario: '))
    aum1 = salario+(salario*0.20)
    aum2 = salario+(salario*0.10)
    aum3 = salario+(salario*0.05)

    if salario <= 5.000:
        print('\nO salário atual é',salario)
        print('O novo salário do',nome,'é',round(aum1,2))
    elif 5.000<=salario<=15.000:
        print('\nO salário atual é',salario)
        print('O novo salário do',nome,'é',round(aum2,2))
    else:
        print('\nO salário atual é',salario)
        print('O novo salário do',nome,'é',round(aum3,2))
    print('\nAluno: Arthur Vequi Timoteo')

# 12) Faça um algoritmo para calcular a conta final de um hóspede de um hotel fictício,
# considerando que:
# ▪ Serão lidos o nome do hóspede, o tipo do apartamento utilizado (A, B, C ou D), o número de diárias
# utilizadas pelo hóspede e o valor do consumo interno do hóspede;
# ▪ O valor da diária é determinado pela seguinte tabela:

# TIPO DO APTO / VALOR DA DIÁRIA (R$)
#      A    /   150,00
#      B    /   100,00
#      C    /   75,00
#      D    /   50,00

# ▪ O valor total das diárias é calculado pela multiplicação do número de diárias utilizadas pelo valor da
# diária;
# ▪ O subtotal é calculado pela soma do valor total das diárias e o valor do consumo interno;
# ▪ O valor da taxa de serviço equivale a 10% do subtotal;
# ▪ A total geral resulta da soma do subtotal com a taxa de serviço.
# ▪ Escreva a conta final contendo: o nome do hóspede, o tipo do apartamento, o número de diárias
# utilizadas, o valor unitário da diária, o valor total das diárias, o valor do consumo interno, o subtotal, o
# valor da taxa de serviço e o total geral.

if exer == 12:
    print('Exercicio 12')
    hospede = input('\nDigite seu nome: ')
    apto = input('Digite o tipo de apartamento (A, B, C ou D): ')
    diarias = int(input('Digite o numero de diarias utilizadas: '))
    consumo = float(input('Digite o valor do consumo interno: '))

    if apto == 'A':
        vdiaria = 150.00
    elif apto == 'B':
        vdiaria = 100.00
    elif apto == 'C':
        vdiaria = 75.00
    else:
        vdiaria = 50.00

    tdiarias = diarias * vdiaria
    subtotal = tdiarias + consumo
    tserviço = subtotal * 0.10
    total = subtotal + tserviço

    print('\nConta final:')
    print('\nNome do hospede:', hospede)
    print('Tipo de apartamento:', apto)
    print('Numero de diarias utilizadas:', diarias)
    print('Foram utilizadas',diarias,'diarias,cada uma custando R$',vdiaria,'reais')
    print('Valor do consumo interno:', consumo)
    print('O subtotal + taxa de servico é:',subtotal)
    print('Taxa de servico:',tserviço)
    print('Total geral:',total)
    print('\nAluno: Arthur Vequi Timoteo')

if exer >12:
    print('\nExercicio invalido')
    print('\nAluno: Arthur Vequi Timoteo')