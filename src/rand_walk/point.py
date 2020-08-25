import numpy as np


class Point:
    x = 0.0
    y = 0.0
    z = 0.0
    r = 0.0
    theta = 0.0
    phi = 0.0

    @staticmethod
    def cartesian(x, y, z):
        result = Point()
        result.x = x
        result.y = y
        result.z = z

        try:
            result.r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
        except Exception:
            pass

        try:
            result.theta = np.arctan(y / x)
        except Exception:
            pass

        try:
            result.phi = np.arccos(z / result.r)
        except Exception:
            pass

        return result

    @staticmethod
    def spherical(r, theta, phi):
        result = Point()
        result.r = r
        result.theta = theta
        result.phi = phi
        result.x = r * np.sin(theta) * np.cos(phi)
        result.y = r * np.sin(theta) * np.sin(phi)
        result.z = r * np.cos(theta)
        return result

    def add(self, inc):
        return Point.cartesian(self.x + inc.x,
                               self.y + inc.y,
                               self.z + inc.z)
