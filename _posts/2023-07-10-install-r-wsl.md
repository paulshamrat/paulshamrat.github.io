---
layout: post
title:  "R in WSL"
image: assets/images/wsl2.png
---

``````
# Update and upgrade package lists
sudo apt update
sudo apt upgrade

# Install additional dependencies
sudo apt install libicu66
sudo apt install build-essential libcurl4-openssl-dev libssl-dev libxml2-dev

# Add CRAN repository to package sources
sudo tee /etc/apt/sources.list.d/cran.list <<EOF
deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran40/
EOF

# Import the CRAN repository key
gpg --keyserver keyserver.ubuntu.com --recv-key 'E298A3A825C0D65DFD57CBB651716619E084DAB9'
gpg --export --armor 'E298A3A825C0D65DFD57CBB651716619E084DAB9' | sudo apt-key add -

# Install additional development libraries
sudo apt install build-essential libcurl4-openssl-dev libssl-dev libxml2-dev libicu-dev

# Download and install libicu66 package
wget http://security.ubuntu.com/ubuntu/pool/main/i/icu/libicu66_66.1-2ubuntu2_amd64.deb
sudo dpkg -i libicu66_66.1-2ubuntu2_amd64.deb

# Install R
sudo apt install r-base
``````