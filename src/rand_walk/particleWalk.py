import numpy as np
import point as pt
import random as rn

two_pi = 2*np.pi


class ParticleWalk:
    def __init__(self, num_steps):
        self.num_steps = num_steps
        pres = pt.Point()
        self.path = [pres]

        for i in range(num_steps):
            inc = pt.Point.spherical(abs(rn.normalvariate(0, 1)), rn.uniform(0, np.pi), rn.uniform(0, two_pi))
            pres = pres.add(inc)
            self.path.append(pres)

        self.end_point = pres
