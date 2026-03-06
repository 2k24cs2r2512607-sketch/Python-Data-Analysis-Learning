# In pandas, a DataFrame works like a dictionary of columns.
import pandas as pd
data={"state":["UP","MP","Maharastra","Rajasthan","Pune","Patna"],
      "year":[2022,2021,2000,2024,2056,2080],
      "pop":[1.4,3.5,2.3,1.3,7.5,8.2]
      }
new_data=pd.DataFrame(data)
print(new_data)
#Specifying a sequence of columns
seq=pd.DataFrame(data,columns=["year","pop","state"])
print(seq)
 
 #If you a pass a column that is not contained in dictionary, it will appear with missing value
frame=pd.DataFrame(data,columns=["pop","state","debt"])
print(frame)
#NanN=not a number or null

#Getting the column name
print(frame.columns)