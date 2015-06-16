# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 01:09:07 2015

@author: Wasit
"""
#http://stackoverflow.com/questions/13983876/adding-hetrogenous-timeseries-to-a-dataframe
import pandas as pd

xl57 = pd.ExcelFile('../../data/AG-RW-CM51-57.xlsx')
xl58 = pd.ExcelFile('../../data/AG-RW-CM51-5805.xlsx')

table57_1=xl57.parse(xl57.sheet_names[0],index_col='Day',na_values='-')
table58_1=xl58.parse(xl58.sheet_names[0],index_col='Day',na_values='-')

#dataframe concatenation
table1=pd.concat([table57_1,table58_1])

table1.SumAlgae[1:].plot(logy=True,legend=True)
table1.Turbidity[1:].plot(legend=True,secondary_y=True)
table1.pH[1:].plot(legend=True,secondary_y=True)
table1.Conductivity[1:].plot(legend=True,secondary_y=True)