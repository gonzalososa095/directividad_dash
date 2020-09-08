# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:44:dash49 2020

@author: Gonzalo Sosa
"""



import plotly.express as px
import dash
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc


df = pd.read_csv('data.csv')




app = dash.Dash(__name__,
external_stylesheets=[dbc.themes.LUX])
server = app.server


app.layout = html.Div([
    dbc.Row(dbc.Col(html.H5("Gonzalo Sosa", style={'text-align': 'center'}),width={'size':4,'offset':8})),
    dbc.Row(dbc.Col(html.H6("Data Scientist", style={'text-align': 'center'}),width={'size':4,'offset':8})),
    dbc.Row(dbc.Col(html.H1("Directividad parlante B&D 6MD38",),width={'size':8,'offset':3})),
    dbc.Row(dbc.Col((html.H4("Angulo")),width={'size':True,'offset':5})),
    dbc.Row(dbc.Col(daq.Gauge(
        id='knob',
        color="#42ADDC",
             value = 0,
        label=' ',
             min = -135,
             max= 135,
             scale={'start':-135,'labelInterval':45,'interval':1},
            theme = 'Light',
    showCurrentValue = True),width={'size':3,'offset':4},align='end'),justify='start'),
    dbc.Row(dbc.Col(dcc.Slider(
        id='slider',
        min=-90,
        max=90,
        step=10,
        value=0),width={'size':5,'offset':3})),
    dbc.Row(dbc.Col(dcc.Graph(id='rta', figure={}),width={'size':10,'offset':1}))
    ])

@app.callback([
    Output('knob', 'value'),
    Output('rta','figure')],
    [Input('slider', 'value')]
)
def update_output(value):

    dff = df.copy()

    fig = px.line(dff, x="Frecuencia", y=str(value),log_x=True,labels={str(value):'Amplitud',"Frecuencia":'Frecuencia [Hz]'},template = 'presentation')
    #template = 'plotly_dark'
    return value,fig


if __name__ == '__main__':
    app.run_server(debug=True)