---
layout: post
title: "Troubleshooting High RAM Usage on Ubuntu: A Case Study"
date: 2026-03-06 17:30:00 +0000
description: "A quick walkthrough of how I diagnosed 13GB of RAM usage and cleared it down to 4GB by identifying hidden virtualization processes and dropping system caches."
tags: [linux, ubuntu, ram, optimization, docker, troubleshooting]
categories: [technical]
---

Have you ever looked at your system monitor and realized that nearly all your RAM is gone? Today, I hit **13 GiB** of usage out of **15 GiB**, despite not having any major applications visibly open.

In this post, I'll walk through how I diagnosed the issue and recovered **9 GiB** of RAM in just a few minutes.

---

## 1. The Symptom: Where did my RAM go?

Running a simple `free -h` revealed a concerning state:
```text
               total        used        free      shared  buff/cache   available
Mem:            15Gi        13Gi       304Mi       397Mi       2.3Gi       1.8Gi
```

Only 300MB of free RAM! While Linux uses memory for caching, the "available" column showed only 1.8GB, meaning the rest was actively "held" by processes.

---

## 2. The Investigation: Finding the Culprit

To find out what was eating the memory, I used `ps` to sort processes by memory consumption:

```bash
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 10
```

The result was immediate:
- **PID 3213**: `qemu-system-x86_64` was using **52.2%** of my RAM (~7.8 GiB).

This process is a Virtual Machine (QEMU). On my system, it was associated with **Docker Desktop**. Even if no containers are doing heavy work, the VM itself reserves a massive chunk of RAM.

---

## 3. The Solution: Reclaiming the Memory

To fix this, I followed a two-step approach:

### Step A: Stopping the Resource Hog
Since I wasn't using Docker at the moment, I stopped the service:
```bash
sudo systemctl stop docker.socket docker
```

### Step B: Clearing the Page Cache
Linux keeps a "Page Cache" of files you've recently accessed. While this is normally good for performance, clearing it can reveal exactly how much "real" RAM you have left.
```bash
sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches
```

---

## 4. The Result: 9GB Recovered

After these steps, another check with `free -h` showed:
```text
               total        used        free      shared  buff/cache   available
Mem:            15Gi       4.1Gi       9.7Gi       361Mi       2.2Gi        11Gi
```

We went from **13 GiB used** to **4.1 GiB used**. Mission accomplished!

---

## 5. Pro-Active Monitoring

If you want to keep a closer eye on your memory without opening a heavy GUI, I highly recommend installing these CLI tools:

1.  **htop**: An interactive process viewer that is much more readable than standard `top`.
    - **How to use**: Simply type `htop` in your terminal.
    - **Keys to remember**:
        - `F6`: Sort by memory (%) or CPU (%).
        - `F3`: Search for a specific process (e.g., "docker").
        - `F9`: Kill a process safely.
        - `q`: Quit.

2.  **smem**: A tool that reports "PSS" (Proportional Set Size), which is the most accurate way to measure memory.
    - **How to use**:
        - `smem -tw`: Shows total memory usage across the system.
        - `smem -u`: Shows memory usage per user.
        - `smem -rk`: Sorts by memory and shows values in MB/GB (human-readable).

**Summary Tip**: If your RAM is low, always check for hidden Virtual Machines or Docker instances first. They are often the stealthy consumers!

---
*Happy debugging!* 🛠️📉
