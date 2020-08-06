import plotly.offline as py
from django_plotly_dash import DjangoDash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_table
import plotly.graph_objs as go

from datetime import timedelta, datetime as dt
from django.conf import settings
settings.DATA_UPLOAD_MAX_MEMORY_SIZE
import pandas

# from ...models import Corpus, Zone, Agregat

from . get_df import CorpZoneAgr


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('history', external_stylesheets=external_stylesheets)


# def select_corpuses():
#     select_corpuses = [{'label':f"Корпус {c}", 'value':c} for i in Corpus.objects.values('name_corpus') if (c:=i['name_corpus'] )]
#     select_corpuses.append({'label':'Всі корпуси', 'value':'None'})
#     return select_corpuses

# def select_zones(c):
#     select_zones = [ {'label':f"Зона {z}", 'value':z} for i in Zone.objects.filter(corpus__name_corpus=c).values('n_zone') if (z:= i['n_zone']) ]
#     select_zones.append({'label':'Всі зони', 'value':'None'})
#     return select_zones

# def select_agregats(c, z):
#     select_agregats = [ {'label':f"Агрегат {a}", 'value':a} for i in Agregat.objects.filter(n_zone__corpus__name_corpus=c, n_zone__n_zone=z).values('n_agr') if (a:=i['n_agr'])]
#     select_agregats.append({'label':'Всі агрегати', 'value':'None'})
#     return select_agregats

dict_values = {'number_of_controller': 'Номер агрегату', 
                't_input': 'Температура в приміщенні', 
                't_output': 'Температура вулиці',
                'capacity_current':'Обєм поточний',
                'w_current':'W пот.',
                'pressure':'Тиск'}

li = ['capacity_warm', 'pressure', 't_output', 't_input', 'ztime', 'zdate', 't_delta', 'capacity_warm', 'capacity_current', 'pressure', 'digital_input', 'digital_output']
list_options = [{'label': i, 'value': i} for i in li]


app.layout = html.Div([
    html.Div([
        html.Div([
            # dcc.Store(id='memory-output'),
            dcc.Store(id='memory-data'),
            
            dcc.DatePickerRange(
                id='data-picker-range',
                display_format='DD.MM.Y',
                min_date_allowed=dt(2000, 1, 1),
                max_date_allowed=dt.today(),
                end_date=(dt.today()).date(),
                start_date = dt(2001,1,1).date(),
                # start_date=(dt.today() - timedelta(days=28)).date(),
                style={
                    'display': 'block', 
                    'width': '300px' 
                },
            ),
   

            dcc.Dropdown(
                id='dropdown-three',
                # value='None',
                clearable=False,
                placeholder='Всі агрегати',
                options = [{'label':'Всі агрегати', 'value':'None'}] + [{'label':f'Агрегат {i}', 'value':f'{i}' } for i in range(1, 51)],
                value = 'None',
                style={
                    'display': 'block', 
                    'width': '200px' 
                },
            ),
        ]),
        dcc.Checklist(
            id='checklist-one',
            options = list_options,
            labelStyle={'display': 'block'},
        )
    ]),
    

    html.Div([
        dcc.Graph(
            id='graph',
            animate=True,
        ),

        dash_table.DataTable(
            id='table',
            # fixed_rows={'headers': True},
            style_table={'height': '200px', 'overflowY': 'auto'},

            
        ),
    ])
],style={'hight': 800})





@app.callback(
    # Output('dropdown-three', 'options'), 
    # [Output('memory-output', 'data'),
    Output('memory-data', 'data'),
    
    [Input('data-picker-range', 'start_date'), 
    Input('data-picker-range', 'end_date'), 
    Input('dropdown-three', 'value')])
def main(start_date, end_date, n_agregat):
    print(f'{n_agregat=}')
    print(n_agregat == 'None')
    
    if n_agregat == 'None':
        return '',
    elif isinstance(int(n_agregat), int):
        print('___________________________________________________________________________@@@@@@@')
        inst_data = CorpZoneAgr(n_agregat, start_date, end_date)
        print('INSTANCE')
        get_test = inst_data.get()
        get_test = pandas.DataFrame(get_test)
        get_test['date_time'] = get_test.zdate.astype(str) +' ' + get_test.ztime.astype(str)
        get_test['date_time'] = pandas.to_datetime(get_test['date_time'])
        
        # get_test.set_index('date_time', inplace=True)
        # get_test = get_test['date_time']
        print(get_test.date_time)
        # data_df = inst_data.get_data()
        print('GET ALREADY')
        print('START INTO DICT')
        # data = data_df.to_dict('records')
        print('END INTO DICT')
        # all_columns = data_df.columns.values.tolist()
        # print(all_columns)
        # print(data_df)
        return get_test.to_dict('records')
    # if n_corpus == 'None':
    #     return [{'label':'Всі зони', 'value':'None'}], [{'label':'Всі агрегати', 'value':'None'}], '', '', ''

    # elif ((n_corpus!='None') and (n_zone!='None')):
    #     if isinstance(n_agregat, int):
    #         inst_all_data = CorpZoneAgr(n_corpus, n_zone, n_agregat, start_date, end_date)
    #         all_data = inst_all_data.get_df()
    #         data= all_data.to_dict('records')
    #         all_data_column = all_data.columns.values.tolist()[:-2]
    #         # print(all_data_column)
    #         return select_zones(n_corpus), select_agregats(n_corpus, n_zone), f'{all_data}', all_data_column, data
            
    #     else:
    #         return select_zones(n_corpus), select_agregats(n_corpus, n_zone), '', '', ''
    # elif isinstance(n_corpus, int):
    #     return select_zones(n_corpus), [{'label':'Всі агрегати', 'value':'None'}], '', '', ''

# @app.callback(
#     Output('checklist-one', 'options'),
#     [Input('memory-data', 'data')]
# )
# def get_test(data):
#     # list_options = [{'label': i, 'value': i} for i in data_label]
#     li = ['capacity_warm', 'pressure', 't_output', 't_input', 'ztime', 'zdate', 't_delta', 'capacity_warm', 'capacity_current', 'pressure', 'digital_input', 'digital_output']
#     list_options = [{'label': i, 'value': i} for i in li]
#     print('###############################################################################')
    
#     # print(data_label)
#     # if data_label == []:
#     #     return [{'label': 'New', 'value': 'YC'}]
    
#     return list_options

@app.callback(
    [Output('table', 'data'), Output('table', 'columns')],
    [Input('checklist-one', 'value'), Input('memory-data', 'data')]
)
def get_table(value, data):
    print('SSSSSSSSSSSSSSSSSS')
    # inst_data = CorpZoneAgr(1, '2001-1-1', '2001-8-1')
    # get_data = inst_data.get()
    # get_data = pandas.DataFrame(get_data)
    print('EEEEEEEEEEEEEEEEEEEEEEEE')
    # get_data = get_data.to_dict('records')
    # print(f'{get_data=}')
    print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
    # if value == []:
    #     return [], [{'name':'name', 'id':'id'}]
    # print(f'{data}')
    # print(f'{value=}')
    if value == None:
        columns = [{'name': '', 'id':'' }]
    else:
        columns = [{'name':i, 'id':i} for i in value]
    # if not data:
    #     data = []
    # print(data)
    return data, columns

    # try:
    #     columns = [{'name':i, 'id':i} for i in value]
    #     print(columns)
    # except TypeError:
    #     print('TypeError')
    #     columns = [{'name': '', 'id':'id' }]
    # return data, columns
    

@app.callback(
    Output('graph', 'figure'),
    [Input('checklist-one', 'value'), Input('memory-data', 'data')]
)
def get_graph(value, data):
    inst_data = CorpZoneAgr(1, '2001-1-1', '2001-8-1')
    get_data = inst_data.get()
    get_data = pandas.DataFrame(get_data)
    
    layout = go.Layout(title='Graph')
                        # xaxis=dict(range=[min('0'), max('1000')]),
                        # yaxis=dict(range=[min(0), max(500)]),)
    
    data_df = pandas.DataFrame(data)
    print('fffffffffffffffffffffff')
    print(f'{data_df=}')
    print(f'{len(data_df.date_time)}')
    print(f'{len(data_df.digital_input)}')
    data = [{'x':data_df.date_time[:100], 'y':data_df[i][:100], 'name':i} for i in value]
    # data = [{'x':data_df.date_time[:17747], 'y':data_df.digital_input[:17747], 'name':'digital_input'}]
    print(data_df[['date_time', 'digital_input']])
    return {'data':data, 'layout':layout}