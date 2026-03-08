---
layout: post
title:  "Install Git bash on Windows 10"
author: paul
image: assets/images/git-bash-windows.png
---

Committing code directly from a local disk to a GitHub repository is an essential skill for productivity. This guide covers how to install, configure, and use Git Bash on Windows 10, including managing large files with Git LFS.

## Installing Git Bash on Windows

1. **Download Git:** Get the Windows installer from the official site: [git-scm.com/download/win](https://git-scm.com/download/win).
2. **Install:** Follow the installation wizard. This will install "Git Bash," a terminal that provides a Unix-like environment on Windows.
3. **Open Git Bash:** Launch the application and navigate to your project directory.
   ```bash
   cd /c/git-projects
   ```

## Initial Configuration

Before you start committing, configure your global username and email:
```bash
git config --global user.name "your_username"
git config --global user.email "your_email@example.com"
```

## Basic Git Workflow

### 1. Cloning and Committing
If you have an existing repository on GitHub:
```bash
# Clone the repository
git clone https://github.com/user/testgit.git
cd testgit

# Check status and add files
git status
git add test.txt

# Commit and push
git commit -m "Initial commit"
git push -u origin main
```

### 2. Handling Merge Conflicts (Pull Before Push)
If you've made changes directly on GitHub (in the browser), your local version will be behind. If you try to push local changes, it will be rejected. To fix this:
```bash
git pull origin main
```
This command pulls the latest changes and merges them into your local branch. After resolving any conflicts, you can push your changes.

## Managing Large Files with Git LFS

Standard Git is not optimized for large files (like videos or large datasets). Git Large File Storage (LFS) handles this by storing references in Git while keeping the actual files on a separate server.

### 1. Setup on Windows/WSL
```bash
# Install and initialize LFS
sudo apt update && sudo apt install git-lfs # On WSL
git lfs install
```

### 2. Tracking and Pushing Large Files
```bash
# Initialize a new repo or go to an existing one
git init

# Track specific file types (e.g., .mp4) or a specific file
git lfs track "*.mp4"
git lfs track "large_dataset.csv"

# Add the configuration file and commit
git add .gitattributes
git commit -m "Configure Git LFS for tracking large files"

# Add the large files and push
git add video.mp4 large_dataset.csv
git commit -m "Add large media and data files"
git push origin main
```

---

*Last Updated: Jul 20 2023.*