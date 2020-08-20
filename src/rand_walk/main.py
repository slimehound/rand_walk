import random
import numpy as np
import matplotlib.pyplot as plt
import point

'''
class Point:
    r = 1
    theta = random.randrange(0, 20 * np.pi, 1) / 10
    phi = random.randrange(0, 10 * np.pi, 1) / 10

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
'''

f = point.CartesianPoint(1, 1, 1)
s = point.SphericalPoint(2, 0, 0)
t = f.add_to(s)

print(t.x)
print(t.y)
print(t.z)
