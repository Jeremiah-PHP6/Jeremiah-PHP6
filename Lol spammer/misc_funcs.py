### Funciones misceláneas / helpers

# Limpia la consola
def limpiar_consola():
    # Desactivado a petición de un ayudante
    # os.system('cls')
    pass

# Muestra un salto de linea
def salto():
    print('\n')

# Verifica si una variable puede ser convertida a int
# Recibe como parámetro un elemento de cualquier tipo
# Retorna un booleano con la verificación
def es_entero(element)-> bool:
    try:
        int(element)
        return True
    except ValueError:
        return False

# Verifica si una variable puede ser convertida a flotante
# Recibe como parámetro un elemento de cualquier tipo
# Retorna un booleano con la verificación
def es_numerico(element)-> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False