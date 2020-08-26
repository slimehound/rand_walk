import numpy as np
import particleWalk as pw


class Simulation:
    def __init__(self, num_sims, num_steps):
        self.num_sims = num_sims
        self.num_steps = num_steps
        self.walks = []

        for i in range(num_sims):
            curr = pw.ParticleWalk(num_steps)
            self.walks.append(curr)

        self.end_mean = np.mean([w.end_point.r for w in self.walks])
        self.end_std = np.std([w.end_point.r for w in self.walks], ddof=1)
        self.furthest_mean = np.mean([w.furthest_point.r for w in self.walks])
        self.furthest_std = np.std([w.furthest_point.r for w in self.walks], ddof=1)
