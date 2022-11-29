import numpy as np
import matplotlib.pyplot as plt


def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

size = 10
matrix = np.zeros((size, size, 3), dtype="uint8")
assert matrix.shape[0] == matrix.shape[1]

color1 = [255, 128, 0]
color2 = [0, 128, 255]

    

v=0
coef=0.01/(size/50)
for k in range(size*2):
    v+=coef
    r = lerp(color1[0], color2[0], v)
    g = lerp(color1[1], color2[1], v)
    b = lerp(color1[2], color2[2], v)
    for j in range(min(k, size - 1), -1, -1):
        i = k - j
        if i < size:
            matrix[i][j]= [r, g, b]
plt.figure(1)
plt.imshow(matrix)
plt.show()
