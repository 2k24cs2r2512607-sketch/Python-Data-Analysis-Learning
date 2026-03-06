import pandas as pd
data={"state":["UP","MP","Maharastra","Rajasthan","Pune","Patna"],
      "year":[2022,2021,2000,2024,2056,2080],
      "pop":[1.4,3.5,2.3,1.3,7.5,8.2]
      }
#head() method selects only the first five rows
new_data=pd.DataFrame(data)
print(new_data.head())
 