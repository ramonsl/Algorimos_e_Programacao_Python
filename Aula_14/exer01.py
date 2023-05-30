
#Faça um programa que leia um vetor (lista) de 5 elementos inteiros e mostre na tela.


lista=[]

for i in range(5):
    valor=int(input("Digite o valor inteiro"))
    lista.append(valor)

#print(lista)

for i in range(5):
    print(f"{lista[i]}")
    
#soma dos elementos
total=0
for i in range(5):
    total+=lista[i]
print(total)
#media
print(total/5)

#soma tbm
total=sum(lista)
print(total)

i=0
while i<5:
    valor=int(input("Digite o valor inteiro"))
    lista.append(valor)
    i+=1
i=0
while i<5:
    print(f"{lista[i]}")
    i+=1