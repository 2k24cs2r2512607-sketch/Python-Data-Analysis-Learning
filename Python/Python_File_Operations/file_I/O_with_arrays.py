import numpy as np
arr=np.arange(10)
#Saving the file
#Arrays are saved by default in an uncompressed raw binary format with file extension.npy
np.save("some_array",arr)
#Loadiing the file
arch=np.load("some_array.npy")
print(arch)