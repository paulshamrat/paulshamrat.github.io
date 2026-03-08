---
layout: post
title:  "Install NGS on Ubuntu 20.04"
image: assets/images/ngs2.png
---
A guide for installing Next-Generation Sequencing (NGS) tools on Ubuntu 20.04 LTS. This post documents the steps taken during my setup process.

## Installation Procedure

### 1. Linux (Ubuntu) Distribution
Start with a laptop or desktop running a Debian-based Linux distribution (e.g., Ubuntu 20.04 LTS).

### 2. Anaconda
Anaconda is a popular Python distribution that simplifies package management. While Ubuntu comes with Python by default, it's recommended to use a modern version like Python 3.8.

1. **Download:** Visit the official [Anaconda website](https://www.anaconda.com/products/individual) to download the Linux installer.
2. **Select Installer:** Choose the "64-Bit (x86) Installer".
3. **Install:** The installer will be a `.sh` file (e.g., `Anaconda3-2020.11-Linux-x86_64.sh`). Open your terminal and run:
   ```bash
   bash ~/Downloads/Anaconda3-2020.11-Linux-x86_64.sh
   ```
4. **Initialize:** Once the installation is complete, initialize Anaconda by running:
   ```bash
   conda init
   ```
5. **Open Navigator (Optional):** To use the graphical interface, run:
   ```bash
   anaconda-navigator
   ```

You can find the full installation guide [here](https://docs.anaconda.com/anaconda/install/linux/).

### 3. SRA Tools with Bioconda
Bioconda is a channel for the conda package manager specializing in bioinformatics software. To install `sra-tools`, run:
```bash
conda install -c bioconda sra-tools
```
Note: This might install an older version. It is often recommended to specify a newer version or use a specific label if required:
```bash
conda install -c bioconda/label/cf201901 sra-tools
```
Refer to the [Bioconda documentation](https://anaconda.org/bioconda/sra-tools) for more details.

**Managing Conda Environments:**
- Check for the `(base)` prompt in your terminal.
- **Activate:** `conda activate`
- **Deactivate:** `conda deactivate`

### 4. FastQC
FastQC is used for quality control checks on raw sequence data.

1. **Prerequisite:** Ensure Java is installed. Check with:
   ```bash
   java -version
   ```
   If Java is not installed, follow a guide like [this one](https://phoenixnap.com/kb/how-to-install-java-ubuntu) to install it.
2. **Install FastQC:**
   Run the following command:
   ```bash
   sudo apt update
   sudo apt install -y fastqc
   ```
