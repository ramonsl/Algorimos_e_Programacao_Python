#Faça um programa que leia um vetor(lista) de 5 elementos e mostre na tela na ordem inversa que foi digitada.

lista=[] 

for i in range(5):
    valor=int(input("Digite o valor inteiro"))
    lista.append(valor)

#print(lista)
tam=len(lista)
for i in range(tam,0,-1):
    print(f"{lista[i-1]}")
    
   #print(reverse) 
lista.reverse()
print(lista)
#print(lista invertida)
for i in range(5):
    print(f"{lista[i]}")