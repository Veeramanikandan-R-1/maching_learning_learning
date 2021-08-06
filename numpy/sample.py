import numpy as np
array1=np.array([1,2,3,3,4,5,6,6])
filtered_array=[]
for i in array1:
    if(i>4):
        filtered_array.append(True)
    else:
        filtered_array.append(False)
new_arr=array1[filtered_array]
print(new_arr)
print(filtered_array)

