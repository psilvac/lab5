import time

# Inicia el cronometro
start_time = time.time()


# Codigo para generar un archivo con numeros del 1 al 100,000


with open('/app/resultado.txt', 'w') as file:
    for i in range(1, 100001):
        file.write(str(i) + '\n')

print('Se ha creado el archivo con numeros del 1 al 100,000')


# Detiene el cronometro
end_time = time.time()

# Calcula y muestra el tiempo de ejecucion
execution_time = end_time - start_time
print(f"Tiempo de ejecucion: {execution_time} segundos")
