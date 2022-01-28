---
layout: post
title:  "NGS tool installation on Ubuntu 20.04"
image: assets/images/ngs2.png
---
A raw and draft version of "NGS tool installation on ubuntu" on my Ubuntu 20.04 LTS operating system. This is the notebook version during the whole trial and error. Tutorial may contain error as it is directly from my notebook.

## INSTALLATION PROCEDURE
### 01. Linux (Ubuntu) Distro
- Find out a Debian Linux distribution (i.e.. Ubuntu20.04) primed laptop or desktop and start.

### 02. Anaconda
- As anaconda is a python distribution it is good to be installed python on your system 
- Though Ubuntu comes with default python 2.7
- Try to prime it with the latest version of python I.e. python 3.8
- Download Anaconda distribution form their official website.
- https://www.anaconda.com/products/individual
- On the website of anaconda you find Download option
- Click on Download button
- Download Anaconda Installer for Linux
- Select 64-Bit (x86) Installer (529 MB) [as per your device requirements]
- This will downolad a *.sh file which will be save on your download directory.
- Assume it is downloaded on your download folder
- So there is the *.sh file
- Type this command 
- `~/Downloads/Anaconda3-2020.11-Linux-x86_64.sh`
- This will install anaconda into your ubuntu system
- Installation Guide can be found here 
- https://docs.anaconda.com/anaconda/install/linux/
- To initiate anaconda open your terminal and type
- `conda init`
- To open anaconda navigator type this command on the terminal
- `anaconda-navigator`

### 03. bioconda / packages / sra-tools 
- To install bioconda sra tools type 
- `conda install -c bioconda sra-tools`
- This command will install v2.8 but it is recommended to install 2.9
- Install v2.9 by this command  
- `conda install -c bioconda/label/cf201901 sra-tools`
- Installation guide can be found here
- https://anaconda.org/bioconda/sra-tools 
- Now you are ready to go..
- Activate/deactivate your conda
- After installation your terminal will prompt with an initial text "(base)"
- Activate or deactivate your anaconda by this command
- `conda activate`
- `conda deactivate` 
- This will only work on conda 4.6 and later versions. For conda versions prior to 4.6, run:
- Windows: activate or deactivate
- Linux and macOS: source activate or source deactivate

### 04. FasttQC
- Before installation of fastqc make sure your system primed with java
- First check if there is installed java or not
- To check the presence of java type this command
- `java -version`
- If not showing any installed version of java then download it with this instruction in this site
- https://phoenixnap.com/kb/how-to-install-java-ubuntu
- Install fastQC software for the qualicte checking purpose of sequence
- Install it with the below command
- `sudo apt-get install -y fastqc`
