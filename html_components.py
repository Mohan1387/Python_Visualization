import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div(['This is the Outermost div!',
                       html.Div(['This is an inner div!'],
                                style={'color': 'red', 'border': '2px red solid', 'textAlign': 'center'}),
                       html.Div(['This is an inner div!'],
                                style={'color': 'blue', 'border': '3px blue solid', 'textAlign': 'right'})
                       ],
                       style={'color': 'green', 'border': '2px black solid'}
                       )


if  __name__ == '__main__':
    app.run_server()