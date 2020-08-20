import numpy as np


class Point:
    x = 0
    y = 0
    z = 0
    r = 0
    theta = 0
    phi = 0

    def add_to(self, incremental_point):
        return CartesianPoint(self.x + incremental_point.x,
                              self.y + incremental_point.y,
                              self.z + incremental_point.z)


class CartesianPoint(Point):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.r = np.sqrt(x ^ 2 + y ^ 2 + z ^ 2)
        self.theta = np.arctan(y / x)
        self.phi = np.arccos(z / self.r)


class SphericalPoint(Point):
    def __init__(self, r, theta, phi):
        self.r = r
        self.theta = theta
        self.phi = phi
        self.x = r * np.sin(theta) * np.cos(phi)
        self.y = r * np.sin(theta) * np.sin(phi)
        self.z = r * np.cos(theta)
