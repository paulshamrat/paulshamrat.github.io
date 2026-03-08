---
layout: post
title:  "Install WSL2 on windows 10"
image: assets/images/wsl2.png
---
A draft guide for activating WSL2 on Windows 10 (Version 20H2, OS Build 19042.746). This post serves as a notebook documenting the trial and error process. Note that it might contain minor errors as it is taken directly from my personal notes.

### Check your Windows Version
- Type `winver` in the Windows search bar and check your version.
- My system shows `Version 20H2 (OS Build 19042.746)`.
- This version is suitable for WSL2, as Microsoft recommends OS Build 19041 or later.

### Enable Windows Features
- Search for "Turn Windows features on or off".
- Enable **Windows Subsystem for Linux**.
- Enable **Virtual Machine Platform**.
- Install **Ubuntu** from the Microsoft Store.
- If you see a message saying "WSL 2 requires an update to its kernel component," visit [https://aka.ms/wsl2kernel](https://aka.ms/wsl2kernel).
- Download and install the required files from that site.

### Update the Linux Kernel
- Visit [https://aka.ms/wsl2kernel](https://aka.ms/wsl2kernel).
- Install the update components.
- Open **Windows PowerShell** as Administrator.
- Run the command: `wsl -l -v`
- This will display the WSL version currently in use.
- If it shows version 1, you need to upgrade to version 2 using the command:
  `wsl --set-version Ubuntu-18.04 2` (Replace `Ubuntu-18.04` with your installed version).
- Finally, set WSL2 as the default version:
  `wsl --set-default-version 2`

---

## Setting up WSL2 with Ubuntu GUI

### Prerequisites
- Install WSL and a Linux distribution (e.g., Ubuntu 20.04).
- Install a lightweight GUI.
- Test the RDP connection to the Ubuntu environment.

### Step-by-Step Guide
Follow the official documentation if needed: [WSL Installation Guide](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

1. **Enable WSL Component:**
   Open PowerShell as Administrator and run:
   `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`

2. **Enable Virtual Machine Feature:**
   Run the following in PowerShell as Administrator:
   `dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`

3. **Install and Update Ubuntu:**
   - Update your packages:
     `sudo apt update && sudo apt upgrade`

4. **Install XRDP for Remote Desktop:**
   - `sudo apt install xrdp`

5. **Install a Lightweight Desktop Environment (XFCE):**
   - `sudo apt install -y xfce4`
   - During configuration, you may be asked to select a default display manager; select `gdm3` or `lightdm`.
   - Install additional utilities:
     `sudo apt install -y xfce4-goodies`

6. **Configure XRDP:**
   It is recommended to back up the configuration before editing:
   ```bash
   sudo cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak
   sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini
   sudo sed -i 's/max_bpp=64/#max_bpp=64\nmax_bpp=128/g' /etc/xrdp/xrdp.ini
   sudo sed -i 's/xserverbpp=24/#xserverbpp=24\nxserverbpp=128/g' /etc/xrdp/xrdp.ini
   echo xfce4-session > ~/.xsession
   ```

7. **Edit Startup Script:**
   Open the startup script:
   `sudo nano /etc/rdp/startwm.sh`
   Add the following line before the last two lines:
   `startxfce4`

8. **Start the XRDP Server:**
   `sudo /etc/init.d/xrdp start`
   This will allow you to connect via the Windows Remote Desktop Connection tool using `localhost:3390`.

---

**Summary**
This setup took some time to figure out, but it provides full control over the Ubuntu environment with a graphical interface.

*Shamrat*
*Published: 17.01.2021*

**References**
- [WSL2 Guide by David Bombal](https://www.youtube.com/watch?v=_fntjriRe48&t=185s)
- [Chris Titus Tech - WSL2](https://christitus.com/wsl2/)
