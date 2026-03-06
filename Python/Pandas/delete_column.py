import pandas as pd
 
data={"state":["Ohio","Ohio","Ohio","Nevada","Nevada","Nevada"],
      "pop":[1.4,3.5,2.3,1.3,7.5,8.2]
      }
frame=pd.DataFrame(data)
frame['eastern']=frame['state']=="Ohio"
print(frame)
# del method use to delete a column
del frame['eastern']
print(frame.columns)