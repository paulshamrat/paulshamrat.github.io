---
layout: post
title:  "Install Git bash on Windows 10"
author: paul
image: assets/images/git-bash-windows.png
---

Commiting codes directly from the local disc to the github repository is an important productivity asset. Let's learn some codes regarding commiting codes through gitbash on Windows 10.

# Git-bash on windows

- download git (commandline interface ) for windows from this site
- [https://git-scm.com/download/win](https://git-scm.com/download/win)
- there will be an unix like terminal installed "gitbash"
- open gitbash
- setup your working directory to the c/git

like: 

```bash
user@DESKTOP-AB6NSDID MiNGW64/c/git
```

- login your github account
- create new repository
- name it "testgit" (whatever in your mind)

```bash
$ git config --global user.name "username"
$ git config --global user.email "useremail@mail.com"
```

- [this will ask your credentials and login via browser in which you previously logged into your github account]

```bash
$ git clone [https://github.com/user/testgit.git](https://github.com/user/testgit.git)
$ ls
$ cd testgit
$ git status
$ git add test.txt
$ git status
$ git commit -m "first commit" test.txt
$ git push -u origin main
```

## Add, commit and push multiple files

```bash
$ git status
$ git add --all
$ git status
$ git commit -m "added 4 new posts" --all
$ git status
$ git push -u origin master
```

# Another note:
- you have cloned repository on your local machine.
- but you have commited from the browser directly.
- then you made changes in your local machine and tried to push the command
- then it wil show, "rejected" sign! so what to do?

```bash
$ git pull --all
```
- So, this command will pull down all changes made in the repository and merged with your local machine and pop-up a message to close the command tab of VS code.
- close the current tab and it pulled down succesfully.
- Now time to push your local changes to your desired repository.

# Git large files

```
# 01 install
git lfs install

# 02 test push
git init
git lfs track "test.txt"
git add .gitattributes
git commit m "configure Git LFS for large files"
git push origin main

# 03 add more large files and origin push
git add .
git commit -m "add new files and changes"
git push origin main

```


# git large file on wsl

```
# Install Git and Git LFS on WSL (if not already installed)
sudo apt update
sudo apt install git git-lfs

# Configure Git LFS
git lfs install
git lfs version
git --version


# Set up a new repository, track large files, and push using Git LFS
mkdir git-lfs-demo
cd git-lfs-demo
git init
git lfs track "test.txt"
git add .gitattributes
git commit -m "Configure Git LFS for large files"
git remote add origin <your_remote_repository_url>  # Replace with your actual remote repository URL
git push origin main

# Add More Large Files and Push to Origin
# Assuming you have more large files (e.g., video.mp4 and dataset.csv) to add
git add video.mp4 dataset.csv
git commit -m "Add new files and changes"
git push origin main

```

***Last update: Jul 20 2023.***