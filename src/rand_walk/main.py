import numpy as np
import random as rn
import walkSimulation as ws

np.seterr(all='raise')

rn.seed(0)

go = ws.Simulation(100, 100)

print(go.end_mean)
print(go.end_std)
print(go.max_dis_mean)
print(go.max_dis_std)

'''
amble = pw.ParticleWalk(100)

print(str(amble.end_point.x) + "\n" + str(amble.end_point.y) + "\n" + str(amble.end_point.z))

print(str(amble.end_point.r) + "\n" + str(amble.end_point.theta) + "\n" + str(amble.end_point.phi))

print(str(amble.max_dis))


thing = pt.Point.cartesian(1.0, 1.0, 1.0)
print(str(thing.r) + "\n" + str(thing.theta) + "\n" + str(thing.phi))

other = pt.Point.spherical(1.0, np.pi, np.pi/4)
print(str(other.x) + "\n" + str(other.y) + "\n" + str(other.z))

new = thing.add(other)
print(str(new.x) + "\n" + str(new.y) + "\n" + str(new.z))
'''