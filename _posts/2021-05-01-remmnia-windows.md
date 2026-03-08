---
layout: post
title:  "Remmina - Remote Desktop Connection on Windows 10"
author: paulshamrat
image: assets/images/remmnia4.png
---
A guide for setting up a Remmina Remote Desktop connection to access Windows 10 from Ubuntu 20.04 LTS. This post documents my trial-and-error process.

## Step 1: Configure Windows for Remote Access

To allow your Windows machine to be accessed remotely:

1. **Open Control Panel:** Go to **System and Security > System > Remote settings**.
2. **Enable Connection:** Under the **Remote** tab, select **"Allow remote connections to this computer"**.
3. **Advanced Settings:** Ensure the checkbox for "Allow connections only from computers running Remote Desktop with Network Level Authentication" is checked for better security.
4. **Select Users:** Click on **"Select Users"** to add specific accounts, or ensure your current user has permission.

## Step 2: Find your Windows IP Address

You need the server's IP address to connect from Linux:

1. Open the **Command Prompt (cmd)** and type:
   ```cmd
   ipconfig
   ```
2. Look for your active network adapter (e.g., **Ethernet adapter** or **Wireless LAN adapter**).
3. Note the **IPv4 Address** (e.g., `192.168.0.102`).
   - *Note: Avoid addresses from virtual adapters like WSL or VirtualBox.*

## Step 3: Connect from Ubuntu using Remmina

1. **Open Remmina:** Search for Remmina in your applications menu.
2. **Create New Connection:** Click the **"+" (plus)** icon in the top-left corner.
3. **Connection Details:**
   - **Server:** Enter the Windows IP address you found in Step 2.
   - **Username/Password:** Enter your Windows login credentials.
   - **Protocol:** Ensure **RDP** is selected.
4. **Connect:** Click **Save and Connect**. Your Windows desktop should now appear in a window on your Linux machine.

---

### Summary
Setting this up allows for a seamless workflow between different operating systems on the same network.

**Shamrat**

### Reference
- [Setup and demonstration of remote desktop connections (YouTube)](https://www.youtube.com/watch?v=Qb9lN3RCqVM)


