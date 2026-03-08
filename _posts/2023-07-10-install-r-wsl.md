---
layout: post
title:  "R in WSL"
image: assets/images/wsl2.png
---

Installing R on Windows Subsystem for Linux (WSL) allows you to leverage the statistical power of R within a Linux environment. This guide provides the commands to set up R-base using the CRAN repository.

## Installation Commands

Run the following commands in your WSL terminal:

```bash
# 1. Update and upgrade package lists
sudo apt update && sudo apt upgrade -y

# 2. Install essential dependencies and build tools
sudo apt install -y build-essential libcurl4-openssl-dev libssl-dev libxml2-dev libicu-dev

# 3. Add the CRAN repository
# Note: Ensure the repository name matches your Ubuntu version (focal, jammy, etc.)
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'

# 4. Install R-base
sudo apt update
sudo apt install -y r-base
```

---

### Verifying the Installation
Once installed, you can launch the R console by typing:
```bash
R
```
This environment is now ready for installing R packages and performing statistical analysis.