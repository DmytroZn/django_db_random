import plotly.offline as py
# import dash
from django_plotly_dash import DjangoDash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from datetime import datetime as dt

# from '/../models' import *
from ...models import Corpus, Zone, Agregat
# from . models import  Zone, Corpus, Agregat

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('simpleexamle', external_stylesheets=external_stylesheets)

select_corpuses = [{'label':f"Корпус {c}", 'value':c} for i in Corpus.objects.values('name_corpus') if (c:=i['name_corpus'] )]
select_corpuses.append({'label':'Всі корпуси', 'value':'None'})
select_test = [{'label':'1', 'value':'None'}]
print(f'{select_corpuses=}')
# select_corpuses = [(f"Корпус {i['name_corpus']}", f"Корпус {i['name_corpus']}") for i in Corpus.objects.values('name_corpus')]

# opt_1 = [{'label':'Вибрати всі зони', 'value':'choice_all'},
#         {'label':'1', 'value':'1'},
#         {'label':'2', 'value':'2'},]
# select_zones = [ {'label':f"Зона {z}", 'value':z} for i in Zone.objects.filter(corpus__name_corpus=23).values('n_zone') if (z:= i['n_zone']) ]

def select_zones(c):
    select_zones = [ {'label':f"Зона {z}", 'value':f'{c}-/-{z}'} for i in Zone.objects.filter(corpus__name_corpus=c).values('n_zone') if (z:= i['n_zone']) ]
    select_zones.append({'label':'Всі зони', 'value':'None'})
    return select_zones

def select_agregats(cz):
    c = int(cz.split('-/-')[0])
    z = int(cz.split('-/-')[1])
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
            options=select_corpuses,        
            # value=select_corpuses[0]['value'],
            # persisted_props = ['None'],
            clearable=True,

        ),
        
        dcc.Dropdown(
            id='dropdown-two',
            options=select_test,        

            # value=select_test[0]['value'],
            clearable=True,
            placeholder='Всі зони',

        ),

        dcc.Dropdown(
            id='dropdown-three',
            # options= select_test if (2+2==4) else select_test,        

            # value='None',
            clearable=True,
            placeholder='Всі агрегати',


        ),

        html.Div(id='testone'),

    ]),
  
])


@app.callback(
    Output('dropdown-two', 'options'),
    [Input('dropdown-one', 'value')])
def update_output(n_corpus):
    print(n_corpus)
    if n_corpus == 'None':
        return [{'label':'Всі зони', 'value':'None'}]
    else:
        return select_zones(n_corpus)
    # return [{'label':'Всі зони', 'value':'None'}]



@app.callback(
    [Output('dropdown-three', 'options'), Output('testone', 'children')],
    [Input('dropdown-two', 'value')])
def update_outpt2(n_zone):
    if n_zone=='None':
        return [{'label':'Всі агрегати', 'value':'None'}], 'aaa'
    else:
        return select_agregats(n_zone), 'a'
            
    # return [{'label':'Всі агрегати', 'value':'None'}], 'aaa'








# if __name__ == "__main__":
#     app.run_server(debug=True)

# 0636025877

# 0969014046