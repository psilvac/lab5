# Código para generar un archivo con números del 1 al 100,000

file_path = '/home/ec2-user/numeros.txt'  # Cambia esto según la estructura de tu directorio

with open(file_path, 'w') as file:
    for i in range(1, 100001):
        file.write(str(i) + '\n')

print(f'Se ha creado el archivo {file_path} con números del 1 al 100,000.')