#Faça um programa que leia um número N, e realize a soma dos números de 1 a N. Ao final, deve-se escrever o resultado. Esse algoritmo deve ser feito duas vezes, uma usando o While e for


numero_n=int(input("Digite o Número n\n"))
soma=0
#10
i=1
while i <numero_n+1:
    soma=soma+i
    i=i+1
    

print( f"A SOMA de 1 a {numero_n} É {soma}")