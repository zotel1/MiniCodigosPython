#Importamos librerias necesarias
import numpy as np # álgebra lineal
import pandas as pd # procesamiento de datos
import matplotlib.pyplot as plt 
%matplotlib inline
#import network as nx
import time
import seaborn as sns
import re
import math
sns.set_style("whitegrid")
#sns.set_style(tylr="darkgrid")
sns.set_palette("tab10")
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode,iplot
import datetime as dt
plt.style.use('seaborn-notebook')
params = {'legend.fontsize': 15,
          'legend.title_fontsize': 16,
          'figure.figsize': (15, 5),
          'axes.labelsize': 18,
          'axes.titlesize': 20,
          'xtick.labelsize': 18,
          'ytick.labelsize': 18}
plt.rcParams.update(params)
img_fmt = 'svg'

import warnings
warnings.fillterwarnings("ignore")



