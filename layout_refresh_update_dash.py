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


app = dash.Dash('layout refresh update app')
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


app.layout = html.Div([
                    html.H1(id='live-update-text'),
                    dcc.Interval(id='interval-component',
                                 interval=2000,
                                 n_intervals=0)

])


@app.callback(Output('live-update-text', 'children'),
             [Input('interval-component','n_intervals')]
             )
def update_layout(n):
    return "Crash free for {} refreshes".format(n)


if __name__ == '__main__':
    app.run_server(debug=True)
