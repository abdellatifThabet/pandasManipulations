import pandas as pd
import numpy as np
import math
import os

def compute_score():
    print("in this script you have to set two arguments the first one is the path to the original csv file and the second argument is the path to the rarity file")
    print("type path to original csv file")
    patho = input()
    print("type path to file contains rarity scores")
    pathr = input()
    dfo = pd.read_csv(patho, index_col=[0])
    dfr = pd.read_csv(pathr, index_col=[0])            
    dfo['total_score'] = np.nan
    index = 0
    for row in dfo.iterrows():
        score = 0
        for col in range(3,len(dfo.columns)-1):
            if(str(row[1][col]) == 'nan'):
                continue
            else:
                col_name = dfo.columns[col]
                col_value = row[1][col]
                score = score + float(dfr.loc[(dfr.trait_type == col_name)&(dfr.value == str(col_value)), 'rarity'])
        dfo.loc[row[0],'total_score'] = score
        index = index+1
    
    head, tail = os.path.split(patho)
    dfo.to_csv(head+"final_"+tail)
    return

if __name__ == "__main__":
    compute_score()