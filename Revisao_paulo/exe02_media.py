#Crie um programa que solicite ao usuário uma quantidade de números e, em seguida, peça para ele digitar os valores correspondentes. O programa deve calcular e exibir a média dos números fornecidos.
while True:
    # quatidade de números que deseja digitar.
    quantidade = int(input("Digite a quantidade de números: "))

    # Crie uma variável para armazenar a soma dos números.
    soma = 0

    #for pra fazer o laço (SIM DA PRA USAR O WHILE).
    for i in range(quantidade):
        numero = float(input("Digite o número " + str(i+1) + ": "))
        soma += numero  
        # soma = soma + numero

    media = soma / quantidade

    print("A média dos números que você digitou é:", media)
