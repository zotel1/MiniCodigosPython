#__import__

# Funciones

ingresarValor = int(input('introduce un numero: '))

def numeroAPalabras(numero):
    """
    Esta función convierte un número entero de hasta tres dígitos a su representación en palabras.

    Parámetros:
    número (int): número entero de hasta 3 dígitos a convertir

    Retorno:
    str: representación en palabras de número
    """

    # Representando los digitos en palabras segun su posicion
    en_palabras = ''
    unidades = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']

    decenas = ['', 'dieci', 'veinti', 'treinta y', 'cuarenta y', 'cincuenta y', 'sesenta y', 'setenta y', 'ochenta y', 'noventa y']

    centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'schocientos', 'novecientos']

    # COnvirtiendo el número a str asegurando que siempre tenga tres dígitos
    numero = '0' * (3 - len(str(numero))) + str(numero) #9 ==> 009
    
    # Convirtiendo cada dígito a número
    unidad = int(numero[-1])
    decena = int(numero[-2])
    centena = int(numero[-3])

    # Juntando todo
    en_palabras = '{} {}{}'.format(centenas[centena], decenas[decena], unidades[unidad]).strip()

    # Encargandose de casos especiales
    en_palabras = en_palabras.replace('dieciuno', 'once')
    en_palabras = en_palabras.replace('diecidos', 'doce')
    en_palabras = en_palabras.replace('diecitres', 'trece')
    en_palabras = en_palabras.replace('diecicuatro', 'catorce')
    en_palabras = en_palabras.replace('diecicinco', 'quince')

    if en_palabras.endswith('dieci'):
        en_palabras = en_palabras.replace('dieci', 'diez')

    elif en_palabras.endswith('veinti'):
        en_palabras = en_palabras.replace('veinti', 'veinte')
    elif en_palabras.endswith(' y'):
        en_palabras = en_palabras[:-2]
    elif en_palabras.endswith('ciento'):
        en_palabras = en_palabras.replace('ciento', 'cien')
    return en_palabras.capitalize()


# Programa principal
# Ejemplo 379 se escribe: Tresciento setenta y nueve
valor = ingresarValor
print(f"El número {ingresarValor} se escribe como: {numeroAPalabras(valor)}") # >>> Trescientos setenta y nueve