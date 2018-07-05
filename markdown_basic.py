import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

markdown_text = ''' this a test'''

app.layout = html.Div([
            dcc.Markdown(children=markdown_text)

])

if __name__ == '__main__':
    app.run_server()