#Faça um programa que leia um vetor (lista) de número não determinado de nomes, ao ser digitado "fim" deve mostrar na tela todos os nomes lidos.

lista_nome=[]
while(True):
    nome=input("Digite o seu nome?")
    if nome=='fim' or nome=='FIM':
        break
    lista_nome.append(nome)

print("Exibindo com for i in range" )
for i in range(len(lista_nome)):
    print(f"{lista_nome[i]}")
    
print("Exibindo com for each" )
for nome in lista_nome:
    print(f"{nome}")
    
for i in range(len(lista_nome),0,-1):
    print(f"{lista_nome[i-1]}")

lista_nome.reverse()
print (lista_nome)