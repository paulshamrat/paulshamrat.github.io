---
layout: post
title: "Fixing GNOME Dock Behavior: Removing Empty Space and Centering"
date: 2026-03-15 15:05:00 +0000
categories: [Linux, Customization]
tags: [ubuntu, gnome, dock, customization]
---

Recently, I encountered an issue where my bottom dock in Ubuntu 24.04 had abnormal behavior: it spanned the full width of the screen, creating large empty spaces on the left and right while the icons were centered. This made it look more like a Windows taskbar than a modern dock.

## The Problem
The issue was caused by the **Dash to Panel** extension, which is designed to be a full-width taskbar. While useful for some, it doesn't provide the compact "dock" look that many prefer.

## The Solution
To fix this, I switched to the **Ubuntu Dock** (Dash to Dock) and configured it to be centered and compact.

### Steps to Fix:
1. **Switch Extensions**:
   - Disable `Dash to Panel`.
   - Enable `Ubuntu Dock`.

2. **Configure Settings via Terminal**:
   Run the following commands to make the dock compact and centered at the bottom:
   ```bash
   # Make the dock compact (not full-width)
   gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false
   
   # Position it at the bottom
   gsettings set org.gnome.shell.extensions.dash-to-dock dock-position 'BOTTOM'
   
   # Set icon size
   gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 48
   
   # Set dynamic transparency
   gsettings set org.gnome.shell.extensions.dash-to-dock transparency-mode 'DYNAMIC'
   ```

## Restore Script
To ensure these settings are never lost, I created a simple restore script:

```bash
#!/bin/bash
gnome-extensions enable ubuntu-dock@ubuntu.com
gnome-extensions disable dash-to-panel@jderose9.github.com
gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false
gsettings set org.gnome.shell.extensions.dash-to-dock dock-position 'BOTTOM'
gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 48
gsettings set org.gnome.shell.extensions.dash-to-dock transparency-mode 'DYNAMIC'
```

Now the dock looks exactly as it should—centered, compact, and clean!
