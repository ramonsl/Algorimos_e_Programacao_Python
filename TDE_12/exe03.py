#Efetue um programa que mostre todos os números inteiros ímpares situados numa  faixa de dois números digitados pelo usuário. Esse algoritmo deve ser feito duas vezes uma usando o WHILE e FOR

inicio= int(input("Digite o valor inicial"))
fim= int(input("Digite o valor final"))
x=inicio
####não 'é obrigatorio
while inicio>fim:
    fim= int(input("Digite o valor final"))

for x in range(inicio,fim,+1):
    if x%2!=0:
        print(x)
   # x+=1

x=inicio
while x<fim:
    if x%2!=0:
        print(x)
    x+=1