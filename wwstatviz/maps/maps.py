#%% 
import pandas as pd
import plotly.express as px  # (version 4.7.0)

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

#%%

app = dash.Dash(__name__)

# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv(".csv")

df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df[:5])
#%%
# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

#créer dictionnaire des années = liste [{"label": "2015", "value": 2015}, {"label": "2015", "value": 2015}, ...]

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018}],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])

#%%
# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='valYear'), 
    Input(component_id='slct_indic', component_property='valIndic')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))


    container = "Year chosen: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    dff = dff[dff["Affected by"] == "Varroa_mites"]

    fig = px.bar(
        data_frame=dff,
        x='State',
        y='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
    )

    return container, fig

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)


####### MY WORK
#%%

import pandas as pd
import plotly.express as px  # (version 4.7.0)

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

def colNames(dataFrame):

    """ Gets the columns names of the dataFrame and creates a dictionary 
    which will be used to plot the datas"""

    colNames = dataFrame.columns
    dict = []
    for k in colNames :
        #we create the new element of the dictionnary
        newElement = {"label":  str(k), "value": k}
        #adding it to the dict
        dict.append(newElement)
    return dict


# %%

df = pd.read_csv("./data/FertilityByAge.csv")

#%%
# ------------------------------------------------------------------------------
# App layout
app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

#créer dictionnaire des années = liste [{"label": "2015", "value": 2015}, {"label": "2015", "value": 2015}, ...]

    dcc.Dropdown(id="slctIndic",
                 options=colNames(df),
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),

    dcc.Dropdown(id="slctYear",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018}],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slctYear', component_property='valYear'), 
    Input(component_id='slctIndic', component_property='valIndic')]
)

def update_graph(valYear, valIndic):
    print(valYear)
    print(type(valIndic))

    container = "The year chosen by user was: {}".format(valYear)

    return container, fig

#%%

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=False)


# %%
