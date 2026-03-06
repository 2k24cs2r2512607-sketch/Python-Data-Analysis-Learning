import pandas as pd
import numpy as np
# The drop method will return a new object with the indicated values deleted from an axis
obj=pd.Series(np.arange(5),index=['a','b','c','d','e'])
print(obj)
print("-------------------------------------------")
print(obj.drop("c"))
