import numpy as np
import random as rn
import walkSimulation as ws
import vrWalkSimulation as vws

np.seterr(all='raise')

rn.seed(0)

end_means = []

print("Simple method")
print("=============\n")

for i in range(10):
    go = ws.Simulation(100, 100)

    gem = f"{go.end_mean:.4f}"
    ges = f"{go.end_std:.4f}"
    gfm = f"{go.furthest_mean:.4f}"
    gfs = f"{go.furthest_std:.4f}"
    print(f'end mean/std {gem} / {ges}   -   furthest mean/std {gfm} / {gfs}')

    end_means.append(go.end_mean)

seed_std = np.std(end_means, ddof=1)
print(f'seed std: {seed_std:.4f}')

print("\n\nComplex method, no vr")
print("=====================\n")

rn.seed(0)
end_means = []

for i in range(10):
    no_vr = vws.VRSimulation(100, 100, False)
    gem = f"{no_vr.mean:.4f}"
    ges = f"{no_vr.std:.4f}"
    print(f'end mean/std {gem} / {ges} ')
    end_means.append(no_vr.mean)

seed_std = np.std(end_means, ddof=1)
print(f'seed std: {seed_std:.4f}')

print("\n\nComplex method, with vr")
print("=======================\n")

rn.seed(0)
end_means = []

for i in range(10):
    no_vr = vws.VRSimulation(50, 100, True)
    gem = f"{no_vr.mean:.4f}"
    ges = f"{no_vr.std:.4f}"
    print(f'end mean/std {gem} / {ges} ')
    end_means.append(no_vr.mean)

seed_std = np.std(end_means, ddof=1)
print(f'seed std: {seed_std:.4f}')