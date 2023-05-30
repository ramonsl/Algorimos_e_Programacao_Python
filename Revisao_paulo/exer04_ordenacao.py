#Desenvolva um programa que solicite ao usuário 10 números e os exiba em ordem crescente em uma linha e em outras duas os pares e os ímpares .

#listas pra guardas os valore (ATE AGORA SO ESSE PRECISOU DE FATO DE UMA LISTA)
numeros = []
pares = []
impares = []
qtd=3
# Leitura dos numero
for i in range(qtd):
    num = int(input("Qual um número: "))  
    numeros.append(num)  #coloca na lista
    
    # Se o número for par, números pares. Se for ímpar,números ímpares.
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

#recomendo fazer isso usando o agortimo burblesort, mas como vcs taão usando gameshark tambem vou usar.
numeros.sort()
pares.sort()
impares.sort()

print(f"Todos os números em ordem crescente: {numeros}")
print(f"Números pares em ordem crescente: {pares}")
print(f"Números ímpares em ordem crescente: {impares}")
