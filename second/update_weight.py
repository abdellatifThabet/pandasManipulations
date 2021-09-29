import pandas as pd
import numpy as np
import math
import os

def update_weight():
    print('this script aims to update a weight of certain value ! ')
    print('please enter the file path : ')
    path_to_file = input()
    print("type value name you want to change its weight: ")
    val = input()
    print("type the new weight value :")
    weight = int(input())
    df = pd.read_csv(path_to_file, index_col=[0])
    total = df['id'].nunique()
    df.loc[df['value'] == val, 'weight'] = weight
    for index in range(0, len(df)):
        if(str(df.iloc[index]['value']) == 'nan'):
            continue
        else:
            df.at[index,'rarity'] = (total/df.iloc[index]['count'])*df.iloc[index]['weight']


    df['rarity'] = df['rarity'].astype('float64').round(2) 
    df = df.set_index('id')
    df.to_csv(path_to_file)
    return

if __name__ == "__main__":
    update_weight()