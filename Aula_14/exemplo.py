lista_de_compras=["abacate","melao", "uva"]

tamanho=len(lista_de_compras)
print(tamanho)

print(lista_de_compras)
lista_de_compras[1]="banana"
print(lista_de_compras[1])
print(lista_de_compras[0:2])

print(lista_de_compras[1:])

lista_de_compras.append("mamão")
lista_de_compras.insert(1,"limão")
print(lista_de_compras)
for i in range(len(lista_de_compras)):
    print (f"item {i} {lista_de_compras[i]}")
    if lista_de_compras[i]=='banana':
        print("Tem banana")
lista_de_compras.pop()
lista_de_compras.pop(0)
lista_de_compras.remove("banana")

for item in lista_de_compras:
    print (f"item {item}")

