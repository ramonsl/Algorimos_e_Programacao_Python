#Faça um programa que escreva os números de 1 a 20, em ordem decrescente.

valor=20

while valor>=1:
    print (f"{valor}\n")
    valor=valor-1

print("Agora com for\n")
valor=20
for valor in range(valor,0,-1):
     print (f"{valor}\n")
print("Agora com for denovo\n")

 