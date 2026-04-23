import numpy as np
import montecarlo # for BitString


class MonteCarlo:

    def __init__(self, ham):
        self.ham = ham
        self.N = ham.N

    def run(self, T: float, n_samples: int = 1000, n_burn: int = 100):
        beta = 1.0 / T
        conf = montecarlo.BitString(self.N)

        conf.set_integer_config(np.random.randint(0, 2 ** self.N))

        current_E = self.ham.energy(conf)

        E_samples = []
        M_samples = []

        total_sweeps = n_burn + n_samples

        for sweep in range(total_sweeps):
            for i in range(self.N):
                conf.flip_site(i)
                new_E = self.ham.energy(conf)

                dE = new_E - current_E

                if dE <= 0.0 or np.random.random() < np.exp(-beta * dE):
                    current_E = new_E
                else:
                    conf.flip_site(i)

            if sweep >= n_burn:
                spins = 2 * conf.config - 1
                M = float(np.sum(spins))
                E_samples.append(current_E)
                M_samples.append(M)

        return E_samples, M_samples
