
opcao = -1
while opcao != 0:
    opcao = int(input("escolha uma unidade de temperatura:\n1 para Celsius\n2 para Fahrenheit\n3 para kelvin\n0 para sair\ndigite;"))  
    if opcao == 1:
        celsius = float(input("digite a temperatura em celsius:"))
        fahrenheit = (celsius*9/5)+32
        kelvin = celsius + 273.15
        print("temperatura em celsius:", celsius)
        print(f"temperatura em fahrenheit: {fahrenheit}")
        print(f"temperatura em kelvin: {kelvin}")
    elif opcao == 2:
        fahrenheit = float(input("digite a temperatura em fahrenheit:"))
        celsius = (fahrenheit-32)*5/9
        kelvin = celsius + 273.15
        print("temperatura em fahrenheit:", fahrenheit)
        print(f"temperatura em celsius: {celsius}")
        print(f"temperatura em kelvin: {kelvin}")
    elif opcao == 3:
        kelvin = float(input("digite a temperatura em kelvin:"))
        celsius = kelvin - 273.15
        fahrenheit = (celsius*9/5)+32
        print("temperatura em kelvin:", kelvin)
        print(f"temperatura em celsius: {celsius}")
        print(f"temperatura em fahrenheit: {fahrenheit}")
    else:
        print("opcao invalida, digite uma valida")