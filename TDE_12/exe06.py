#Efetue um programa que leia 5 números. Para cada número fornecido, escrever se ele é NULO, NEGATIVO ou POSITIVO.

for i in range(5):
    numero=int(input("Digite o numero\n"))
    if numero==0:
        print( "valor igual a zero, nulo")
    elif numero >0:
        print( "Valor positivo")
    else:
        print( "Valor negativo")

print("Agora com while")
i=0
while i<5:
    numero=int(input("Digite o numero\n"))
    if numero==0:
        print( "valor igual a zero, nulo")
    elif numero >0:
        print( "Valor positivo")
    else:
        print( "Valor negativo")
    i=i+1
