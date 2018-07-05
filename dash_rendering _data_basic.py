import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd


app = dash.Dash('Test app')
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

np.random.seed(42)

rand_x = np.random.randint(1, 101, 100)
rand_y = np.random.randint(1, 101, 100)


app.layout = html.Div([dcc.Graph(id='ScatterPlot',
                                 figure={'data': [go.Scatter(x=rand_x,
                                                              y=rand_y,
                                                              mode='markers',
                                                             marker={'size': 12,
                                                                     'color': 'rgb(51,204,153)',
                                                                     'symbol': 'pentagon',
                                                                     'line': {'width': 2}})],
                                           'layout': go.Layout(title='My ScatterPlot')}
                                 )])

if __name__ == '__main__':
    app.run_server(debug=True)