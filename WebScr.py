import re
from colorama import Fore
import requests

# Definición de la URL del sitio web que se va a analizar
website = "https://www.vulnhub.com/"

# Realiza una solicitud GET al sitio web y obtiene el contenido HTML de la página
resultado = requests.get(website)
content = resultado.text

# Define un patrón regex para encontrar las entradas de máquinas en la página web
patron = r"/entry/[\w-]*"

# Utiliza el patrón regex para encontrar todas las coincidencias de máquinas en el contenido de la página
maquinas_repetidas = re.findall(patron, str(content))

# Elimina las entradas duplicadas usando un conjunto y las convierte de nuevo en una lista
sin_duplicados = list(set(maquinas_repetidas))

# Lista para almacenar los nombres finales de las máquinas
maquinas_final = []

# Itera sobre las entradas sin duplicados para limpiar y agregar el nombre de la máquina a la lista final
for i in sin_duplicados:
    nombre_maquinas = i.replace("/entry/", "")
    maquinas_final.append(nombre_maquinas)
    print(nombre_maquinas)

# Nombre de la máquina que se desea buscar
maquina_noob = "noob-1"
# Bandera para indicar si la máquina buscada existe
existe_noob = False

# Itera sobre la lista final de máquinas para comprobar si la máquina buscada existe
for a in maquinas_final:
    if a == maquina_noob:
        existe_noob = True
        break

# Definición de colores utilizando la librería colorama para mejorar la visualización en la consola
color_verde = Fore.GREEN
color_amarillo = Fore.YELLOW

# Imprime un mensaje dependiendo de si la máquina buscada existe o no
if existe_noob:
    print("\n" + color_verde + "No hay ninguna máquina nueva")
else:
    print("\n" + color_amarillo + "¡Máquina nueva!")
