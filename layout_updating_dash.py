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


app = dash.Dash('graph update app')
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

crash_free = 0

def refresh_layout():
    global crash_free
    crash_free += 1
    return html.H1('Crash free for {} refreshes'.format(crash_free))


app.layout = refresh_layout


if __name__ == '__main__':
    app.run_server()
