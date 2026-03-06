'''Pandas's Index Objects are responsible for holding the axis labels (Including a Data Frame's column names) and 
other metadata (like the axis names).
Any array or other sequence of labels you use when constructing a Series/Dataframe is internally converted to and index'''
import pandas as pd
import numpy as np
obj=pd.Series(np.arange(3),index=['a','b','c'])
index=obj.index
print(index)
# Index Objects are immutable-cannot be modified by User
'''
index[2]='c' - Type Error
Advantage - Immutability makes it safer to share Index Objects among Data Structures
'''
_Indexes_=pd.Index(np.arange(3))
objects=pd.Series(['A','B','C'],index=_Indexes_)
print(objects)

print(objects.index is _Indexes_)
print(4 in objects.index)

# A Pandas Index can contain duplicate labels
new_obj=pd.DataFrame(['Apple',"banana","Grapes"],index=[1,1,1])
# Selection with Duplicate labels will select all occurrences of that label
print(new_obj)