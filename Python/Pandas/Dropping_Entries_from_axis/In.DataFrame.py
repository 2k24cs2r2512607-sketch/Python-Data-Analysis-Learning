#With DataFrame index values can be deleted from either axis or column
import pandas as pd
import numpy as np
obj=pd.DataFrame(np.arange(16).reshape(4,4),index=['Ohio','Colordo','Utah','New York'],
                 columns=["one","two","Three","Four"])
print(obj)
print("-------------------------------------------")
#Calling drop with a sequence of labels will drop values from row labels
data=obj.drop(index=["Ohio","Utah"])
print(data)
print("-------------------------------------------")
#To drop labels from columns, use columns Keyword
delete_column=obj.drop(columns=["two"])
print(delete_column)
#Dropping values from column by passing axis=1 or axis=columns
print("-------------------------------------------")
new_data=obj.drop("Ohio",axis="index")
print(new_data)
new_data=obj.drop("two",axis="columns") #or new_data=obj.drop("two",axis=1)
print(new_data)



 
