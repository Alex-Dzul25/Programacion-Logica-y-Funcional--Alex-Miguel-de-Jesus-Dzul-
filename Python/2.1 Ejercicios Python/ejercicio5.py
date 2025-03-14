
def cadenaBits(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return cadenaBits(numero // 2) + str(numero % 2)


print(cadenaBits(20)) 



def dec_bin(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return dec_bin(num // 2) + str(num % 2)


numero = int(input("Ingrese un número en base 10: "))


binario = dec_bin(numero)
print(f"El número {numero} en binario es: {binario}")
