---
layout: post
title:  "Install GROMACS on WSL"
author: paulshamrat
image: assets/data/rmsd-1aki.svg
---

# Install GROMACS on Windows

Are you interested in running GROMACS, the popular molecular dynamics simulation software, on your Windows machine? Good news! You can easily set it up using the Windows Subsystem for Linux (WSL). In this blog post, we will guide you through the installation process step by step.

## Activating Windows Subsystem for Linux

To begin, we need to activate the Windows Subsystem for Linux. Follow these steps:

1. Click on the Windows button located in the bottom left corner of your screen.
2. In the search bar, type "Turn Windows features on or off" and double-click on the corresponding option that appears.
3. Scroll down the list of features and locate "Windows Subsystem for Linux." It is recommended to also enable the virtual machine feature.
4. Checkmark the option for "Windows Subsystem for Linux."
5. Click "OK" to save the changes.
6. A prompt to restart your computer will appear. Restart your computer to apply the changes.

With the Windows Subsystem for Linux activated, we can proceed to install Ubuntu on your Windows machine.

## Installing Ubuntu 20.04 LTS

1. Open the Microsoft Store on your Windows machine.
2. Search for "Ubuntu 20.04 LTS" and select the option to install it.
3. Follow the on-screen instructions to complete the installation. Once installed, you will have Ubuntu available as a command-line interface on your Windows machine.

Now that we have Ubuntu installed, we can proceed with installing GROMACS.

## Alternatively follow this to install Ubuntu on WSL
To install WSL (Windows Subsystem for Linux) on Windows 11, you can follow these steps:
1. Open PowerShell as an administrator. 
2. Right-click on the  Start button and select "Windows PowerShell (Admin)".
3. Enable the Windows Subsystem for Linux feature by running the following command:

```
wsl --install
```
## Installing GROMACS

1. Open the Ubuntu terminal or command-line interface on your Windows machine.
2. In the terminal, enter the following commands one by one and press Enter after each:

```bash
sudo apt update
sudo apt upgrade
sudo apt install gcc
sudo apt install cmake
sudo apt install build-essential
sudo apt install libfftw3-dev
sudo apt install gromacs
```

Installation Complete and check the version hitting the command ```gmx```.