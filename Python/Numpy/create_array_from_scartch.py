import numpy as np
#Creating array of length 10 filled with zeroes
print(np.zeros(10,dtype=int))

#Creating 3x5 floating-point array filled with 1's
print(np.ones((3,5),dtype=float))

#Creating 3x5 array filled with 3.14
print(np.full((3,5),3.14))

#Creating array using range
print(np.arange(0,20,2))

#Creating array of 5 values evenly spaced between 0 and 1
print(np.linspace(0,1,5))

#Creating 3x3 array of uniformly distributed 
#pseudorandom values between 0 and 1
print(np.random.random((3,3)))

#Creating 3x3 array of normally distributed pseudorandom
#values with mean 0 and standard deviation 1
print(np.random.normal(0,1,(3,3)))

#Creating 3x3 array of pseudorandom integers in the intervals [0,10]
print(np.random.randint(0,10,(3,3)))

#Creating a 3x3 identity matrix
print(np.eye(3))

#Creating an uninitialized array of three integers: the values will be
#whatever happens to already exist at that memory location
print(np.empty(3))

#Array can be specified using a string
print(np.zeros(10,dtype='int16'))
#Or using the associated numpy object 
print(np.zeros(10,dtype=np.int16))

 