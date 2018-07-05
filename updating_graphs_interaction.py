import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import json
import base64


app = dash.Dash('graph update app')
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

df = pd.read_csv('mpg.csv')
df['year'] = np.random.randint(-4,5,len(df))*0.1 + df['model_year']

app.layout = html.Div([
                html.Div([
                    dcc.Graph(id='mpg-scatter',
                              figure={'data':[go.Scatter(x=df['year']+1900,
                                                         y=df['mpg'],
                                                         text=df['name'],
                                                         hoverinfo='text'+'y'+'x',
                                                         mode='markers'
                                                         )],
                              'layout': go.Layout(title='MPG Data',
                                                  xaxis={'title': 'MPG Year'},
                                                  yaxis={'title':'MPG'},
                                                  hovermode='closest')
                                    })
                        ], style={'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top'}),
                html.Div([
                    dcc.Graph(id='mpg_line',
                              figure={'data': [go.Scatter(x=[0, 1],
                                                          y=[0, 1],
                                                          mode='lines'
                                                          )],
                                      'layout':go.Layout(title='Accleration', margin={'l': 0})}) #left=l,right=r,top=t,bottom=b
                ], style={'width': '20%', 'display': 'inline-block', 'height': '50%'}),
                html.Div([
                    dcc.Markdown(id='mpg_stats')
                ], style={'width': '20%', 'display': 'inline-block', 'height': '50%'})
])


@app.callback(Output('mpg_line','figure'),
              [Input('mpg-scatter', 'hoverData')])
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    figure = {'data': [go.Scatter(x=[0, 1],
                                  y=[0,60/df.iloc[v_index]['acceleration']],
                                  mode='lines',
                                  line={'width': 3*df.iloc[v_index]['cylinders']}
                                 )],
              'layout': go.Layout(title=df.iloc[v_index]['name'],
                                  xaxis={'visible':False},
                                  yaxis={'visible': False, 'range':[0,60/df['acceleration'].min()]},
                                  margin={'l': 0},
                                  height=300)
              }

    return figure


@app.callback(Output('mpg_stats','children'),
              [Input('mpg-scatter', 'hoverData')])
def callback_stats(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = """
            {} Cylinders
            {}cc Displacement
            0 tp 60 in {} seconds   
            """.format(df.iloc[v_index]['cylinders'],
                       df.iloc[v_index]['displacement'],
                       df.iloc[v_index]['acceleration'])

    return stats


if __name__ == '__main__':
    app.run_server()