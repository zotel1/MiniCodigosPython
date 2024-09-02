import requests

# Define el IMDb ID o el título de la película
movie_id = "tt0100669"  # Puedes usar también el título de la película, por ejemplo: "Spiderman"

# Define la clave de API de OMDb
api_key = "TU-API-KEY"

# Define la URL de la API de OMDb
url = f"http://www.omdbapi.com/?i={movie_id}&apikey={api_key}"

# Realiza la solicitud GET
response = requests.get(url)
datos_pelicula = response.json()

# Verifica si la respuesta es exitosa
if datos_pelicula['Response'] == 'True':
    # Extrae y muestra los detalles de la película
    titulo = datos_pelicula['Title']
    año_lanzamiento = datos_pelicula['Year']
    dia_lanzamiento = datos_pelicula.get('Released', 'N/A')  # Puede que no siempre esté disponible
    genero = datos_pelicula['Genre']
    director = datos_pelicula['Director']
    calificacion_imdb = datos_pelicula['imdbRating']
    numero_votos = datos_pelicula['imdbVotes']

    print(f"Nombre de la película: {titulo}")
    print(f"Año de lanzamiento: {año_lanzamiento}")
    print(f"Día de lanzamiento: {dia_lanzamiento}")
    print(f"Género: {genero}")
    print(f"Director: {director}")
    print(f"Calificación en IMDb: {calificacion_imdb}")
    print(f"Número de votos: {numero_votos}")
else:
    print("No se pudo obtener la información de la película.")
