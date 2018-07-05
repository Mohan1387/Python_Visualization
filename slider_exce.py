import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output


app = dash.Dash('wheels Image app')
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


app.layout = html.Div([
            dcc.RangeSlider(id='slider-input',
                            min=-10,
                            max=10,
                            value=[-2, 4],
                            marks={i:str(i) for i in range(-10, 11)}),

            html.H1(id='multiply')

],style={'width': '80%', 'float': 'left'})


@app.callback(Output(component_id='multiply', component_property='children'),
              [Input(component_id='slider-input', component_property='value')])
def update_output_div(slider_range):
    return "Multiplied : {}".format(str(slider_range[0]*slider_range[1]))


if __name__ == '__main__':
    app.run_server(debug=True)