---
layout: post
title: "GNOME System Customization: Achieving a Windows 11-Style Dock"
date: 2026-03-02 11:45:00-0500
description: A guide on how to customize the GNOME dock to look and feel like Windows 11 with centered icons and a functional start menu.
tags: linux gnome customization windows11
categories: system-customization
---

Following up on recent system tweaks, I've successfully transformed my Ubuntu GNOME desktop to mirror the clean, centered aesthetic of Windows 11. Here's a breakdown of the configuration and how to ensure it stays persistent.

### The Objective
The goal was to move the traditional Ubuntu dock into a single, centered panel that expands dynamically as applications are opened, with the "Show Apps" (Start) button positioned at the very left of the centered group.

### Core Extensions
To achieve this, I used two primary GNOME extensions:
1. **Dash to Panel**: This is the heavy lifter that combines the top bar and the dock into a single taskbar at the bottom.
2. **ArcMenu**: (Optional) While I explored ArcMenu for a more themed Start menu, the built-in Ubuntu "Show Apps" button proved more stable for this specific centered layout.

### Configuration Steps

#### 1. Centering the Taskbar
Using `gsettings`, I configured `Dash to Panel` to center all elements. The key is the `panel-element-positions` JSON:

```bash
gsettings --schemadir ~/.local/share/gnome-shell/extensions/dash-to-panel@jderose9.github.com/schemas set org.gnome.shell.extensions.dash-to-panel panel-element-positions \
'{"0":[{"element":"showAppsButton","visible":true,"position":"centered"},{"element":"taskbar","visible":true,"position":"centered"},{"element":"activitiesButton","visible":false,"position":"hidden"},{"element":"leftBox","visible":false,"position":"hidden"},{"element":"centerBox","visible":false,"position":"hidden"},{"element":"rightBox","visible":true,"position":"stackedBR"},{"element":"dateMenu","visible":true,"position":"stackedBR"},{"element":"systemMenu","visible":true,"position":"stackedBR"},{"element":"desktopButton","visible":true,"position":"stackedBR"}]}'
```

#### 2. Ensuring Persistence
One common issue with GNOME extensions is that they can sometimes revert after a restart or crash. To prevent this, ensure that user extensions are globally enabled:

```bash
gsettings set org.gnome.shell disable-user-extensions false
```

### Summary
The final result is a sleek, modern desktop that maintains the power of Linux while enjoying the refined UI of Windows 11. For more detailed logs and a step-by-step breakdown of all my system customizations, stay tuned for my upcoming comprehensive System Customization Guide.
