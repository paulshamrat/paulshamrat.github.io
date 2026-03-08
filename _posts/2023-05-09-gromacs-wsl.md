---
layout: post
title:  "Install GROMACS on WSL"
author: paulshamrat
image: assets/data/rmsd-1aki.svg
---

# Install GROMACS on Windows

Running GROMACS on Windows has never been easier thanks to the Windows Subsystem for Linux (WSL). This guide will walk you through the process of setting up a Linux environment and installing GROMACS for molecular dynamics simulations.

## Step 1: Activate Windows Subsystem for Linux (WSL)

To enable WSL on your Windows machine:

1. **Search for Features:** Click the Windows button and search for "Turn Windows features on or off".
2. **Enable WSL:** Locate and check **Windows Subsystem for Linux**.
3. **Optional:** It is also highly recommended to enable **Virtual Machine Platform**.
4. **Restart:** Click OK and restart your computer when prompted to apply the changes.

*Tip:* On Windows 11, you can simply open PowerShell as Administrator and run:
```powershell
wsl --install
```

## Step 2: Install Ubuntu from the Microsoft Store

1. Open the [Microsoft Store](https://www.microsoft.com/store).
2. Search for **Ubuntu 20.04 LTS** (or a more recent version like 22.04 LTS).
3. Click **Install**. Once finished, launch Ubuntu and follow the prompts to create your user account.

## Step 3: Install GROMACS

Open your Ubuntu terminal and run the following commands to update your system and install the necessary dependencies and GROMACS:

```bash
# Update package lists and upgrade existing packages
sudo apt update && sudo apt upgrade -y

# Install build tools and GROMACS
sudo apt install -y build-essential gcc cmake libfftw3-dev gromacs
```

### Verification
Once the installation is complete, verify that GROMACS is working by checking its version:
```bash
gmx -version
```

---

**Summary**
You now have a functional GROMACS installation on your Windows machine, combining the ease of Windows with the power of Linux for scientific computing.