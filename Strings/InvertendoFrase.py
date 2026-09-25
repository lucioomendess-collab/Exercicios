# Inverter palavras de uma frase
frase = input('Digite uma frase: ')
resultado = " ".join(frase.split()[::-1])
print(resultado)