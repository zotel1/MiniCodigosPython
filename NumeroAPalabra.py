#__import__

# Funciones

#valorNumerico = input(int(f'introduce un numero: '))

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
    return en_palabras.capitalize()


# Programa principal
# Ejemplo 379 se escribe: Tresciento setenta y nueve
valor = 318
print(numeroAPalabras(valor)) # >>> Trescientos setenta y nueve