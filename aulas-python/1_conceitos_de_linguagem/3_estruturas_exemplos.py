a = 2
b = 3


def exemplo_if(a, b):
    """
    Função que checa o que um número é em relação ao outro
    :param a:
    :param b:
    :return:
    """
    if a < b:
        print('A é menor do que B')
    elif a == b:
        print('A é igual a B')
    else:
        print('A é maior do que B')


def exemplo_while():
    """
    Este código irá imprimir os números de 1 a 100 até que a condição do while
    seja satistfeita
    :return:
    """
    numero = 0
    # Enquanto a condição for atendida as linhas 24 a 27 serão executadas
    while numero < 100:
        numero += 1
        # numero = numero + 1
        # Outra forma de escrever é numero += 1
        print(numero)


def exemplo_for():
    """
    Este código irá imprimir cada elemento do loop que seja par
    :return:
    """
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for numero in numeros:
        if numero % 2 == 0:
            print(numero)
