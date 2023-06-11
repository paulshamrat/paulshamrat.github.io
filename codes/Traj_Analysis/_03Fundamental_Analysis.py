# RMSD
import MDAnalysis as mda
from MDAnalysis.analysis import rms
import matplotlib.pyplot as plt

# load the trajectories and topologies
u1 = mda.Universe('/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_wt/1AKI_solv_ions.gro', '/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_wt/md_0_1.xtc')
u2 = mda.Universe('/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_g210v/1AKI_solv_ions.gro', '/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_g210v/md_0_1.xtc')

# select the protein atoms for RMSD calculation
ref1 = u1.select_atoms('protein')
ref2 = u2.select_atoms('protein')

# calculate the RMSD
R1 = rms.RMSD(u1, ref1, select='backbone', groupselections=['protein'])
R1.run()
R2 = rms.RMSD(u2, ref2, select='backbone', groupselections=['protein'])
R2.run()

# plot the RMSD
fig, ax = plt.subplots()
ax.plot(R1.rmsd[:,1], R1.rmsd[:,2], label='1cqf_g62t_wt')
ax.plot(R2.rmsd[:,1], R2.rmsd[:,2], label='1cqf_t62g_mut')
ax.legend()
ax.set_xlabel('Time (ps)')
ax.set_ylabel('RMSD (Å)')

# save the plot as a PNG file
plt.savefig('rmsd_plot_230425.png', dpi=300)

# show the plot
plt.show()


# rmsf ca
import MDAnalysis as mda
from MDAnalysis.analysis import rms
from MDAnalysis.analysis.rms import RMSF
import matplotlib.pyplot as plt

# Load the two trajectory and topology files
u1 = mda.Universe('/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_wt/1AKI_solv_ions.gro', '/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_wt/md_0_1.xtc')
u2 = mda.Universe('/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_g210v/1AKI_solv_ions.gro', '/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_g210v/md_0_1.xtc')

# Select the C-alpha atoms
calpha1 = u1.select_atoms('protein and name CA')
calpha2 = u2.select_atoms('protein and name CA')

# Align the protein to the reference structure
ref1 = mda.Universe('/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_wt/1AKI_solv_ions.gro')
ref2 = mda.Universe('/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_g210v/1AKI_solv_ions.gro')
R1 = rms.RMSD(u1, ref1, select='protein and name CA', center=True, superposition=True)
R1.run()
R2 = rms.RMSD(u2, ref2, select='protein and name CA', center=True, superposition=True)
R2.run()

# Calculate RMSF for each trajectory
RMSF1 = RMSF(calpha1).run()
RMSF2 = RMSF(calpha2).run()

# Plot RMSF values of both trajectories on the same plot
fig, ax = plt.subplots()
ax.plot(RMSF1.rmsf, label='wild type')
ax.plot(RMSF2.rmsf, label='mutant')
ax.set_xlabel('Residue')
ax.set_ylabel('RMSF (nm)')
ax.legend()

# Set the y-axis limits based on the range of your RMSF values
ymin = 0
ymax = max(RMSF1.rmsf.max(), RMSF2.rmsf.max()) + 0.1
ax.set_ylim(ymin, ymax)

# Save the plot as a high-resolution PNG image
fig.savefig('rmsf_ca_230425.png', dpi=300)

plt.show()


# RG
import MDAnalysis as mda
import numpy as np
import matplotlib.pyplot as plt

# Load the trajectory and topology files for both systems
u1 = mda.Universe('/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_wt/1AKI_solv_ions.gro', '/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_wt/md_0_1.xtc')
u2 = mda.Universe('/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_g210v/1AKI_solv_ions.gro', '/content/gdrive/MyDrive/works/psmb8/3unf/3unf-palmetto/3unf_g210v/md_0_1.xtc')

# Select only protein atoms
protein_sel1 = u1.select_atoms('protein')
protein_sel2 = u2.select_atoms('protein')

# Initialize arrays to store Rg values and time
Rg1 = np.zeros(len(u1.trajectory))
Rg2 = np.zeros(len(u2.trajectory))
time1 = np.zeros(len(u1.trajectory))
time2 = np.zeros(len(u2.trajectory))

# Loop over all frames in trajectory and calculate Rg
for ts in u1.trajectory:
    Rg1[ts.frame] = protein_sel1.radius_of_gyration()
    time1[ts.frame] = u1.trajectory.time

for ts in u2.trajectory:
    Rg2[ts.frame] = protein_sel2.radius_of_gyration()
    time2[ts.frame] = u2.trajectory.time

# Plot Rg values of both systems on the same plot
fig, ax = plt.subplots()
ax.plot(time1, Rg1, label='wild type')
ax.plot(time2, Rg2, label='mutant')
ax.set_xlabel('Time (ps)')
ax.set_ylabel('Radius of gyration (nm)')
ax.legend()

# Save the plot as a high-resolution PNG image
fig.savefig('rg_230425.png', dpi=300)

plt.show()
