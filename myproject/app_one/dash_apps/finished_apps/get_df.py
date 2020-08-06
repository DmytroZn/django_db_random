import requests
import json
from pandas import DataFrame as df
import pandas as pd
from ... models import MaAgregate

class CorpZoneAgr:
    def __init__(self, agregat, start_date, end_date):
        self.agregat = str(agregat)
        self.start_date = start_date
        self.end_date = end_date

    def get_data(self):
        response = requests.get(
            'http://' + '0.0.0.0:8000/v1/' + 'get-agr/' + self.agregat + 
            '/' + self.start_date + 'and' + self.end_date + '/')
        if response.status_code == 200:
            res = response.json()
        else:
            res = []
        return res

    def get_df(self):
        res = df(self.get_data())
        print(f'{res=}')
        # res['id_zone'] = df(res['id_zone'].values.tolist(), columns=['zdate', 'ztime'])
        # try:
        
        # except KeyError:
        #     # print(dir(res))
        # if res.size==0:
        #     pass
        # else:
        #     print('something error with dataframe')
        #     pass
        return res

    def get(self):
        obj = MaAgregate.objects.filter(number_of_controller=self.agregat, 
                                    zdate__gte=self.start_date,
                                    zdate__lte=self.end_date )
        return obj.values()
        # http://0.0.0.0:8001/getcorpzonearg/23/1/1/2019-08-08and2019-10-18/
        
# ins = CorpZoneAgr(1, '2019-08-08', '2019-10-18')
# y = ins.get_data()
# z = ins.get_df()
# print(z)