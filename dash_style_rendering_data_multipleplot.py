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

colors = {'background': '#111111', 'text': '#7FDBFF'}

app.layout = html.Div(children=[
            html.H1("HelloDash", style={'textAlign': 'center', 'color': colors['text']}),
            html.Div('Dash: Web Dashboards with Python', style={'textAlign': 'center', 'color': colors['text']}),
            dcc.Graph(id='Example',
                      figure={'data': [
                          {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                          {'x': [1, 2, 3], 'y':[2, 4, 5], 'type':'bar', 'name':'NYC'}
                      ],
                              'layout':{'plot_bgcolor': colors['background'],
                                        'paper_bgcolor':colors['background'],
                                        'font':{'color': colors['text']},
                                        'title':'BAR PLOTS !'
                                        }}),
            dcc.Graph(id='ScatterPlot_2',
                                 figure={'data': [go.Scatter(x=rand_x,
                                                              y=rand_y,
                                                              mode='markers',
                                                             marker={'size': 12,
                                                                     'color': 'rgb(200,204,53)',
                                                                     'symbol': 'pentagon',
                                                                     'line': {'width': 2}})],
                                           'layout': go.Layout(title='My Scatter Plot 2')})
], style={'backgroundColor': colors['background']})


if __name__ == '__main__':
    app.run_server(debug=True)
