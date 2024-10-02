import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output

# Inicializa la app de Dash
app = dash.Dash(__name__)

# Datos de ejemplo
df = px.data.gapminder()

# Gráfico de ejemplo
fig = px.line(df[df['country'] == 'Canada'], x='year', y='gdpPercap', title='GDP per Capita de Canadá')

# Layout de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Dashboard con Plotly y Dash'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Ejecutar el servidor
if __name__ == '__main__':
    app.run_server(debug=True)
