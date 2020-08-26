import numpy as np
import random as rn
import walkSimulation as ws

np.seterr(all='raise')

rn.seed(0)

end_means = []

for i in range(10):
    go = ws.Simulation(1000, 100)

    gem = f"{go.end_mean:.4f}"
    ges = f"{go.end_std:.4f}"
    gfm = f"{go.furthest_mean:.4f}"
    gfs = f"{go.furthest_std:.4f}"
    print(f'end mean/std {gem} / {ges}   -   furthest mean/std {gfm} / {gfs}')

    end_means.append(go.end_mean)

seed_std = np.std(end_means, ddof=1)
print(f'seed std: {seed_std:.4f}')

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