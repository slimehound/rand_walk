import numpy as np
import particleWalk as pw

np.seterr(all='raise')

amble = pw.ParticleWalk(100)

print(str(amble.end_point.x) + "\n" + str(amble.end_point.y) + "\n" + str(amble.end_point.z))

print(str(amble.end_point.r) + "\n" + str(amble.end_point.theta) + "\n" + str(amble.end_point.phi))

'''
thing = pt.Point.cartesian(1.0, 1.0, 1.0)
print(str(thing.r) + "\n" + str(thing.theta) + "\n" + str(thing.phi))

other = pt.Point.spherical(1.0, np.pi, np.pi/4)
print(str(other.x) + "\n" + str(other.y) + "\n" + str(other.z))

new = thing.add(other)
print(str(new.x) + "\n" + str(new.y) + "\n" + str(new.z))
'''