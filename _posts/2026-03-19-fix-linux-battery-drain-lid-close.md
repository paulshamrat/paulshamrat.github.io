---
layout: post
title:  "Fixing Linux Battery Drain on Lid Close (HP Envy x360)"
image: assets/images/battery_fix.png
---

If you've switched to Linux on a modern laptop like the HP Envy x360, you might have noticed that closing the lid doesn't "save" your battery as well as it did on Windows. Often, you'll find your laptop dead after a few hours in your bag. This is usually due to **Modern Standby (s2idle)**, which keeps many components powered on.

Here is how I fixed it by enabling **Deep Sleep (S3)** and **Hibernation (S4)** on Ubuntu 24.04.

### The Problem: s2idle vs Deep Sleep
Most modern BIOS versions hide the traditional S3 "Suspend-to-RAM" in favor of S0ix (s2idle). While s2idle allows for faster wake times, it is often poorly optimized on Linux, leading to significant battery drain.

### Step 1: Prepare for Hibernation
Hibernation is the only way to ensure **zero** battery drain. Since I have 16GB of RAM, I needed a swap file of at least the same size.

```bash
sudo swapoff /swap.img
sudo rm /swap.img
sudo dd if=/dev/zero of=/swap.img bs=1M count=16384 status=progress
sudo chmod 600 /swap.img
sudo mkswap /swap.img
sudo swapon /swap.img
```

### Step 2: Configure Kernel Parameters
We need to tell the kernel to use the swap file for resuming from hibernation and to prefer "deep" sleep.

1. Find your swap UUID and offset:
   ```bash
   sudo findmnt -no SOURCE,UUID -T /swap.img
   sudo filefrag -v /swap.img | awk '{if($1=="0:"){print $4}}' | tr -d '.' | head -n 1
   ```

2. Update `/etc/default/grub` by adding these to `GRUB_CMDLINE_LINUX_DEFAULT`:
   - `resume=UUID=YOUR_UUID`
   - `resume_offset=YOUR_OFFSET`
   - `mem_sleep_default=deep`

3. Apply changes:
   ```bash
   sudo update-grub
   sudo update-initramfs -u
   ```

### Step 3: Force Suspend on Lid Close
Sometimes applications "inhibit" the sleep process. You can force the system to ignore these inhibitors when the lid is closed by editing `/etc/systemd/logind.conf`:

```ini
HandleLidSwitch=suspend
LidSwitchIgnoreInhibited=yes
```

### Verification
After a reboot, check if deep sleep is active:
```bash
cat /sys/power/mem_sleep
# You should see: s2idle [deep]
```

Now, your laptop should stay alive much longer when the lid is closed!

*Published: March 19, 2026*
