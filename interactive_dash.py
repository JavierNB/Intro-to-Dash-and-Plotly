from dash import Dash, dcc, Output, Input  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
mytext = dcc.Markdown(children='') # as this is Markdown you can use that language freely
myinput = dbc.Input(value="# Hello World - let's build web apps in **Python** [check this link](https://www.google.com)!")

# Customize your own Layout
app.layout = dbc.Container([mytext, myinput])

# Callback allows components to interact
@app.callback(
    Output(mytext, component_property='children'),
    Input(myinput, component_property='value')
)
def update_title(user_input):  # function arguments come from the component property of the Input
    return user_input  # returned objects are assigned to the component property of the Output


# Run app
if __name__=='__main__':
    app.run_server(port=8052)
