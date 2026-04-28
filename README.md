# montecarlo

A Monte Carlo simulation package for Ising models.

* [GitHub](https://github.com/PaladinBIGDan2077/QS1_Sp26_MonteCarlo/) | [Documentation](https://monte-carlo-danieljlomis.readthedocs.io/en/latest/index.html)
* Created by [Daniel J. Lomis](https://www.lomisco.net) | GitHub [@PaladinBIGDan2077](https://github.com/PaladinBIGDan2077) 
* MIT License

## Features

* **BitString** — lightweight representation of spin configurations over N sites, with methods for flipping sites, counting on/off bits, and converting to/from integers
* **IsingHamiltonian** — graph-based Ising model defined via a `networkx.Graph` with weighted edges; supports external magnetic fields (µ) and exact thermodynamic averages (energy, magnetization, heat capacity, magnetic susceptibility) via full enumeration
* **MonteCarlo** — Metropolis–Hastings sampler that efficiently approximates thermodynamic averages for large systems where exact enumeration is intractable; supports configurable burn-in and sample count

## Documentation

Documentation is built with Sphinx and deployed to ReadTheDocs.

* **Live site:** [https://monte-carlo-danieljlomis.readthedocs.io](https://monte-carlo-danieljlomis.readthedocs.io/en/latest/)

Docs deploy automatically on push to `main` via GitHub Actions.

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/QS1_Sp26_MonteCarlo.git
cd montecarlo
```

## Author

montecarlo was created in 2026 by Daniel J. Lomis.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
