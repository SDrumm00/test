# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import glob
import pandas as pd

def concatenate(inpath=r'C:\Users\scott\OneDrive\Desktop\test', outfile=r'C:\Users\scott\OneDrive\Desktop\test'):
    # find the directory where the CSV files are based upon the above variables
    file_list = glob.glob(os.path.join(inpath, '*.csv'))
    # create empty dataframe
    dflist = []
    # column name variables based on data structure
    colnames = ['Column1']

    # loop through files in stated directory
    for filenames in file_list:
        print(filenames) # status of loading gets printed here
        # create the new dataframe for each individual file being loaded
        df = (pd.read_csv(filenames))
        # append the individual files together into 1 file
        dflist.append(df)
    concatdf = pd.concat(dflist, axis=0)
    concatdf.columns = colnames
    concatdf.to_csv(outfile, index=None)
    #print(concatdf)
    print('Job Complete')
    

    
