import numpy as np
#  1️⃣ np.ones()
# This function creates a new array filled with 1s, based on a shape you provide
d=np.ones((3,2),dtype=float)
print(d)



# 2️⃣ np.ones_like()
# This creates a new array of 1s with the same shape and dtype as another array.
a = np.array([[5,6,7],
              [8,9,10]])

b = np.ones_like(a)
print(b)

 