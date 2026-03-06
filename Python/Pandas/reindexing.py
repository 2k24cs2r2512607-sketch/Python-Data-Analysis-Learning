import pandas as pd
import numpy as np
# Re-Index = Creating a new object with values arranged to align with new Index.
obj=pd.Series(['a','b','c','d','e'],index=[1,3,5,6,7])
print(obj)
#Reindexing
obj2=obj.reindex(index=[3,4,5,6,7])
print("-------------------------------------------")
print(obj2)

''''For ordered data like time series, 
You may want to do interpolation or filling of values when rendering.
Methods such as - ffill => Forward fills the values
while bfill=>fills backward'''
object=pd.Series(["blue","purple","yellow"])
print(object.reindex(np.arange(6),method="bfill"))
print("-------------------------------------------")
frame=pd.DataFrame(np.arange(9).reshape((3,3)),
                   index=["a","c","d"],
                   columns=["Ohio","Texas","California"])
print(frame)
print("-------------------------------------------")
#Reindexing
frame2=frame.reindex(index=["a","b","c","d"])
print(frame2)
print("-------------------------------------------")
#The Column can be reindexed with the column keyword:
states=["Texas","Europe","California"]
print(frame2.reindex(columns=states))
print("-------------------------------------------")

#You can also reindex by using the loc operator. This work only if all of the new index labels already exist in the dataframe
print(frame2.loc[["a","b","c"],["California","Texas"]])
