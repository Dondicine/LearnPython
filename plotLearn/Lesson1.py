import numpy as np

# method 1

# arr1 = np.zeros(5)

# arr2 = np.zeros([5,3],dtype=int)

# print("arr1 = ", arr1)

# print("arr2 = ", arr2)

# method 2

# arr1 = np.array([0,1,2])

# arr2 = np.array([[0, 1, 2],
# [3, 2, 1],
# [-1, -2, -3],
# [0, 0, 0]])

# print("arr1 = ", arr1)

# print("arr2 = ")
# print(arr2)

# print(arr2.shape, arr2.shape[0], arr2.shape[1])


# method 3

# arr1 = np.arange(0, 10.001, 0.5)
# print(arr1)

# mehod 4

arr1 = np.linspace(0, 10, 11, endpoint=False)

print(arr1)