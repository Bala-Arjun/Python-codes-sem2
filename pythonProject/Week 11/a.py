import numpy as np
import time
size = 1000000
start = time.time()
list1 = [i for i in range(size)]
list2 = [i for i in range(size)]
result_list = [list1[i] + list2[i] for i in range(size)]
end = time.time()
print("Time taken using list:", end - start)
start = time.time()
arr1 = np.arange(size)
arr2 = np.arange(size)
result_array = arr1 + arr2
end = time.time()
print("Time taken using NumPy:", end - start)
