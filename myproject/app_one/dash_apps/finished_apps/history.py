import plotly.offline as py
from django_plotly_dash import DjangoDash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
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



dict_values = {'number_of_controller': 'Номер агрегату', 
                't_input': 'Температура в приміщенні', 
                't_output': 'Температура вулиці',
                'capacity_current':'Обєм поточний',
                'w_current':'W пот.',
                'pressure':'Тиск'}

li = ['capacity_warm', 'pressure', 't_output', 't_input', 'ztime', 'zdate', 't_delta', 'capacity_current', 'pressure', 'digital_input', 'digital_output']
list_options = [{'label': i, 'value': i} for i in li]


app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Store(id='memory-label'),
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
        html.Div([

            html.Div([
                dcc.Checklist(
                    id='checklist-one',
                    # options = [{'label': 'i', 'value': 'i'} ],
                    labelStyle={'display': 'block', 'margin': '10px 10px', 'border-top': '1px solid #333'},
                    style={'border': '1px solid #333'},
                ),
                html.Button('Submit', id='submit-val', n_clicks=0)
            # ], style={'margin': '10px 10px', }
            ]),
            
            dcc.Markdown(id='p-test', style={'line-height': '4px', 'margin-top':'-7px'}),
        ], style={'display':'flex','justify-content':'start'},),

        html.Table([
            html.Tbody([
                html.Tr([
                    html.Td(children='a', style={'border': '1px solid #333'}), 
                    html.Td(children='a', style={'border': '1px solid #333', 'padding': '10px 10px'})
                ]),
                html.Tr([
                    html.Td(children='g'), 
                    html.Td(children='a', style={'border': '1px solid #333', 'padding': '10px 10px'})
                ]),                
                html.Tr([
                    html.Td([dcc.Checklist(id='ddd', options = [{'label': 'i8', 'value': 'i'}, {'label': 'i', 'value': 'i7'} ] )]), 
                    html.Td(children='a', style={'border': '1px solid #333', 'padding': '10px 10px'})
                ])
            ])
            # html.Td(children=value)
        ], style={ 
                    'border-collapse': 'collapse',
                    'border': '2px solid rgb(100, 100, 100)',
                    # 'letter-spacing': '1px',
                    # 'font-family': 'sans-serif',
                    # 'font-size': '.7rem'
                    })
    ]),
    
    
    
    html.Div([
        # dcc.Graph(
        #     id='graph',
        #     animate=True,
        # ),
        dcc.Loading(
            id='loading-1',
            type='cube',
            children=dcc.Graph(id='graph', animate=True,)
        ),

        dash_table.DataTable(
            id='table',
            # fixed_rows={'headers': True},
            style_table={'height': '200px', 'overflowY': 'auto'},


            
        ),
    ])
],style={'hight': 800})





@app.callback(
    [Output('memory-data', 'data'), Output('memory-label', 'data')],
    
    [Input('data-picker-range', 'start_date'), 
    Input('data-picker-range', 'end_date'), 
    Input('dropdown-three', 'value')])
def main(start_date, end_date, n_agregat):

    
    if n_agregat == 'None':
        return '', []
    elif isinstance(int(n_agregat), int):
        # print('___________________________________________________________________________@@@@@@@')
        inst_data = CorpZoneAgr(n_agregat, start_date, end_date)
        # print('INSTANCE')
        # get_test = inst_data.get_df()
        get_test2 = inst_data.get_data()
        # get_test2[0]
        # get_test['date_time'] = get_test.zdate.astype(str) +' ' + get_test.ztime.astype(str)
        # get_test['date_time'] = 
        
        # print(get_test.date_time)
        # print('GET ALREADY')
        # print('START INTO DICT')
        # print('END INTO DICT')
        print('start 2')
        get_ind2 = [{'label': i, 'value': i} for i in get_test2[0]]
        print('end 2')

        # print('start 1 ')
        # get_ind = [{'label': i, 'value': i} for i in get_test.columns]
        # print('end 1')
        return get_test2, get_ind2
        # return get_test.to_dict('records'), get_ind


@app.callback(
    Output('checklist-one', 'options'),
    [Input('dropdown-three', 'value')]
)
def get_test(value):
    # list_options = [{'label': 'i', 'value': 'i'} ]
    print(f'{value=}')
    if value == None:
        # return list_options
        return []
    elif value == '1':
        return list_options
    else:
        return []


@app.callback(
    [Output('table', 'data'), Output('table', 'columns')],
    [Input('submit-val', 'n_clicks'), Input('memory-data', 'data')],
    [State('checklist-one', 'value')] #Input('checklist-one', 'value')
)
def get_table(n_clicks, data, value):
    print(f'{n_clicks}')
    if value == None:
        columns = [{'name': '', 'id':'' }]
    else:
        columns = [{'name':i, 'id':i} for i in value]
    return data, columns
    

@app.callback(
    Output('graph', 'figure'),
    [Input('submit-val', 'n_clicks'), Input('memory-data', 'data')],
    [State('checklist-one', 'value')]
)
def get_graph(n_clicks, data, value ):    
    print('Load start')
   
    layout = go.Layout(title='Graph')
                        # xaxis=dict(range=[min('0'), max('1000')]),
                        # yaxis=dict(range=[min(0), max(500)]),)

    data_df = pandas.DataFrame(data)
    if data == None:
        data = [{'x':[0], 'y':[0], 'name':''}]
    elif (value != None) and data:
        data = [{'x':data_df.zdate, 'y':data_df[i], 'name':i} for i in value]
        # data = [{'x':data_df.date_time, 'y':data_df[i], 'name':i} for i in value]
    else:
        data = [{'x':[0], 'y':[0], 'name':''}]
    print('Load end')
    return {'data':data, 'layout':layout}

@app.callback(
    Output('p-test', 'children'),
    [Input('submit-val', 'n_clicks'), Input('graph', 'hoverData')],
    [State('checklist-one', 'value')]
)
def send_res(n_clicks, hoverData, value):
    print(f'{value=}')

    if hoverData == []:
        return ''
    t = [(f"{dict_values.get(value[i.get('curveNumber')], value[i.get('curveNumber')]  )} - {i.get('y')} \n") for i in hoverData['points'] ]
    t.append(f"Дата та час {hoverData['points'][0]['x']}")
    return t

    #     v = value.get('points')[0].get('y')
    #     return v
    # else:
    #     return ''


    # if hoverData == []:        
    #     return ''
    # t = [(f"{dict_values.get(value[i.get('curveNumber')], value[i.get('curveNumber')]  )} - {i.get('y')} \n") for i in hoverData['points'] ]
    # t.append(f"Дата та час {hoverData['points'][0]['x']}")
    # return t



