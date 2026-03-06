# Modification of columns
# Assigning a column that does not exist will create a new column.
import pandas as pd
import numpy as np
data={"year":[2022,2021,2080,2024,2056,2080],
      "hours":[1.4,3.5,2.3,1.3,7.5,8.2]
      }
frame=pd.DataFrame(data)
print(frame)
#Coulmn can be modified by assignment.
#the empty debt column could be assigned a scalar value or an array of values
frame['debt']=23.5
print(frame)
#Array of values
frame['date']=[11,13,23,10,1,9]
print(frame)

#Note- When you are assigning lists or arrays to a column, the value's length must match the length of DataFrame
frame["Numbers"]=np.arange(6.)
print(frame)

frame['double_hours'] = frame['hours'] * 2
print(frame)

frame['Bool']=frame['year']==2080
print(frame)
