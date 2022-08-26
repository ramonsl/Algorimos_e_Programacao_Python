#Escreva um programa que converta uma temperatura de um padrão a outro usando estas fórmulas:

#Celsius para Fahrenheit: °F = 9/5 (°C) + 32
#Kelvin para Celsius: °C = K - 273,15
#Fahrenheit para Kelvin: K = 5/9 (°F - 32) + 273,15

#O Programa deve perguntar a temperatura em Celsius e exibir a temperatura em Kelvin e  Fahrenheit
celsius=float(input("Digite a temperatura\n"))
fahrenheit = ((9/5) * celsius) + 32
kelvin = (5/9 *(fahrenheit - 32)) + 273.15
print(f"Temperatura em celsius {celsius}")
print(f"Temperatura em Fahrenheit {fahrenheit}")
print(f"Temperatura em kelvin {kelvin}")