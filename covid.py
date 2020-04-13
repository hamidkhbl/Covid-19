#%%
# imports
import numpy as np 
import pandas as pd 
import dash
import dash_core_components as dcc
import dash_html_components as html 
import plotly.graph_objs as go
import requests

#%%
# download the data from github
address = 'https://health-infobase.canada.ca/src/data/covidLive/covid19.csv'
fileName = 'data.csv'
r = requests.get(address)
with open(os.path.join(fileName), mode='wb') as file:
    file.write(r.content)

#%%
# read the data
df = pd.read_csv('data.csv')

#%%
# %%


# %%
