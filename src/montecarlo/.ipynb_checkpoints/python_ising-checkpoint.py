import numpy as np
import networkx as nx
import montecarlo as montecarlo

class IsingHamiltonian:

    def __init__(self, G: nx.Graph):
        self.G = G
        self.N = G.number_of_nodes()
        # Default: zero external field
        self.mu = np.zeros(self.N)

    def set_mu(self, mus: np.ndarray):
        self.mu = np.array(mus, dtype=float)

    def energy(self, config: montecarlo.BitString) -> float:
        spins = 2 * config.config - 1
        E = 0.0
        for i, j, data in self.G.edges(data=True):
            J = data.get('weight', 1.0)
            E += J * spins[i] * spins[j]   # antiferromagnetic convention
        E -= np.dot(self.mu, config.config) # mu couples to bit occupations {0,1}
        return E

    def compute_average_values(self, T: float):
        beta = 1.0 / T

        conf = montecarlo.BitString(self.N)

        # Accumulators (use log-sum-exp for numerical stability)
        energies = np.zeros(2 ** self.N)
        magnetisations = np.zeros(2 ** self.N)

        for idx in range(2 ** self.N):
            conf.set_integer_config(idx)
            spins = 2 * conf.config - 1

            energies[idx] = self.energy(conf)
            magnetisations[idx] = float(np.sum(spins))

        # Boltzmann weights with log-sum-exp for stability
        log_weights = -beta * energies
        log_Z = _logsumexp(log_weights)
        log_probs = log_weights - log_Z          # log P(config)
        probs = np.exp(log_probs)                # P(config)

        E  = float(np.dot(probs, energies))
        M  = float(np.dot(probs, magnetisations))
        E2 = float(np.dot(probs, energies ** 2))
        M2 = float(np.dot(probs, magnetisations ** 2))

        HC = (E2 - E ** 2) / (T ** 2)
        MS = (M2 - M ** 2) / T

        return E, M, HC, MS


# ── helpers ────────────────────────────────────────────────────────────────

def _logsumexp(a: np.ndarray) -> float:
    a_max = np.max(a)
    return float(a_max + np.log(np.sum(np.exp(a - a_max))))