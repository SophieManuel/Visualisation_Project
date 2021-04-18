#%% 
import pandas as pd
import plotly.express as px  # (version 4.7.0)

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

#%%

app = dash.Dash(__name__)

###################################################
################### MY WORK #######################
###################################################

#%%

import pandas as pd
import plotly.express as px  # (version 4.7.0)

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html

import random #to fake a dataFrame
import numpy as np


from dash.dependencies import Input, Output

def colNames(dataFrame):

    """ Gets the columns names of the dataFrame and creates a dictionary 
    which will be used to plot the datas"""

    colNames = dataFrame.columns
    dict = []
    for k in colNames[2:] :
        #we create the new element of the dictionnary
        newElement = {"label":  str(k), "value": k}
        #adding it to the dict
        dict.append(newElement)
    return dict

def yearsAvailable(df):

    """ Years available  in the dataframe """

    dfYear = df["Year"].unique()
    dict = []
    for k in dfYear :
        #we create the new element of the dictionnary
        newElement = {"label":  str(k), "value": k}
        #adding it to the dict
        dict.append(newElement)
    return dict

def dataframe(year):
    """ Gets the datas related to a given year """
    dfYear = df.groupby('Year')
    dfYear.get_group(year)
    return dfYear

# %%

#### CREATION OF A FAKE DATASETS TO TEST THE CODE

#df = pd.read_csv("../data/TotalPopBySex.csv")
pays = [k for i in range(10) for k in ["FR", "EN", "USA", "CN", "IT", "AL"]]
annee = [i for i in range(2000, 2010) for k in range(6)]

ind1 = [random.randint(0, 2000) for i in range(60)]
ind2 = [random.randint(0, 2000) for i in range(60)]
ind3 = [random.randint(0, 2000) for i in range(60)]
ind4 = [random.randint(0, 2000) for i in range(60)]
ind5 = [random.randint(0, 2000) for i in range(60)]
ind6 = [random.randint(0, 2000) for i in range(60)]

M = np.array([pays, annee, ind1, ind2, ind3, ind4, ind5, ind6], order = 'F')
df = pd.DataFrame(np.transpose(M))
df.columns = ['Country', 'Year', 'Ind1', 'Ind2', 'Ind3', 'Ind4', 'Ind5', 'Ind6']


# %%
# ------------------------------------------------------------------------------
# App layout
app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Choropleth Map", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_indic",
                 options=colNames(df),
                 multi=False,
                 value = df.columns[2],
                 style={'width': "40%"}
                 ),

                 html.Br(),

    dcc.Dropdown(id="slct_year",
                 options = yearsAvailable(df),
                 multi=False, #on ne peut pas faire plusieurs choix
                 value=2005,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),

    html.Br(),

    dcc.Graph(id='myChoroMap', figure={})

])

@app.callback(
    [Output(component_id='output_container', component_property='children'), 
    Output(component_id='myChoroMap', component_property='figure')],
    [Input(component_id='slct_year', component_property='value'), 
    Input(component_id='slct_indic', component_property='value')]
)

def update_graph(slct_year, slct_indic):
    #print(slct_year, slct_indic)

    #print(type(slct_year, slct_indic))

    container = "The year chosen by user was: {}".format(slct_year)
    print(container)
    dfYear = dataframe(slct_year)

    fig = px.choropleth(
        data_frame=dfYear,
        locationmode='ISO-3',
        locations='Country',
        scope = 'world',
        color = str(slct_indic),
        hover_data=['Country', str(slct_indic)],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={slct_indic: 'personnes'},
        template='plotly_dark'
    )

    #print(type(container), type(fig2))
    return fig
# %%

#%%

if __name__ == '__main__':
    app.run_server(debug=False)

# %%


#%%


