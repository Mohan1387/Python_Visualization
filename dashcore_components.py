import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div([

            html.Label('Dropdown'),
            dcc.Dropdown(options=[{'label': 'New York City',
                                   'value': 'NYC'},
                                  {'label': 'Los Angels',
                                   'value': 'LA'}],
                         value='LA'),

            html.Label('Slider'),
            dcc.Slider(min=-10, max=10, step=0.5, value=0, marks={i: i for i in range(-10, 10)}),

            html.P(html.Label('Radio Items')),
            dcc.RadioItems(options=[{'label': 'New York City',
                                   'value': 'NYC'},
                                  {'label': 'Los Angels',
                                   'value': 'LA'}],
                         value='LA')
])

if __name__ == '__main__':
    app.run_server()