import os, json
import pandas as pd
import numpy as np
import glob
import re

pd.set_option('display.max_columns', None)
temp = pd.DataFrame()
def jsons_df(path_to_json):
    file_list = []
    num_files = len(glob.glob(path_to_json + "*.json"))
    print(num_files)
    for i in range(1,num_files+1):
        file_list.append(path_to_json + str(i) + '.json')
    
    data = []
    for cpt, file in enumerate(file_list):
        try:
            with open(file,'r') as f:
                sample = json.loads(f.read())
                sample['id'] = cpt+1
                data.append(sample)
        except:
            continue
        # Flattening JSON data
    normalized = pd.json_normalize(
        data, 
        record_path =['attributes'], 
        #meta=['class', 'room', ['info', 'teachers', 'math']],
        meta=['name', 'image','description','id' ],
        errors='ignore'
    )
    last_df = normalized.pivot_table(values='value', index=normalized.index, columns='trait_type', aggfunc='first')
    
    result_svs = pd.concat([normalized[['name','description','image','id']], last_df], axis=1)
    result_svs = result_svs.groupby(['name'], as_index=False).first()
    result_svs = result_svs.set_index('id')
    return result_svs

result_svs = jsons_df('svs/svs_json/')
result_uni = jsons_df('uni/uni_json/')
result_js = jsons_df('json/')

result_svs.to_csv('result_svs.csv')
result_uni.to_csv('result_uni.csv')
result_js.to_csv('result_js.csv')

