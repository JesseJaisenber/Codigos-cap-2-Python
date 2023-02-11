import numpy as np

numbers=np.array(["1,2,3,4,5,6,7,8"])

print(numbers)
print(numbers.shape)

print(numbers.ravel())
print(numbers.T)
print(numbers.T.ravel())

print(numbers.reshape(8,1))

print(np.arrange(18).reshape(6,3))
print(np.arrange(18).reshape(3,6))

mas_numbers=np.array(["9,10,11,12,13,14"])
print(mas_numbers.reshape(-1,3))
print(mas_numbers.reshape(3,-1))
print(mas_numbers.reshape(4,-1))

