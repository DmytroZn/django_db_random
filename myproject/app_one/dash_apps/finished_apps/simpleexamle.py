import plotly.offline as py
from django_plotly_dash import DjangoDash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from datetime import datetime as dt

from ...models import Corpus, Zone, Agregat


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('simpleexamle', external_stylesheets=external_stylesheets)


def select_corpuses():
    select_corpuses = [{'label':f"Корпус {c}", 'value':c} for i in Corpus.objects.values('name_corpus') if (c:=i['name_corpus'] )]
    select_corpuses.append({'label':'Всі корпуси', 'value':'None'})
    return select_corpuses

def select_zones(c):
    select_zones = [ {'label':f"Зона {z}", 'value':z} for i in Zone.objects.filter(corpus__name_corpus=c).values('n_zone') if (z:= i['n_zone']) ]
    select_zones.append({'label':'Всі зони', 'value':'None'})
    return select_zones

def select_agregats(c, z):
    select_agregats = [ {'label':f"Агрегат {a}", 'value':a} for i in Agregat.objects.filter(n_zone__corpus__name_corpus=c, n_zone__n_zone=z).values('n_agr') if (a:=i['n_agr'])]
    select_agregats.append({'label':'Всі агрегати', 'value':'None'})
    return select_agregats


app.layout = html.Div([
    html.Div([
        dcc.DatePickerRange(
            id='data-picker-range',
            min_date_allowed=dt(2018, 1, 1),
            max_date_allowed=dt.today(),
        ),

        dcc.Dropdown(
            id='dropdown-one',
            options=select_corpuses(),        
            value='None',
            clearable=False,
        ),
        
        dcc.Dropdown(
            id='dropdown-two',
            # value='None',
            clearable=False,
            placeholder='Всі зони',
            # optionHeight=20,
        ),

        dcc.Dropdown(
            id='dropdown-three',
            # value='None',
            clearable=False,
            placeholder='Всі агрегати',
        ),

        html.Div(id='testone'),

    ]),
  
])


@app.callback(
    [Output('dropdown-two', 'options'), Output('dropdown-three', 'options')],
    [Input('dropdown-one', 'value'), Input('dropdown-two', 'value'), Input('dropdown-three', 'value')])
def update_output(n_corpus, n_zone, n_agregat):
    if n_corpus == 'None':
        return [{'label':'Всі зони', 'value':'None'}], [{'label':'Всі агрегати', 'value':'None'}]
    elif (n_corpus!='None') and (n_zone!='None'):
        return select_zones(n_corpus), select_agregats(n_corpus, n_zone)
    elif isinstance(n_corpus, int):
        return select_zones(n_corpus), [{'label':'Всі агрегати', 'value':'None'}]
