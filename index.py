import unicodedata

alfabeto = 'abcdefghijklmnopqrstuvwxyz0123456789 '
cifra = '9876543210zyxwvutsrqponmlkjihgfedcba '


def tratar_msg(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sem_acentos = ''.join(
        char for char in texto_normalizado if unicodedata.category(char) != 'Mn')
    return texto_sem_acentos.lower()


def criptografar(entrada, deslocamento):
    texto = tratar_msg(entrada)
    texto_criptografado = ''

    for letra in texto:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            texto_criptografado += cifra[(indice + deslocamento) % len(cifra)]
        else:
            texto_criptografado += letra
    return texto_criptografado


def descriptografar(entrada, deslocamento):
    texto = tratar_msg(entrada)
    texto_descriptografado = ''

    for letra in texto:
        if letra in cifra:
            indice = cifra.index(letra)
            texto_descriptografado += alfabeto[(indice - deslocamento) % len(alfabeto)]
        else:
            texto_descriptografado += letra
    return texto_descriptografado


mensagem_original = input("Digite a mensagem: ")
mensagem_cifrada = criptografar(mensagem_original, 10)
print("Mensagem cifrada:", mensagem_cifrada)

mensagem_decifrada = descriptografar(mensagem_cifrada, 10)
print("Mensagem decifrada:", mensagem_decifrada)
