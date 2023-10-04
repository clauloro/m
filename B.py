def calcular_gondolas(n, x, pesos):

    for i in range(n):
        for j in range(n - i - 1):
            if pesos[j] > pesos[j + 1]:
                pesos[j], pesos[j + 1] = pesos[j + 1], pesos[j]

    count = 0
    i = 0
    j = n - 1

    while i <= j:
        if pesos[i] + pesos[j] <= x:
            count += 1
            i += 1
            j -= 1
        else:
            count += 1
            j -= 1

    return count

n, x = map(int, input("Ingrese el número de niños y el peso máximo por góndola: ").split())
pesos = list(map(int, input("Ingrese los pesos de los niños: ").split()))

resultado = calcular_gondolas(n, x, pesos)
print(resultado)