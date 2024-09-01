import numpy as np  # álgebra lineal
import pandas as pd  # procesamiento de datos
import matplotlib.pyplot as plt
#import network as nx
import time
import seaborn as sns
import re
import math

# Usar directamente la API de Seaborn para establecer el estilo
sns.set_style("whitegrid")
#sns.set_style("darkgrid")
sns.set_palette("tab10")

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
import datetime as dt

# El estilo 'seaborn-notebook' ha sido cambiado por el estilo correspondiente en Seaborn
sns.set_context("notebook", rc={
    "legend.fontsize": 15,
    "legend.title_fontsize": 16,
    "figure.figsize": (15, 5),
    "axes.labelsize": 18,
    "axes.titlesize": 20,
    "xtick.labelsize": 18,
    "ytick.labelsize": 18
})

# Opcionalmente, puedes seguir usando el estilo de Matplotlib, adaptado
# plt.style.use('seaborn-v0_8-notebook')

import warnings
warnings.filterwarnings("ignore")

# Cambia la ruta si el archivo no está en el mismo directorio
df = pd.read_csv('netflix_titles.csv')  # Asegúrate de que la ruta sea correcta
df.head()

df.info()

df.isna().sum()