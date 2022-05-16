import dash
from dash import dcc
from dash import html
from os.path import dirname, join

current_dir = dirname(__file__)
tz_map_1_path = join(current_dir, "tz_map_1.html")
tz_map_2_path = join(current_dir, "tz_map_2.html")

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1('Tanzania Map'),
    html.H1(file_path),
    html.Iframe(id = 'map', srcDoc = open(tz_map_2_path).read(), width='100%', height='600')
])

if __name__ == "__main__":
    app.run_server(debug=True)