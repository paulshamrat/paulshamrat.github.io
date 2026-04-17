---
layout: post
title: "Rclone Google Drive Sync Guide: A Reliable Multi-Device Workflow"
date: 2026-03-03 10:00:00 +0000
description: "A comprehensive guide to managing Google Drive synchronization on Linux using rclone, including custom Client ID setup for stability."
tags: [rclone, google-drive, linux, cloud, backup]
categories: [technical]
---

Managing large datasets or research wikis across multiple devices can be a headache, especially with Google Drive's native client limitations on Linux. **Rclone** is the gold standard for bridging this gap, offering a powerful, command-line interface for seamless cloud synchronization.

In this guide, I'll walk you through setting up a robust, "permanent" connection that doesn't require daily re-authentication, along with my recommended daily workflow.

---

## 1. Fixing the Root Cause (The Permanent Fix)

If you use the default rclone configuration, you might find yourself logging in and authorizing every few days. To stop this and gain better performance, you should create your own **Google Client ID**.

### How to Create Your Own Client ID & Secret
1.  **Google Cloud Console**: Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  **Create Project**: Click the project dropdown at the top and select **"New Project"**. Name it something like `rclone-sync`.
3.  **Enable API**: Search for **"Google Drive API"** and click **Enable**.
4.  **Configure OAuth Consent**:
    - Go to **APIs & Services** > **OAuth consent screen**.
    - Choose **"External"** and click **Create**.
    - Fill in the required app details and your email.
    - Click **Save and Continue** until you're back at the dashboard.
5.  **Create Credentials**:
    - Go to **APIs & Services** > **Credentials**.
    - Click **+ Create Credentials** > **OAuth client ID**.
    - Select **"Desktop app"** as the Application type.
    - Click **Create**.
6.  **Get the Keys**: A popup will show your **Client ID** and **Client Secret**. 

### Apply the Keys
Run `rclone config`, edit your existing `gdrive` remote (or create a new one), and paste your new `client_id` and `client_secret` when prompted. This makes your connection much more stable and faster.

---

## 2. Daily Workflow (Best Practices)

To keep your files synced without accidents, I recommend this routine:

### Start of Day: Download Changes
If you've worked on another device, bring those changes to your local machine:
```bash
rclone copy gdrive:works /home/paul/works -P
```

### End of Day: Upload Changes
Back up your locally modified files to the cloud:
```bash
rclone copy /home/paul/works gdrive:works -P
```

### Syncing a Specific Folder
If you've only updated one project and don't want to scan your entire `works` directory, you can target that specific subfolder to save time:

```bash
rclone copy /home/paul/works/academics gdrive:works/academics -P
```

> [!TIP]
> Use `copy` instead of `sync` most of the time. `copy` only adds files to the destination; `sync` can delete files if they are missing on the source.

---

## 3. Maintenance & Troubleshooting

### Check for Differences
Before a big transfer, see what has actually changed:
```bash
rclone check /home/paul/works gdrive:works --size-only
```

### Fix Duplicates
Google Drive sometimes creates two files with the exact same name. Rclone can fix this automatically:
```bash
rclone dedupe gdrive:works
```

### Re-authentication
If you ever get an "Authorization failed" error, run:
```bash
rclone config reconnect gdrive:
```

---

## 4. Understanding the Logs

- **`Checks: 2679 / 2679`**: Rclone compared all files and found them identical. It did **NOT** re-transfer them, saving you time and bandwidth.
- **`Progress (-P)`**: Always use this flag to see real-time transfer speeds and percentages.

By following this setup, your research data and wiki will stay synchronized and secure, allowing you to focus on the science rather than the plumbing.

**Happy Syncing!** 📂✨
