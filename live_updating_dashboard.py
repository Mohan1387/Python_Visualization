import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import json
import datetime
import pandas_datareader.data as web
import requests
import urllib.request


app = dash.Dash('layout refresh update app')
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


app.layout = html.Div([
                    html.Div([
                        html.Iframe(src="https://www.flightradar24.com",
                                    height=500,
                                    width=1200)
                    ]),
                    html.Div([
                        html.Pre(id='counter_text',
                                 children='Active Flights Worldwide'),
                        dcc.Graph(id='live-update-graph', style={'width':1200}),
                        dcc.Interval(id='interval-component',
                                     interval=6000,
                                     n_intervals=0)
                    ])
])


counter_list = []

@app.callback(Output('counter_text', 'children'),
             [Input('interval-component', 'n_intervals')]
)
def update_layout(n):
    proxies = {'https': 'https://172.22.42.120:8080'}
    proxy = urllib.request.ProxyHandler(proxies)
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
    # Get response
    response = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    f = urllib.request.urlopen(response)
    page = f.read().decode('utf8')
    data = json.loads(page)
    counter = 0
    for element in data['stats']['total']:
        counter += data['stats']['total'][element]

    counter_list.append(counter)

    return "Active filghts Worldwide: {}".format(counter)


@app.callback(Output('live-update-graph', 'figure'),
             [Input('interval-component', 'n_intervals')])
def update_layout_graph(n):
    fig = go.Figure(data=[go.Scatter(x=list(range(len(counter_list))),
                                     y=counter_list,
                                     mode='lines+markers')
                          ])
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)