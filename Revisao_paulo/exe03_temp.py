
temp = float(input("Por favor, insira a temperatura que você deseja converter: "))

temperatura_original = input("Qual a escala da temperatura inserida? (Digite 'C' para Celsius, 'F' para Fahrenheit ou 'K' para Kelvin): ")

temperatura_covertida = input("Para qual escala você deseja converter a temperatura? (Digite '1' para Celsius, '2' para Fahrenheit ou '3' para Kelvin): ")

# refatorando aquela coisa feia da aual
if temperatura_original == 1:
    if temperatura_covertida == 2:
        temp = temp * 9/5 + 32
    elif temperatura_covertida == 3:
        temp = temp + 273.15
elif temperatura_original == 2:
    if temperatura_covertida == 1:
        temp = (temp - 32) * 5/9
    elif temperatura_covertida == 3:
        temp = (temp - 32) * 5/9 + 273.15
elif temperatura_original == 3:
    if temperatura_covertida == 1:
        temp = temp - 273.15
    elif temperatura_covertida == 2:
        temp = (temp - 273.15) * 9/5 + 32

# Finalmente, exiba a temperatura convertida.
print("A temperatura em", temperatura_covertida, "é", temp)
