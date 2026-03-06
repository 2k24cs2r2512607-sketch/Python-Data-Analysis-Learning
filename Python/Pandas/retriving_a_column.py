import pandas as pd
data={"state_1":["UP","MP","Maharastra","Rajasthan","Pune","Patna"],
      "year":[2022,2021,2000,2024,2056,2080],
      "pop":[1.4,3.5,2.3,1.3,7.5,8.2]
      }
frame=pd.DataFrame(data)
print(frame["state_1"])#Works in every case
print(frame.state_1)
'''only works when column name is valid and 
if a column name contain's white spaces or symbols other than underscore 
then it raise a error'''