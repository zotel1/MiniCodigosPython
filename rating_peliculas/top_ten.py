import requests

# Lista de IMDb IDs para las 10 mejores películas según IMDb
# Puedes modificar esta lista según tus preferencias
movies_ids = [
    "tt0111161",  # The Shawshank Redemption
    "tt0068646",  # The Godfather
    "tt0071562",  # The Godfather: Part II
    "tt0468569",  # The Dark Knight
    "tt0050083",  # 12 Angry Men
    "tt0108052",  # Schindler's List
    "tt0167260",  # The Lord of the Rings: The Return of the King
    "tt0110912",  # Pulp Fiction
    "tt0060196",  # The Good, the Bad and the Ugly
    "tt0137523",  # Fight Club
]

# Tu clave de API de OMDb
api_key = "TU-API-KEY"

print("Top 10 Rating Movies:\n")
print("Película / Calificación")

for movie_id in movies_ids:
    # Definimos la URL con el IMDb ID
    url = f"http://www.omdbapi.com/?i={movie_id}&apikey={api_key}"
    
    # Realizamos la solicitud GET
    response = requests.get(url)
    movie_data = response.json()
    
    # Verificamos si la respuesta es exitosa
    if movie_data['Response'] == 'True':
        title = movie_data['Title']
        rating = movie_data['imdbRating']
        print(f"{title} / {rating}")
    else:
        print(f"No se pudo obtener información para la película con ID: {movie_id}")
