#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Calculating the Hydrophobic_occupancy
import MDAnalysis as mda
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Change these to match your GROMACS output files
topology_file = "you_topology_file.gro"
trajectory_file = "your_trajectory_file.xtc"

# Change these to match your selection strings for GPCR and the ligand
gpcr_selection = "resid 1:last and not (name H* or type O)"
ligand_selection = "resid 1:last"

# Load the GROMACS output files into MDAnalysis
universe = mda.Universe(topology_file, trajectory_file)

# Select the GPCR and ligand atoms
gpcr_atoms = universe.select_atoms(gpcr_selection)
ligand_atoms = universe.select_atoms(ligand_selection)

# Calculate the hydrophobic interactions between GPCR and ligand
cutoff_distance = 4.0  # Cutoff distance

# Store all residue pairs interacting in each frame
interacting_residue_pairs = []

# Iterate through trajectory frames (up to 2000 frames)
max_frames = 2000
frames_to_process = min(max_frames, len(universe.trajectory))

for frame in range(frames_to_process):
    universe.trajectory[frame]

    # Calculate distance matrix between GPCR and ligand atoms
    distance_matrix = np.linalg.norm(gpcr_atoms.positions[:, np.newaxis] - ligand_atoms.positions, axis=2)

    # Find the residue pairs with distances less than the cutoff
    residue_pairs = np.argwhere(distance_matrix < cutoff_distance)

    if residue_pairs.size > 0:
        for pair in residue_pairs:
            gpcr_residue = gpcr_atoms[pair[0]].resid
            ligand_residue = ligand_atoms[pair[1]].resid
            interacting_residue_pairs.append((gpcr_residue, ligand_residue))

# Calculate the occupancy of hydrophobic interactions
interaction_counts = Counter(interacting_residue_pairs)
occupancy = {pair: (count / frames_to_process) * 100 for pair, count in interaction_counts.items()}

# Sort residue pairs by occupancy in descending order
sorted_occupancy = sorted(occupancy.values(), reverse=True)

# Generate a histogram
plt.hist(sorted_occupancy, bins=20, range=(0, 100), edgecolor='black')
plt.xlabel("Hydrophobic Interaction Occupancy (%)")
plt.ylabel("Number of Residue Pairs")
plt.title("Hydrophobic Interaction Occupancy Distribution for 2000 Frames")
plt.tight_layout()
plt.show()

# Save results to a dat file
with open("hydrophobic_occupancy.dat", "w") as outfile:
    outfile.write("Residue Pair (GPCR, Ligand)\tOccupancy (%)\n")
    for pair, occupancy_percentage in occupancy.items():
        outfile.write(f"{pair[0]}, {pair[1]}\t{occupancy_percentage:.2f}\n")

print("Results saved to hydrophobic_occupancy.dat.")

