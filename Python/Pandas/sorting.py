import pandas as pd 
import numpy as np
data=[1.4,3.5,2.3,1.3,7.5,8.2,np.nan]
new_data=pd.Series(data)
print(new_data.sort_values(na_position='first'))

 