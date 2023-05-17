---
layout: post
title:  "Install WSL2 on windows 10"
image: assets/images/wsl2.png
---
A raw and draft version of wsl2 activation on my version 20H2 (OS Build 19042.746) windows 10 operating system. This is the notebook version during the whole trial and error. Tutorial may contain error as it is directly from my notebook.

### Check the version of windows
- Type winver and check the version of windows 
- For me it is showing 
- `Version 20H2 (OS Build 19042.746)`
- So this version of windows is okay for using wsl2 
- As microsoft is recommending for having OS Build 19041 and later

### Turn on windows feature on or off
- Check mark on Windows subsystem for LInux
- Check mark on Virtual Machine Platform
- Install ubuntu form microsoft store
- It may show that WSL 2 requires an update to its kernel componenet. 
- For more information please visit https://aka.ms/wsl2kernel
- Visiting that site download required files

### Step 4 - Download the Linux kernel update package
- visit https://aka.ms/wsl2kernel
- Install this components
- Then go fro windows powershell
- Type the command `wsl -l –v`
- This will show which wsl version you are using
- If it is showing version 1
- Then needed to change it to version 2
- This conversion will happen by this command 
- `wsl --set-version Ubuntu-18.04 2`
- After conversion needd to set up this version to as a the default version
- wsl --set-default-version 2

-----------------------------------------------------------------------------------------------------
## New one
1. WSL2 Ubuntu GUI
2. WSL2 Ubuntu GUI

Overview 
**Prerequisites**
- Install WSL 
- install Ubuntu 20.04/18/04
- Install Ubuntu GUI
- Test RDP connection to the Ubuntu VM


- Follow this link
- Windows Subsystem for Linux Installation Guide for Windows 10
- https://docs.microsoft.com/en-us/windows/wsl/install-win10
- Open windows powershell in administrative mode

### Step 1 - Enable the Windows Subsystem for Linux 
- You must first enable the "Windows Subsystem for Linux" optional feature before installing any Linux distributions on Windows. 
- Open PowerShell as Administrator and run: 
- `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`

### Step 3 - Enable Virtual Machine feature
- Before installing WSL 2, you must enable the Virtual Machine Platform optional feature.
- Open PowerShell as Administrator and run:
- `PowerShell`
- Copy
- `dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`

### Step 4 - Download the Linux kernel update package
1. Download the latest package:
- WSL2 Linux kernel update package for x64 machines

- Check your machine's health/properties
- Go to this pc
- Properties 
- Check computer's configuration
- 8 gb ram

- Update your ubuntu
- Sudo apt get update
- Sudo apt get upgrade

- Install xrdp
- `sudo apt install xrdp`

- Let's install lightweight gui (graphical user interface)
- `sudo apt install -y xfce4`

- install additional software
- sudo apt install -y xfce4-goodies

- After this he made a backup/ as a learner I don’t need it immediately


- In tutorial there is tested these commands

`sudo cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak`
`sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini`
`sudo sed -i 's/max_bpp=64/#max_bpp=64/nmax_bpp=128/g' /etc/xrdp/xrdp.ini`
`sedo sed -i 's/xserverbpp-24/#xserverbpp=24\nxserverbpp=128/g' /etc/xrdp/xrdp.ini`
`echo xfce4-session > ~/.xsession`
`suso nano /etc/xrdp/startwm.sh`


- go to the last two lines of the previous commnands
- given a space between # and test and exect
- and added two additional lines
### xfce
- startxfce4
- ctrl+X, save the file 

- sudo /etc/init.d/xrdp start
- Starting Remote Desktop Protocol server
- This will open a remote desktop dialog
- then press correct button


**Install the Windows Subsystem for Linux**
Find the link: https://christitus.com/wsl2/


## Try this for understanding wsl2 & GUI for total control

### INSTALL UBUNTU GUI
- `pwd`
- `lsb_release -a`
- `sudo apt update`
- `sudo apt upgrade`

### Install XRDP to install RDP
- `sudo apt install xrdp`

### Install a lightweight graphical user interface
- `sudo apt install -y xfce4`

- Package configuration; Configuring lightdm
- This will ask you to select default display manager;
 - select gdm3 as gui

### Install an additional software
- `sudo apt install -y xfce4-goodies`

- Now it is needed to do some configuration of XRDP,
- `sudo cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak`
- `sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini`

- `sudo sed -i 's/max_bpp=64/#max_bpp=64/nmax_bpp=128/g' /etc/xrdp/xrdp.ini`
- `sedo sed -i 's/xserverbpp-24/#xserverbpp=24\nxserverbpp=128/g' /etc/xrdp/xrdp.ini`

- `echo xfce4-session > ~/.xsession`
- `suso nano /etc/xrdp/startwm.sh`



- This wil open gnu nano 4.8 to edit something
- go to the command last two line
- given a space between # and test and exect
- and added two additional lines

### xfce
- startxfce4
- ctrl+X, save the file 

- `sudo /etc/init.d/xrdp start`
- Starting Remote Desktop Protocol server

- This will open a remote desktop dialog
- then press correct button


**Done**
- Yeah its took a whole day to accomplish this. At last I did it....
- Shamrat 
- 17.01.2021


**Reference Tutorial**
wsl2 by David Bomball: https://www.youtube.com/watch?v=_fntjriRe48&t=185s
