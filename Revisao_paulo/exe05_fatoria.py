#Desenvolva um programa que solicite ao usuário um número e calcule o fatorial desse número. 
# O fatorial de um número é o produto de todos os números inteiros de 1 até o próprio número.
while True:
    num = int(input("Digite um número: "))

    #iniciailizar var em 1
    resultado = 1

    #com um laço percorrer tods os valore
    for i in range(1, num + 1):
        resultado = resultado * i

    print("O fatorial de", num, "é", resultado)


    #plus usem recursao no futuro