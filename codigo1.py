# Abrir el archivo en modo lectura
with open('informacion.txt', 'r') as archivo:
    # Leer cada línea del archivo
    for linea in archivo:
        # Eliminar los espacios en blanco al principio y al final de la línea
        linea = linea.strip()
        # Imprimir la información detallada de cada línea
        print(f"Línea: '{linea}'")
        print(f"Número de caracteres: {len(linea)}")
        print(f"Palabras: {linea.split()}")  # Dividir la línea en palabras
        print()  # Imprimir una línea en blanco entre cada línea del archivo nuevo
