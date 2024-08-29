#__import__

# Funciones

def numeroAPalabras(numero):
    """
    Esta función convierte un número entero de hasta tres dígitos a su representación en palabras.

    Parámetros:
    número (int): número entero de hasta 3 dígitos a convertir

    Retorno:
    str: representación en palabras de número
    """

    en_palabras = ''
    unidades = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez']

    decenas = ['', 'dieci', 'veinti', 'treinta y', 'cuarenta y', 'cincuenta y', 'sesenta y', 'setenta y', 'ochenta y', 'noventa y']

    centenas = ['', 'cien', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'schocientos', 'novecientos']


    return en_palabras


# Programa principal
# Ejemplo 379 se escribe: Tresciento setenta y nueve
valor = 379
print(numeroAPalabras(valor)) # >>> Trescientos setenta y nueve