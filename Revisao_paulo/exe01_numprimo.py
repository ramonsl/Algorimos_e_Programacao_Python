#Desenvolva um programa que verifique se um número fornecido pelo usuário é um número primo. Um número primo é aquele que é divisível apenas por 1 e por ele mesmo. Implemente a lógica correta para identificar se o número é primo ou não.
while True:
    # Primeiro, vamos pedir ao usuário um número.
    num = int(input("Insira um número"))

    # Vamos assumir que o número é primo (juro que nao é gambiarra)
    eh_primo = True

    # Um número primo é maior que 1 e apenas divisível por 1 e ele mesmo.
    # Então, primeiro, vamos verificar se o número é maior que 1.
    if num > 1:
        
        # Agora vamos verificar se o número é divisível por qualquer número (exceto 1 e ele mesmo).
        # Vamos fazer isso verificando se o número é divisível por qualquer número no intervalo de 2 ao número que o usuário inseriu.
        for i in range(2, num):
            # Se o número for divisível por 'i', então ele não é um número primo.
            if num % i == 0:
                eh_primo = False
                # Não precisamos verificar mais, então podemos interromper o laço.
                break
                
        # vamos imprimir se o número é primo ou não.
        if eh_primo:
            print(num, "é um número primo.")
        else:
            print(num, "não é um número primo.")
            
    # Se o número não é maior que 1, então ele não é um número primo.
    else:
        print(num, "não é um número primo.")
