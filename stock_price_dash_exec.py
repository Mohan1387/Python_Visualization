import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd
import numpy as np
import json
import datetime
import pandas_datareader.data as web
import requests


app = dash.Dash('graph update app')
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

nasdaq_stocks = pd.read_csv('NASDAQcompanylist.csv')

proxies = {'http': 'http://172.22.42.120:8080', 'https': 'https://172.22.42.120:8080'}
s = requests.Session()
s.proxies.update(proxies)

'''
start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 1, 27)
proxies = {'http': 'http://172.22.42.120:8080','https': 'https://172.22.42.120:8080'}
s = requests.Session()
s.proxies.update(proxies)
f = web.DataReader('TSLA', 'iex', start, end, session=s, retry_count=3, pause=0.001)
print(f.columns) # ['open', 'high', 'low', 'close', 'volume'] and date is the index
'''

app.layout = html.Div([html.H1("Stock Ticker Dashboard"),

                html.Div([html.H3("Select stock symbols: ",
                                  style={'color': "rgba(117, 117, 117, 0.95)", 'paddingRight': '30px'}),
                    dcc.Dropdown(id='drop-select',
                                 options=[{'label': getattr(row, 'Name'), 'value': getattr(row, 'Symbol')} for row in nasdaq_stocks.itertuples(index=True, name='Pandas')],
                                 multi=True,
                                 value=['TSLA'],
                                 )
                         ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top'}),

                html.Div([html.H3("Select start and end Date: ",
                                  style={'color': "rgba(117, 117, 117, 0.95)"}),
                    dcc.DatePickerRange(
                        id='date-picker-range',
                        start_date=datetime.datetime(2018, 1, 1),
                        end_date=datetime.datetime.now(),
                        max_date_allowed=datetime.datetime.now(),
                        min_date_allowed=datetime.datetime(2015, 1, 1)
                        #end_date_placeholder_text='Select a date!'
                    )
                ], style={'display': 'inline-block'}),

                html.Div([
                    html.Button(id='submit-button',
                            n_clicks=0,
                            children='Submit',
                            style={'fontSize': 24,
                                   'marginLeft':'30px'})
                        ], style={'display': 'inline-block'}),

                html.Div([
                    dcc.Graph(id='feature-graph')
                ], style={'verticalAlign': 'top'})
])


@app.callback(Output('feature-graph', 'figure'),
              [Input('submit-button', 'n_clicks')],
              [State('drop-select', 'value'),
               State('date-picker-range', 'start_date'),
               State('date-picker-range', 'end_date')],
              )
def update_graph(n_clicks, stock_symbol, start_dt, end_dt):
    traces = []
    for stk in stock_symbol:
        stocks_data = web.DataReader(stk, 'iex', start_dt, end_dt, session=s, retry_count=3, pause=0.001)
        trace = go.Scatter(x=stocks_data.index,
                           y=stocks_data['close'],
                           name=stk,
                           mode='lines')
        traces.append(trace)

    layout = go.Layout(title=' ,'.join(stock_symbol)+' Closing Price', height=300)

    figure = go.Figure(data=traces, layout=layout)
    return figure


if __name__ == '__main__':
    app.run_server()
