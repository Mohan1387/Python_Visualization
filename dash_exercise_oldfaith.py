import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

app = dash.Dash('Test app')
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

df = pd.read_csv('oldfaith.csv')

data = [go.Scatter(x=df['X'],
                   y=df['Y'],
                   mode='markers',
                   #text=df['D'],
                   #hoverinfo='x+y+text',
                   marker=dict(size=8,
                              color='rgb(20,145,120)',
                              symbol='circle',
                              opacity = 0.8,
                              line={'width': 1}
                              ))]
layout = go.Layout(title='Old Faith Exe',
                  xaxis={'title': 'Duration of current Eruption'},
                  yaxis=dict(title='Wait time till Next Eruption'),
                  hovermode='compare')

fig = go.Figure(data=data, layout=layout)

app.layout = html.Div([dcc.Graph(id='ScatterPlot',
                                 figure=fig
                                 )])

if __name__ == '__main__':
    app.run_server(debug=True)