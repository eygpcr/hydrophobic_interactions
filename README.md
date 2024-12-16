# Hydrophobic_interactions

## Project Description
The study of interactions between ligands and receptors is crucial for understanding molecular recognition and binding mechanisms, which are fundamental to drug discovery and biophysics. Among these interactions, hydrophobic interactions play a significant role in stabilizing ligand-receptor complexes and facilitating binding specificity.

This project provides a Python-based framework to analyze hydrophobic interactions in molecular dynamics (MD) simulations. By leveraging **MDAnalysis** and other computational tools, the code identifies residues on both the ligand and receptor that contribute to hydrophobic interactions. Furthermore, it calculates the interaction occupancy, providing insights into the frequency and stability of these interactions over the course of the simulation.

The methodology focuses on identifying residue pairs within a specified cutoff distance, calculating their interaction occupancy as a percentage of the total simulation time, and presenting the results in a comprehensive histogram. This tool can be applied to:
- **Ligand-GPCR systems** for studying binding mechanisms.
- **General protein-ligand complexes** to assess interaction dynamics.
- **Simulation-based analyses** to quantify hydrophobic contributions in biomolecular systems.

By enabling residue-level insights, this framework helps researchers understand key molecular interactions and design experiments or computational models for further investigation.
---

## Essential Tools
- **GROMACS Output Files** (`.gro`, `.xtc`)
- **Python**
- **MDAnalysis**
- **NumPy**
- **Matplotlib**
- **Google Colab**


---

## Installation Steps
1. Prepare **GROMACS** output files:
   - `topology_file.gro`
   - `trajectory_file.xtc`
2. Load these files into the script using **MDAnalysis**.
3. Run the script to calculate hydrophobic interactions between GPCR and ligand residues.

---

## Features
- Identify hydrophobic interactions between ligands and GPCRs.
- Calculate the occupancy (%) of hydrophobic interactions throughout the simulation.
- Generate a histogram to visualize the distribution of interaction occupancy.

---

## Usage

### Calculating the Hydrophobic Interaction Occupancy
To calculate the hydrophobic interaction occupancy, use the following resources:

- **Google Colab Notebook:** [Open in Colab](https://colab.research.google.com/github/eygpcr/hydrophobic_interactions/blob/main/hydrophobic_interaction_occupancy.ipynb)
- **Python Script:** [Download hydrophobic_occupancy.py](https://github.com/eygpcr/hydrophobic_interactions/raw/main/hydrophobic_occupancy.py)

---

## Contribution
We welcome contributions to this project! Here's how you can contribute:

1. **Fork** the repository.
2. Clone your fork to your local machine:
   ```bash
   git clone https://github.com/eygpcr/hydrophobic_interactions.git

---

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this project under the terms of the license.
