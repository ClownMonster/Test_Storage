import plotly.graph_objects as go

import numpy as np
import pandas as pd
import scipy
from random import randint
from scipy import signal

np.random.seed(1) # system refresh seed 

x = np.linspace(0, 10, 100)
y = np.sin(x)
noise = 10.0 + 2 * randint(1,100) # replacce your noise data here i have added Your check case
y_noise = y + noise

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(size=2, color='black'),
    name='Sine'
))
 
fig.add_trace(go.Scatter(
    x=x,
    y=y_noise,
    mode='markers',
    marker=dict(
        size=6,
        color='royalblue',
        symbol='circle-open'
    ),
    name='Noisy Sine'
))

fig.add_trace(go.Scatter(
    x=x,
    y=signal.savgol_filter(y,
                           53, # window size used for filtering
                           3), # order of fitted polynomial
    mode='markers',
    marker=dict(
        size=6,
        color='mediumpurple',
        symbol='triangle-up'
    ),
    name='ClownMonster'
))

fig.show()
