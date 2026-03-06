import pandas as pd
data={"year":[2022,2021,2000,2024,2056,2080],
      "day":[1,3,2,1,7,8]
      }
frame=pd.DataFrame(data)
print(frame.loc[1])
print(frame.iloc[1])