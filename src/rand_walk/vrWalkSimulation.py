import numpy as np
import point as pt
import random as rn
from scipy.stats import norm

two_pi = 2 * np.pi


class VRSimulation:
    def __init__(self, num_sims, num_steps, match_moments):
        self.num_sims = num_sims
        self.num_steps = num_steps
        self.match_moments = match_moments
        self.points = []

        step_points = []

        for i in range(num_sims):
            step_points.append(pt.Point.cartesian(0, 0, 0))

        self.points.append(step_points)

        for step in range(num_steps):
            v_r = []
            v_theta = []
            v_phi = []

            if match_moments:
                for sim in range(num_sims):
                    v_r.append(rn.normalvariate(0, 1))
                    v_theta.append(rn.normalvariate(0, 1))
                    v_phi.append(rn.normalvariate(0, 1))

                mean_r = np.mean(v_r)
                mean_theta = np.mean(v_theta)
                mean_phi = np.mean(v_phi)

                std_r = np.std(v_r)
                std_theta = np.std(v_theta)
                std_phi = np.std(v_phi)

                for sim in range(num_sims):
                    v_r[sim] = abs((v_r[sim] - mean_r) / std_r)
                    v_theta[sim] = np.pi * norm.cdf((v_theta[sim] - mean_theta) / std_theta)
                    v_phi[sim] = two_pi * norm.cdf((v_phi[sim] - mean_phi) / std_phi)
            else:
                for sim in range(num_sims):
                    v_r.append(abs(rn.normalvariate(0, 1)))
                    v_theta.append(rn.uniform(0, np.pi))
                    v_phi.append(rn.uniform(0, two_pi))

            prev_points = step_points
            step_points = []

            for i in range(num_sims):
                inc = pt.Point.spherical(v_r[i], v_theta[i], v_phi[i])

                step_points.append(prev_points[i].add(inc))

            self.points.append(step_points)

        self.mean = np.mean([p.r for p in step_points])
        self.std = np.std([p.r for p in step_points], ddof=1)
