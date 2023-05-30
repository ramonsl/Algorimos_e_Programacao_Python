#Crie um programa que solicite ao usuário uma sequência de números separados por
# vírgula e exiba a soma apenas dos números pares da sequência.

string_de_numeros = input("Digite uma sequência de números, separados por vírgula: ")

#transformar a string em uma lista(acho que é o que esta pedido ..perguntar pro paulo se ta certo)

lista = string_de_numeros.split(',')
#eu faria sem lista inclusive
soma = 0  

# Percorrer a lista
for num_str in lista:
    num = int(num_str)  # Converte a string para um número inteiro
    if num % 2 == 0:  # Verifica se o número é par
        soma += num  

# Exibe o resultado
print("A soma dos números pares é:", soma)
