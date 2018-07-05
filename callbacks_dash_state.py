import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd


app = dash.Dash('Mpg app')
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


app.layout = html.Div([
                    dcc.Input(id='number-in', value=1, style={'fontSize':24}),
                    html.Button(id='submit-button',
                                n_clicks=0,
                                children='submit Here',
                                style={'fontSize': 24}),
                    html.H1(id='number-out')
])


@app.callback(Output('number-out', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('number-in', 'value')])
def Output(n_clicks, number):
    return "{} was typed in, and button was clicked {} times".format(number,n_clicks)


if __name__ == '__main__':
    app.run_server()