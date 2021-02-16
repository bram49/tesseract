import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import folium

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Start the app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1('Tesseract'),
    html.Iframe(id='map',
                srcDoc = open('base_map.html', 'r').read(),
                width= '100%',
                style={'height':'80vh'}),
    dbc.FormGroup(
        [
            dbc.Label("Slider", html_for="slider"),
            dcc.Slider(id="slider", min=0, max=10, step=0.5, value=3),
        ]
)
])

if __name__ == '__main__':
    app.run_server(debug=True)