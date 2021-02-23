import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Start the app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

quakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

fig = go.Figure(go.Densitymapbox(lat=quakes.Latitude, lon=quakes.Longitude, z=quakes.Magnitude, radius=10))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

app.layout = html.Div(children=[
    html.H1('Tesseract'),
    html.Div(className="worldmap", children=[
        dcc.Graph(className="worldmap", figure=fig)
    ]),
    dbc.FormGroup(
        [
            dbc.Label("Slider", html_for="slider"),
            dcc.Slider(id="slider", min=0, max=10, step=0.5, value=3),
        ]
)
])

if __name__ == '__main__':
    app.run_server(debug=True)