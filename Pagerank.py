## Numpy library for matrix and vector manipulation
import numpy as np ## Link matrix
L = np.array([[0,1/2,0,0], [1/3, 0, 0, 1/2], [1/3, 0, 0, 1/2], [1/3, 1/2, 1, 0]])## Rank Matrix
r = np.array([1/4,1/4,1/4,1/4])
print("i A B C D") ## Print the link vector
## Looping over Link matrix And Rank vector.
for i in range(30):
 print(i, round(r[0],2), round(r[1], 2), round(r[2], 2), round(r[3],2))
 r = L@r
