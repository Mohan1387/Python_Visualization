import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd

df = pd.read_csv('wheels.csv')

app = dash.Dash('wheels app')
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

features = df.columns

app.layout = html.Div([
            dcc.RadioItems(id='wheels',
                           options=[{'label': i, 'value': i} for i in df['wheels'].unique()],
                           value=1),
            html.Div(id='wheels-output'),
            html.Hr(),
            dcc.RadioItems(id='colors',
                           options=[{'label': i, 'value': i} for i in df['color'].unique()],
                           value='blue'),
            html.Div(id='color-output')

], style={'fontFamily': 'helvetica', 'fontSize': 18})


@app.callback(Output('wheels-output', 'children'),
              [Input('wheels', 'value')])
def callback_a(wheels_value):
    return "you chose {}".format(wheels_value)


@app.callback(Output('color-output', 'children'),
              [Input('colors', 'value')])
def callback_b(color_value):
    return "you chose {}".format(color_value)


if __name__ == '__main__':
    app.run_server()