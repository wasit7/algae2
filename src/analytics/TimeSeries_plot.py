# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 01:09:07 2015

@author: Wasit
"""

import pandas as pd
#from matplotlib import pyplot as plt
xl = pd.ExcelFile('../../data/AG-RW-CM51-57.xlsx')
#xl.sheet_names  # see all sheet names
table1=xl.parse(xl.sheet_names[0],index_col='Day',na_values='-')  # read a specific sheet to DataFrame
#table1.convert_objects(convert_numeric=True)

#plt.plot(table1.index,table1.SumAlgae)
#plt.yscale('log')
table1.SumAlgae[1:].plot(logy=True,legend=True)
table1.Turbidity[1:].plot(legend=True,secondary_y=True)
table1.pH[1:].plot(legend=True,secondary_y=True)
table1.Conductivity[1:].plot(legend=True,secondary_y=True)
table1.Anabaena[1:].plot(logy=True,legend=True)