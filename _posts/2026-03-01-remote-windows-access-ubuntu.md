---
layout: post
title: "Remote Windows Access from Ubuntu: A Robust SSHFS & RDP Setup"
date: 2026-03-01 16:00:00 +0000
description: "How to seamlessly link an Ubuntu laptop to a Windows machine for high-performance research and file management."
tags: [ubuntu, windows, ssh, rdp, technical]
categories: [technical]
---

In modern research workflows, we often find ourselves jumping between different operating systems. For me, this meant wanting to access my powerful Windows machine (**Insurgent**) directly from my portable Ubuntu laptop (**Divergent**).

After some trial and error, I've established a setup that feels like the Windows drive is actually *inside* my Ubuntu laptop. Here is how I did it.

## The Goal
The objective was simple:
1.  **File Access**: Browse and edit Windows files (C: drive) as a local folder on Ubuntu.
2.  **Full Control**: Remote desktop into Windows when I need the GUI.
3.  **Stability**: A connection that doesn't break every time I reboot or change Wi-Fi.

---

## 🚀 The Solution: SSHFS + Remmina (RDP)

### 🛠️ Phase 1: The Windows Setup (Insurgent)
The biggest hurdle was authentication. Microsoft accounts and PINs often cause issues with SSH. The fix? **A dedicated local account.**

1.  **Local Account**: Created `insurgent_user` with a standard password.
2.  **Permissions**: Used `icacls` to grant this user full control over my main profile (`C:\Users\paul`).
3.  **OpenSSH Server**: Enabled the Windows OpenSSH service and allowed Port 22 through the firewall.
4.  **RDP Permission**: Added `insurgent_user` to the "Remote Desktop Users" and "Administrators" groups.

### 🐧 Phase 2: The Ubuntu Setup (Divergent)
Once Windows was ready, I used two key tools on Ubuntu:

-   **SSHFS**: To "mount" the Windows drive as a local folder.
-   **Remmina**: To control the Windows screen.

#### Mounting the Drive
To mount the Windows C: drive to `~/insurgent`:
```bash
sshfs insurgent_user@192.168.0.85:/C:/ ~/insurgent -o allow_other
```

### 🌍 Phase 3: Global Access (Tailscale)
What if I'm not at home? I installed **Tailscale** on both machines. This creates a secure, private tunnel that works anywhere in the world. I just replaced the home IP with my Tailscale IP, and it worked like a charm!

---

## 🧠 Lessons Learned
-   **Force Unmount**: If Windows reboots, the link "freezes." The command `fusermount3 -uz ~/insurgent` is your best friend to reset the link.
-   **NLA Settings**: If Remmina can't connect, disabling "Network Level Authentication" (NLA) on Windows usually fixes it.
-   **Home vs. Office**: I use the local IP at home for maximum speed and Tailscale when I'm away for reliability.

This setup has completely streamlined my workflow. No more syncing files or carrying two laptops—just one seamless research environment.

**Happy Hacking!** 🚀
