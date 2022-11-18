from dash import Dash, dcc               # Si no esta disponible usa: pip install dash
import dash_bootstrap_components as dbc  # Si no esta disponible usa: pip install dash-bootstrap-components

## Dash

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
mytext = dcc.Markdown(children="**Dash** es un *framework* para realizar aplicaciones web interactivas con gráficas y controles vinculados.")

# Customize your own Layout
app.layout = dbc.Container([mytext])

# Run app
if __name__=='__main__':
    app.run_server(port=8051)
