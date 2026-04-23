import numpy as np
import montecarlo # for BitString


class MonteCarlo:
    """
    Metropolis Monte Carlo sampler for an IsingHamiltonian.

    Parameters
    ----------
    ham : IsingHamiltonian
        The Ising Hamiltonian that defines the energy landscape.
    """

    def __init__(self, ham):
        self.ham = ham
        self.N = ham.N

    def run(self, T: float, n_samples: int = 1000, n_burn: int = 100):
        """
        Run the Metropolis algorithm and return sampled energies and magnetizations.

        Parameters
        ----------
        T        : float  – temperature (in natural units where k_B = 1)
        n_samples: int    – number of MC sweeps to *record* after burn-in
        n_burn   : int    – number of MC sweeps to discard as burn-in

        Returns
        -------
        E_samples : list[float]  – energy at each recorded sweep
        M_samples : list[float]  – magnetization at each recorded sweep

        Algorithm
        ---------
        Each "sweep" consists of one attempted spin-flip per site (N flips).
        For a proposed flip at site i:
          - Compute ΔE = E(β) − E(α).
          - Accept with probability min(1, exp(−ΔE / T)).
        """
        beta = 1.0 / T
        conf = montecarlo.BitString(self.N)

        # Initialise to a random configuration
        conf.set_integer_config(np.random.randint(0, 2 ** self.N))

        current_E = self.ham.energy(conf)

        E_samples = []
        M_samples = []

        total_sweeps = n_burn + n_samples

        for sweep in range(total_sweeps):
            # One sweep = attempt one flip per site
            for i in range(self.N):
                # Propose a flip at site i
                conf.flip_site(i)
                new_E = self.ham.energy(conf)

                dE = new_E - current_E

                # Metropolis acceptance criterion
                if dE <= 0.0 or np.random.random() < np.exp(-beta * dE):
                    # Accept: keep the flipped configuration
                    current_E = new_E
                else:
                    # Reject: flip back
                    conf.flip_site(i)

            # Record after burn-in
            if sweep >= n_burn:
                # Magnetization = N_up − N_down = 2*N_up − N
                spins = 2 * conf.config - 1
                M = float(np.sum(spins))
                E_samples.append(current_E)
                M_samples.append(M)

        return E_samples, M_samples