# Importamos librerias
import pandas as pd  # procesamiento de datos
import numpy as np  # álgebra lineal
import ast
pd.set_option('display.max_columns', None)

movies = pd.read_csv('/content/tmdb_5000_movies.csv')
credits = pd.read_csv('/content/tmdb_5000_credits.csv', encoding = "utf-8")

print(movies.shape)


