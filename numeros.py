import time

# Obten el tiempo de inicio
inicio_tiempo = time.time()

with open('numeros.txt', 'w') as archivo:
    for numero in range(1, 1000000001):
        archivo.write(str(numero) + '\n')

# Obten el tiempo de finalizacion
fin_tiempo = time.time()

# Calcula el tiempo total de ejecucion
tiempo_total = fin_tiempo - inicio_tiempo

print(f"Archivo creado exitosamente en {tiempo_total} segundos.")
