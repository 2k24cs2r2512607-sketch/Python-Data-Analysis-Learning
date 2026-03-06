import pandas as pd
import numpy
data={"Ohio":{2000:1.5,2001:1.7,2002:3.6,2005:9.3},
      "Nevada":{2001:2.4,2002:2}}
frame=pd.DataFrame(data)
# If nested Dictionary passed to the DataFrame, pandas will interpret the outer dictionary keys as the columns, and the inner keys as row indices
print(frame)
# Tranpose the DataFrame (swap rows and columns)
# Note : Transposing discrads the column data types 
print(frame.T)

# The keys in inner directions are combined to form the index in result
new_frame=pd.DataFrame(frame,index=[2000,2001,2003])
print(new_frame)

# Dictionaries of Series are treated in much the same way-
pdata={"Ohio":frame["Ohio"][:-1],
       "Nevada":frame["Nevada"][:2]}
print(pd.DataFrame(pdata))
print(frame.to_numpy())