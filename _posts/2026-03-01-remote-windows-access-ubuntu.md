---
layout: post
title: "Remote Windows Access from Ubuntu: A Robust SSHFS & RDP Setup"
date: 2026-03-01 16:00:00 +0000
description: "How to seamlessly link an Ubuntu laptop to a Windows machine for high-performance research and file management."
tags: [ubuntu, windows, ssh, rdp, technical]
categories: [technical]
---

In modern research workflows, we often find ourselves working across different operating systems. For me, this meant wanting to access my powerful Windows machine (**Insurgent**) directly from my portable Ubuntu laptop (**Divergent**).

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
sshfs insurgent_user@192.168.0.76:/C:/ ~/insurgent -o allow_other
```

If the mount freezes after a reboot or network change, reset it first:
```bash
fusermount3 -uz ~/insurgent
sshfs insurgent_user@192.168.0.76:/C:/ ~/insurgent -o allow_other
```

#### Connecting with Remmina
For a quick RDP connection in Remmina, type only the server IP in the quick-connect bar:

```text
192.168.0.76
```

Do **not** type `username@ip` there, because Remmina will treat the whole string as the server name.

When prompted, use:

```text
Username: Paul Shamrat
Password: <your Windows account password>
Domain: <leave blank>
```

For a saved connection profile, these settings worked best:

```text
Protocol: RDP - Remote Desktop Protocol
Server: 192.168.0.76
Username: Paul Shamrat
Domain: blank
Resolution: Use client resolution or a smaller custom resolution
Colour depth: Automatic (32 bpp)
```

One important Windows detail: RDP login requires the real account password, not just a PIN.

### 🌍 Phase 3: Global Access (Tailscale)
What if I'm not at home? I installed **Tailscale** on both machines. This creates a secure, private tunnel that works anywhere in the world. I just replaced the home IP with my Tailscale IP, and it worked like a charm!

---

## 🧠 Lessons Learned
-   **Force Unmount**: If Windows reboots, the link "freezes." The command `fusermount3 -uz ~/insurgent` is your best friend to reset the link.
-   **NLA Settings**: If Remmina can't connect, disabling "Network Level Authentication" (NLA) on Windows usually fixes it.
-   **Home vs. Office**: I use the local IP at home for maximum speed and Tailscale when I'm away for reliability.
-   **Windows IPs Change**: My home IP changed from `192.168.0.85` to `192.168.0.76`, so checking `ipconfig` on Windows saved a lot of confusion.
-   **RDP Scaling Limitation**: Windows does not let me change display scaling from inside an RDP session, so changing Windows display scale there was not a reliable fix.
-   **Practical Display Workaround**: In Remmina, using a smaller custom resolution can make text appear larger than simply using client resolution.

## Troubleshooting

### SSH works, but SSHFS says `Connection reset by peer`
That usually means the Windows machine is reachable, but the SSH service reset the connection or the Windows IP changed. First, verify the current Windows IP with:

```powershell
ipconfig
```

Then reconnect from Ubuntu using the current address.

### Remmina says it cannot connect to the RDP server
Check the following on Windows:

```powershell
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name 'fDenyTSConnections' -Value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
Add-LocalGroupMember -Group "Remote Desktop Users" -Member "insurgent_user"
netstat -ano | findstr :3389
```

If I want the remote session to open as an administrator, I log in through Remmina with the administrator account itself rather than the helper account.

### The text looks too small in Remmina
Inside the Windows RDP session, the Display settings page reports that scaling cannot be changed from a remote session. In practice, the most reliable options are:

1. Use Remmina's scale mode / dynamic resolution tools.
2. Try a **smaller custom resolution** in the Remmina profile, which makes the Windows desktop appear larger.
3. If true Windows scaling is needed, set it while physically at the Windows machine, then reconnect later.

This setup has completely streamlined my workflow. No more manual file syncing or carrying two laptops—just one seamless, integrated research environment.

**Happy Hacking!** 🚀
