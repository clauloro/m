def maximo_numero_peliculas(n, horarios):
    horarios.sort(key=lambda x: x[1])
    
    count = 0
    end_time = 0
    
    for horario in horarios:
        if horario[0] >= end_time:
            count += 1
            end_time = horario[1]
    
    return count

n = int(input("Ingrese el número de películas calendarizadas: "))

horarios = []
for _ in range(n):
    a, b = map(int, input("Ingrese el tiempo de inicio y fin de una película: ").split())
    horarios.append((a, b))

resultado = maximo_numero_peliculas(n, horarios)
print(resultado)