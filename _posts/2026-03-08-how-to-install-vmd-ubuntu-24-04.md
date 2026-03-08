---
layout: post
title: "How to Install VMD (Visual Molecular Dynamics) on Ubuntu 24.04"
date: 2026-03-08 13:00:00 +0000
description: "A complete step-by-step guide to installing VMD 1.9.4 Alpha on Ubuntu 24.04 Noble Numbat."
tags: [linux, vmd, molecular-dynamics, bioinformatics, simulation]
categories: [technical]
---

VMD (Visual Molecular Dynamics) is a powerful tool for displaying, animating, and analyzing large biomolecular systems. While it's a staple in computational biophysics, installing it on modern Linux distributions like Ubuntu 24.04 can sometimes be tricky due to dependency requirements.

In this guide, I'll walk you through the process of installing **VMD 1.9.4 Alpha**, which is the recommended version for modern hardware.

---

## 1. Prerequisites: Install Dependencies

Before installing VMD, you need to ensure your system has the necessary libraries for OpenGL rendering and script execution.

Open your terminal and run the following command:

```bash
sudo apt-get update
sudo apt-get install -y libglu1-mesa libxinerama1 libxi6 libxrender1 libcanberra-gtk-module csh libtcl8.6 libtk8.6
```

---

## 2. Download the VMD Binary

VMD requires manual registration, so you'll need to download it from the official website:

1.  Go to the [VMD Download Page](https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD).
2.  Register or log in.
3.  Under **Version 1.9.4 LATEST ALPHA**, select:
    **LINUX_64 (RHEL 7+) OpenGL, CUDA, OptiX RTX, OSPRay**
4.  Save the file to your `~/Downloads` folder.

---

## 3. Extract and Configure

Once the download is complete, navigate to your Downloads folder and extract the archive:

```bash
cd ~/Downloads
tar -xvzf vmd-1.9.4a57.bin.LINUXAMD64-CUDA102-OptiX650-OSPRay185.opengl.tar.gz
cd vmd-1.9.4a57
```

Now, run the configuration script:

```bash
./configure
```

---

## 4. Final Installation

After configuring, move into the `src` directory and install the binary to your system:

```bash
cd src
sudo make install
```

---

## 5. Verify the Installation

To start VMD, simply type:

```bash
vmd
```

You should see the **VMD Main** controller and a **VMD Display** window appear. If you have an Intel Iris Xe or similar integrated graphics, VMD will use OpenGL rendering for smooth performance.

---

## Troubleshooting: Fix Tiny Fonts on High-DPI Screens

If you are using a high-resolution display, you might find that VMD's menus and text are very small. You can fix this by setting environment variables and using a startup script:

1.  **Main Menu Scaling**: Launch VMD with the `FLTK_SCALING_FACTOR` variable:
    ```bash
    export FLTK_SCALING_FACTOR=2.0
    vmd
    ```
2.  **Plugin/Console Scaling**: Create a `.vmdrc` file in your home directory:
    ```tcl
    tk scaling 2.0
    ```

---

---

*Happy simulating!* 🧬💻
