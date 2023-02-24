def binary(decimal):
    binary = ''

    while decimal // 2 != 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return str(decimal) + binary


num = int(input('Introduce el numero que quieres convertir a Binario'))
print(binary(num))
