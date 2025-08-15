def imprimeImpares(max):
    i = 0
    while i <= max:
        if (i % 2) != 0:
            print(i)
        i += 1


def imprimePrimos(max):
    num = 1
    while num <= max:
        count = 0
        for i in range(1, num + 1):
            if (num % i) == 0:
                count += 1
        if count == 2 or num == 1:
            print(num)
        num += 1


def imprimeFibonacci(max):
    num1 = 0
    num2 = 1

    print(num1)
    print(num2)

    while num2 <= max:
        aux = num2
        num2 = num1 + num2
        num1 = aux
        print(num2)


def imprimeExponencial(base, max):
    i = 0
    valor = 0
    while valor <= max:
        valor = base**i
        print(valor)
        i += 1


imprimeImpares(100)
imprimePrimos(100)
imprimeFibonacci(100)
imprimeExponencial(2, 100)
