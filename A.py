def contar_alumnos_unicos(n, alumnos):
    for i in range(n):
        intercambio = False
        for j in range(n - i - 1):
            if alumnos[j] > alumnos[j + 1]:
                alumnos[j], alumnos[j + 1] = alumnos[j + 1], alumnos[j]
                intercambio = True
        if not intercambio:
            break
    
    count = 1
    for i in range(1, n):
        if alumnos[i] != alumnos[i - 1]:
            count += 1
    
    return count

t = int(input("Ingrese el número de casos de prueba: "))

for _ in range(t):
    n = int(input("Ingrese el número de alumnos: "))
    alumnos = list(map(int, input("Ingrese los identificadores de los alumnos: ").split()))

    resultado = contar_alumnos_unicos(n, alumnos)
    print(resultado)