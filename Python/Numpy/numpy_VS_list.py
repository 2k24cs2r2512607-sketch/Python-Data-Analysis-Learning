import numpy as np 
my_arr=np.arange(1_000_000)
my_list=list(range(1_000_000))
%timeit my_arr2=my_arr*2
%timeit my_arr3=my_list*2
