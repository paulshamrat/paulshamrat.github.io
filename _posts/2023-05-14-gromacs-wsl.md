---
layout: post
title:  "Install GROMACS on WSL"
image: assets/images/wsl2.png
---
A quick summary of the commands required to install GROMACS on Windows Subsystem for Linux (WSL).

## Technical Summary

Run the following commands in your Ubuntu terminal:

```bash
# Update and upgrade system packages
sudo apt update && sudo apt upgrade -y

# Install build dependencies
sudo apt install -y gcc cmake build-essential libfftw3-dev

# Install GROMACS
sudo apt install -y gromacs
```

## Detailed Explanation

1. **Update and Upgrade:** Ensures your package manager has the latest information and that existing software is up to date.
2. **GCC & Build-Essential:** Installs the necessary compilers and tools required for scientific software.
3. **CMake:** A cross-platform build system used by GROMACS.
4. **libfftw3-dev:** The Fastest Fourier Transform in the West (FFTW) library, which is essential for GROMACS performance.
5. **GROMACS:** The final command installs the GROMACS package itself.

Check your installation by running:
```bash
gmx -version
```


