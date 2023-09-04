"""
Nesta seção irei iniciar a sequencia interminalvel de exercicios de funções S.O.S

Exercicio 1 - Faça uma função que retorne o dobro de um inteiro

def dobro(num):
    return num * 2

Exercicio 2 - Faça uma função que receba a data atual(dia, mes e ano) e exiba na tela o formto por
extenso

def data_estenso(info):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
             'Outubro', 'Novembro', 'Dezembro']

    carac = './-'
    for i in range(3):
        info = info.replace(carac[i], '')

    if int(info[2:4]) > 12:
        print('o formato da data é invalido')
        return 0

    print(f'A data informada foi dia {info[0:2]} no mês de {meses[int(info[2:4])-1]} no ano de {info[4:9]}')


data = input('Digite uma data no formato dd/mm/aaaa ou dd-mm-aa ou ddmmaaaa: ')

data_estenso(data)


Exercicio 3
Faça uma função prar verificar se o número é positivo ou negativo. Sendo que o retorno será 1 se o postivo,
-1 se negativo e 0 se for igual a zero

def zero(numero=0):
    if numero == 0:
        return 0
    elif numero >= 1:
        return 1
    return -1


print(zero(numero=10), zero(-59), zero())


Exercicio 4:
Faça uma funcao para verificar se um número é um quadrado perfeito


def quadrado_perfeito(num):
    numero = num ** 0.5
    if numero == int(numero):
        return print('É um quadrado perfeito')
    return print('Não é um quadrado perfeito')


quadrado_perfeito(10)
quadrado_perfeito(4)
quadrado_perfeito(9)


Exercicio 5:
Faça uma função e um programa de teste para o cálculo do volume de uma esfera. Sendo que o raio é passado por parametro


def volume_esfera(raio):
    volume = 4/3 * 3.141592 * raio ** 3
    print(volume.__round__(2))


volume_esfera(5)
volume_esfera(10)


Exercicio 6:
Faça uma função que receba 3 números interios como parametros, representando horas, minutos e segundos, e os converta
em segundos


def t_segundos(hora, minuto, segundo):
    print(f'O total de segundo é {(hora*3600 + minuto*60 + segundo)}')


tempo = {'hora': 0, 'minuto': 0, 'segundo': 0}

print('Digite hora, minutos e segundos conforme abaixo')
for c, v in tempo.items():
    tempo[c] = int(input(f'Digite a {c}: '))

t_segundos(**tempo)


Exercicio 7, já feito em lista anterior, não muda nada além de colocar dentro de uma função


Exercicio 8:
Calcule a hipotenusa onde os parametros são a e b.


def hipotenusa(a, b):
    return print(f'A hipotenusa é {(a ** 2 + b ** 2) ** 0.5}')


lista = [[4, 5], [1, 3], [5, 5]]

hipotenusa(*lista[0])
hipotenusa(*lista[1])
hipotenusa(*lista[2])


Exercicio 9 não vou fazer, repeticao do mesmo


Exercicio 10:
Faça uma função que recaba dois números e retorne qual deles é maior

def maior_num(a, b):
    if a > b:
        return print('O primeiro numero é maior')
    elif a == b:
        return print('Os numero são iguais')
    return print('O segundo numero é maior')


lista = [[1, 1], [2, 4], [4, 2]]

maior_num(*lista[0])
maior_num(*lista[1])
maior_num(*lista[2])


Exercicio 11:
Elebora uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra for A, a função deverá
calcular a média aritimética das notas do aluno, se for P, deverá calcular a média ponderada, com pesos 5,3 e 2

def media(nota1, nota2, nota3, letra):
    if letra == 'a':
        return print(f'A media aritimetica do aluno foi {(nota1 + nota2 + nota3)/3}')
    elif letra == 'p':
        return print(f'A media ponderada do aluno foi {(nota1*5 + nota2*3 + nota3*2) / 10}')
    print('Letra selecionada invalida, tente novamente.')

media(5, 10, 10, 'p')


Exercicio 12:
Escreva uma função que receba um número inteiro maior do que zero e retorne a soma de todos os algarimoz.

def soma_numerica(num):
    soma = 0
    if num > 0:
        for a in str(num):
            soma += int(a)
        return print(f'A soma dos algarismos é {soma}')
    return print('O numero é menor ou igual a zero')


soma_numerica(555)
soma_numerica(100)
soma_numerica(0)
soma_numerica(-199)


Exercicio 13 não vou fazer, repeticao de calculadores já feitas anteriormente


Exercicio 14:
Faça uma função que receba em Km e a quantidade de listros de gasolina consumidos por um carro, calcule o consumo em
Km/l e escreva de acordo com a tabela abaixo
x > 8 - Venda o carro
8 < x < 11 - Economico
x > 12 - Super Economico


def km_l(km, litro):
    consumo = km/litro
    if consumo < 8:
        print('Venda o carro')
    elif consumo > 12:
        print('Super Economico')
    else:
        print('Economico')


km_l(10, 1)
km_l(100, 2)
km_l(5, 2)


Exercicio 15:
Crie um programa que receba 3 valores (obrigatóriamente maiores que zero) , representando as medidas dos 3 lados de um
triangulo .
(a) determinar se os lados formam um triângulo, sabendo que:
# O comprimento de cada lado de um triangulo é
menor do que a soma dos outros dois lados
(b)Determinar e mostrar o tipo de triangulo, caso as medidas#  formem um triângulo. Sabendo que:
# Chama-se equilátero o triangulo que tem 3 lados iguais
# Isósceles o triangulo que tem o comprimento de dois lados iguais
# Recebe o nome de escaleno o triangulo que tem 3 lados diferenttes


def info_triangulo(a, b, c):
    if ((a < (b + c)) and (b < (b + c)) and (c < (b + a))) is False:
        return print('Não é um triangulo.')
    elif a == b == c:
        print('É um triangulo equilatero.')
    elif (a == b) or (a == c) or (b == c):
        print('É um triangulo isoceles.')
    else:
        print('É um triangulo escaleno.')


info_triangulo(100, 10, 9)
info_triangulo(20, 20, 5)
info_triangulo(10, 9, 8)
info_triangulo(5, 5, 5)


Exercicio 16 é muito idiota, é só multiplicação de string.


Exercicio 17:
Faça uma função que receba dois números inteiros positivos por parâmetro e retorne a soma dos N números interios exis-
tentes entre eles.


def soma_num(num1, num2):
    soma = 0
    for i in range(num1, num2+1):
        soma += i

    print(soma)


def soma_num2(*args):
    soma = 0
    for i in range(min(args), max(args)+1):
        soma += i
    print(soma)


soma_num(1, 5)
soma_num2(5, 1)


Exercicio 18:
Faça uma função que receba por parâmetro dois valores X e Z. Calcule e retorne o resultado de X^Z para o programa
printcipal.

def exponencial(x, z):
    return x ** z


print(exponencial(2, 2))
print(exponencial(3, 2))
print(exponencial(3, 3))


Exercicio 19:
Faça uma função que retorne o maior fator primo de um número
# depois de revisar ficou um pouco confuso, mas funciona

def fator_primo(fator):
    primo = 1
    ate_um = fator

    while ate_um != 1:
        contador = 0
        while contador != 2:
            contador = 0
            for i in range(1, (primo + 1)):
                if (primo % i) == 0:
                    contador += 1
            if contador == 2:
                primo = i
            else:
                primo += 1

        if (ate_um/primo) == int(ate_um/primo):
            ate_um = ate_um/primo
        else:
            primo += 1

    return print(primo)


fator_primo(100)


Exercicio 20:
Faça um algoritimo que receba um número inteiro postivo n e calcule o seu fatorial n!

def fatorial(num):

    if num == 1:
        return 1
    else:
        return num * fatorial(num-1)


print(fatorial(5))


def fatorial2(num, fat=1):
    for i in range(1, num+1):
        fat *= i
    return fat

def fatorial(num):

    if num > 1:
        return num * fatorial(num-1)
    return 1

print(fatorial(5))


Exercicio 21:
Escreva uma função para determinar a quantidade de números primos abaixo de N

def b_primo(num):
    primos = []
    for i in range(num):
        contador = 0
        for b in range(1, i+1):
            if (i % b) == 0:
                contador += 1
        if contador == 2:
            primos.append(i)
    return primos


print(b_primo(50))

Exercicio 22:
Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas com pontos de exclamação,
conforme ex:

!
!!
!!!

def exclamacao(num):

    for i in range(1, num+1):
        print('!'*i)


exclamacao(10)


Exercicio 23:
Escreva uma função que gera um triangulo lateral de altura 2*n-1 e n largura


def triangulo_lateral(num):
    antes_do_meio = int((num*2)/2)

    for i in range(1, antes_do_meio+1):
        print('*'*i)
    for i in range((antes_do_meio-1), 0, -1):
        print('*'*i)


triangulo_lateral(4)

Solução do coloque que eu adaptei:

def triangulo_lateral(num):

    tri1 = [[print('*' * i)] for i in range(1, num+1)]
    tri2 = [[print('*' * i)] for i in range(num-1, 0, -1)]

triangulo_lateral(4)


Exercicio 24:
Escreva uma função que gere um triangulo de altura e lados n e base 2*n-1. Por exemplo
  *
 ***
*****

def triangulo(num):

    for i in range(1, num+1):
        print(' ' * (num - i), '*' * (2*i - 1))

triangulo(10)


Exercicio 25 não vou fazer, é apenas uma divisão de duas somas


Exercicio 26:
Faça um algoritimo que receba um número inteiro positivo n e calcule o somatório de 1 até n

def somatorio(num):
    if num > 1:
        return num + somatorio(num-1)
    return 1


print(somatorio(3))

Exercicios 27 a 30 não vou fazer, tem de estudar angulos para isso.


Exercicio 31:
Faça uma função para calcula o númeor neperiano usando uma série.

def fatorial(num):

    if num > 1:
        return num * fatorial(num-1)
    return 1


def log(num):
    if num > 0:
        return (1/fatorial(num)) + log(num-1)
    return 0


def log2(num):
    soma = 0
    for i in range(1, num+1):
        soma += (1/fatorial(i))
    return soma


print(log(3))
print(log2(3))


Exercicio 32:
Faça uma função chama simplifica que recebe como parametro o umerador e o denominador de uma fração. Esta funçao deve
simplificar a fração recebida dividando o numerador e denominador pelo maior fator possível.


def simplificador(num1, num2):
    lista = [num1, num2]

    for i in range(min(lista), 0, -1):
        i = i
        if (lista[0] % i == 0) and (lista[1] % i == 0):
            lista = [lista[0] / i, lista[1] / i]
    return lista


print(simplificador(50, 10))


print(simplificador(50, 10))


Exercicio 33:
Faça uma função que receba um número N e retorne a soma dos algarismos de N!

def fat(num):
    if num < 2:
        return 1
    else:
        return num * fat(num-1)


def soma(num):
    x = sum((int(x) for x in str(fat(num))))
    return x


print(soma(4))


Exercicio 34:
Faça uma função não recursiva para fatorial duplde de N. É fatorial de numero impar..

def fat_duplo(impar):
    impares = [numero for numero in range(1, impar+1) if numero % 2 != 0]
    multi = 1
    for i in impares:
        multi *= i
    return multi


print(fat_duplo(5))


Exercicio 35:
Faça uma função não recursiva que receba um número inteiro positivo n e retorne o fatorial quadruplo.
(2n)! / n!

def fatorial(num, fat=1):
    for i in range(1, num+1):
        fat *= i
    return fat


def fatorial_quadruplo(num):
    if num < 0:
        return print('Numero deve ser maior que zero')
    return print((fatorial(2*num)/fatorial(num)))


fatorial_quadruplo(5)


Exercicio 36 é um fatorial com uma multiplicação do fatorial de cara numero, igual a logica dos exercicios anteriores.


Exercicio 37:
Faça um função que receba um inteiro postivio n e retorne o hiperfatorial desse número.

def hiperfatorail(n):
    if n < 0:
        return print('Numero deve ser maior que zero')
    soma = 1
    for i in range(1, n+1):
        soma *= (i**i)
    return print(soma)


hiperfatorail(5)


Exercicio 38:
Faça uma função que receba um inteiro positivo n e retorne o fatorial exponencial desse número.

def fatorial_exp(num):
    if num < 0:
        return print('Numero deve ser maior que zero')
    x = 0
    for i in range(1, num+1):
        if i == 0:
            x = (i+1) ** i
        else:
            y = i ** x
            x = y

    return print(x)


fatorial_exp(4)


Exercicio 39:


def troca(*args):
    return [args[1], args[0]]


print(troca(1, 2))

Exercicio 40:

def quant_pares(vetor):
    pares = [par for par in vetor if par % 2 ==0]
    return sum(pares)


vetor = [x for x in range(1, 100)]
print(quant_pares(vetor))


Exercicio 41:

def maior_numero(vetor):
    maior = 0
    for i in vetor:
        if maior < i:
            maior = i
    return maior


lista = [x for x in range(1, 11)]   # Sempre esqueco que o range(x, y) o y é não incluso, ultmo num é y-1
print(maior_numero(lista))


Exercicio 42:

def media(vetor):
    med = 0
    for i in len(vetor):
        med += vetor
    return med/len(vetor)


lista = [x for x in range(1, 11)]

Exercicio 43 meio sem noção.


Exercicio 44:


def par_e_impar(vetor, a=[], b=[]):
    c =[a.append(numero) if (numero % 2 == 0) else b.append(numero) for numero in vetor]
    return a, b


lista = [x for x in range(1, 30)]
par, impar = par_e_impar(lista)
print(par)
print(impar)

Exercicio 45:

def desvio_padrao(vetor):
    media = sum(vetor)/len(vetor)
    somatorio = 0

    for i in vetor:
        somatorio += (i - media) ** 2

    return round((1/(len(vetor)-1) * somatorio) ** 0.5, 2)


lista = [x for x in range(1, 7)]
print(desvio_padrao(lista))


Exercicio 46:

def diversos(vetor=[]):
    print(vetor)
    vetor.reverse()
    print(vetor)
    print(sum(vetor)/len(vetor))


lista = [x for x in range(1, 10)]
diversos(lista)


Exercicio 47:

from random import randint

# matriz = [[randint(1, 20) for i in range(4)] for i in range(4)]
matriz = [[5, 13, 4, 19], [4, 16, 3, 6], [12, 7, 18, 14], [2, 17, 8, 19], [11]]


def maior_10(matriz):

    return sum([len([coluna for coluna in matriz[linha] if coluna > 10]) for linha in range(len(matriz))])


print(maior_10(matriz))


Resolucao dos exercicio 48 a 51

def diagonal_p(passo_l, passo_c, matriz=[], vertical=0, horizontal=0):
    soma = 0

    for linha in range(vertical, len(matriz)):
        for coluna in range(horizontal, len(matriz)):
            if (linha == vertical) and (coluna == horizontal):
                soma += matriz[linha][coluna]

        horizontal += passo_c
        vertical += passo_l

    return soma


matriz2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(diagonal_p(1, 1, matriz2, horizontal=1))  # Resolucao 48 - Acima da diagonal principal
print(diagonal_p(1, 1, matriz2, vertical=1))  # Resolucao 49 - Abaixo da diagonal principal
print(diagonal_p(1, 1, matriz2))  # Resolucao 50 - Na diagonal principal
print(diagonal_p(1, -1, matriz2, horizontal=2))  # Resolucao 51 - Na diagonal segundaria


Exercicio 52:

def transposta(matriz):
    b = []
    for linha in range(len(matriz)):
        temp = []
        for coluna in range(len(matriz)):
            temp.append(matriz[coluna][linha])

        b.append(temp)
    return b


matriz2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(transposta(matriz2))

Exercicio 52:

def soma_num_matriz(matriz):
    return sum([sum(mat) for mat in matriz])


matriz2 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
print(soma_num_matriz(matriz2))


Exercicio 53:

def matriz_identidade(matriz=[], passo_l=1, passo_c=1, vertical=0, horizontal=0):
    soma = 0

    for linha in range(vertical, len(matriz)):
        for coluna in range(horizontal, len(matriz)):
            if (linha == vertical) and (coluna == horizontal) and (matriz[linha][coluna] == 1):
                soma += 1
            elif matriz[linha][coluna] == 0:
                pass
            else:
                soma -= 1

        horizontal += passo_c
        vertical += passo_l

    if soma == len(matriz):
        return print('É uma matriz identidade')
    return print('Não é uma matriz identidade')


teste = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
teste2 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
teste3 = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

matriz_identidade(teste)
matriz_identidade(teste2)
matriz_identidade(teste3)

Exercicio 54:

from random import randint


def soma_num_matriz(matriz):
    return sum([sum(mat) for mat in matriz])


matriz = [[randint(1, 20) for i in range(4)] for i in range(4)]

print(soma_num_matriz(matriz))


Exercicio 55:

def soma_dos_passos(valor):
    def soma_ao_passo_matriz(passo_l, passo_c, matriz=[], vertical=0, horizontal=0):
        soma = 0
        for linha in range(vertical, len(matriz)):
            for coluna in range(horizontal, len(matriz)):
                if (linha == vertical) and (coluna == horizontal):
                    soma += matriz[linha][coluna]

            horizontal += passo_c
            vertical += passo_l

        return soma

    return soma_ao_passo_matriz(1, 1, valor) + soma_ao_passo_matriz(1, -1, valor, horizontal=2) - matriz[1][1]

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


print(soma_dos_passos(matriz))   # Falta retirar o numero duplicado do meio, vou fazer gambiarra.

Exercicio 56 e 57:

def retorna_linha(matriz, linha):
    return matriz[linha]


def retorna_soma_linha(matriz, linha):
    return sum(matriz[linha])



matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(retorna_linha(matriz, 2))
print(retorna_soma_linha(matriz, 2))


Exercicio 58:

def produto_de_matriz(a, b, c=[]):
    for linha in range(len(a)):
        temp = []
        for coluna in range(len(a)):
            res = 0
            for vertical in range(len(a)):
                res += a[linha][vertical] * b[vertical][coluna]
                input()
                print(a[linha][vertical], b[vertical][coluna], vertical, coluna)
            temp.append(res)
        c.append(temp)
    return c


matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]

print(produto_de_matriz(matriz1, matriz2))

Exercicio 59:


def uniao_vetor(vetor1, vetor2):
    return vetor1 + vetor2


a = list(range(10))
b = a[::-1].copy()

print(uniao_vetor(a, b))



Exercicio 60 - Não vou fazer esta muito generico.

Exercicio 61: Duas formas de fazer

from collections import Counter


def anagrama_facil(letras, resposta):
    texto1 = Counter(letras)
    texto2 = Counter(resposta)
    if texto1 == texto2:
        return True
    return False


def anagrama(letras, resposta):
    dicionario_letras = {}
    dicionario_resp = {}

    for a in letras:
        if a in dicionario_letras.keys():
            dicionario_letras[a] += 1
        else:
            dicionario_letras[a] = 0

    for b in resposta:
        if b in dicionario_resp.keys():
            dicionario_resp[b] += 1
        else:
            dicionario_resp[b] = 0

    if dicionario_letras == dicionario_resp:
        return True
    return False


print(anagrama_facil('aarfle', 'rafael'))
print(anagrama('aarfle', 'rafael'))


Exercicio 62 é muito tosco.

Exercicio 63 é muito tosco.

Exercicio 64 é god tosco.

Exercicio 65 é tosco

Exercicio 66 é tosco

Exercicio 67 


"""

import random

lista = min(random.sample(range(1_000_000), 1_000_000))

print(lista)
