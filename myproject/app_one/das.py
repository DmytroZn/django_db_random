import plotly.offline as py
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from datetime import datetime as dt


# from . models import  Zone, Corpus, Agregat

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# select_corpuses = [(f"Корпус {a}", a) for i in Corpus.objects.values('name_corpus') if (a := i['name_corpus'] )]
# select_corpuses.append(('Всі корпуси', None))
# select_corpuses = [(f"Корпус {i['name_corpus']}", f"Корпус {i['name_corpus']}") for i in Corpus.objects.values('name_corpus')]

opt_1 = [{'label':'Вибрати всі зони', 'value':'choice_all'},
        {'label':'1', 'value':'1'},
        {'label':'2', 'value':'2'},]

one111111111111 = [
        {'label':'Вибрати всі агрегати', 'value':'voice_all'},
        {'label':'1', 'value':'1'},
        {'label':'1', 'value':'1'},
        ]

one222222222222 = [
        {'label':'Вибрати всі агрегати', 'value':'voice_all'},
        {'label':'2', 'value':'2'},
        {'label':'2', 'value':'2'},
        ]

fal = [
        {'label':'all', 'value':'all'},
        ]

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.DatePickerRange(
                id='data-picker-range',
                min_date_allowed=dt(2018, 1, 1),
                max_date_allowed=dt.today(),
                style={ 
                'display': 'block', 
                'width': '300px' 
                },

            ),

            dcc.Dropdown(
                className='li',
                id='dropdown-one',
                options=opt_1,        
                value=None,
                clearable=False,
                style={ 
                'display': 'block', 
                'width': '200px' 
                },        ),
            
            dcc.Dropdown(
                className='li',
                options=one111111111111,        

                id='dropdown-two',
                value='ff',
                style={ 
                'display': 'block', 
                'width': '200px' 
                },

            ),

            dcc.Dropdown(
                className='li',
                options=opt_1,        

                id='dropdown-three',
                value='ff',
                style={ 
                'display': 'block', 
                'width': '200px' 
                },        ),
        
            
            

            

        ], style={	
                'display':'flex',
                'justify-content':'space-around',
                # 'height': '100px',
                # # 'display': 'inline-block',
                # 'width': '100%'
                    },),
    ]),
    
    html.Div(id='testone'),
])


@app.callback(
    Output('dropdown-two', 'options'),
    [Input('dropdown-one', 'value')])
def update_output(value1):
    print(value1)
    if value1 == '1':
        return one222222222222
    else:
        return fal



@app.callback(
    [Output('dropdown-three', 'options'), Output('testone', 'children')],
    [Input('dropdown-two', 'value')])
def update_outpt2(value2):
    # print(value1)
    if value2=='1':
        return one222222222222, 'f'
    elif value2 == '2':
        print()
        return one222222222222, 152
    return fal, '15' if value2 == '2' else 'f'








if __name__ == "__main__":
    app.run_server(debug=True)

# 0636025877

# 0969014046