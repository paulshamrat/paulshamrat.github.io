---
layout: post
title:  "GROMACS 2021.2 installation on WSL2"
author: paushamrat
image: assets/images/example.png
---

0. Check you have these prerequisties
   - Latest version of your C and C++ compilers <br>
      `gcc --version` <br>
   - CMake version 3.13 or later. <br>
      `cmake --version` <br>
   - Find this site useful: https://www.cyberciti.biz/faq/locate-linux-gnu-c-or-gcc-compiler-location/

1. Download the tarball from (36.2 MB) <br>
   As https https://ftp.gromacs.org/gromacs/gromacs-2021.2.tar.gz

2. Move it to your desired directory and open the terminal indicating that path

3. Follow these commands

   `tar xfz gromacs-2021.2.tar.gz` <br>
   `cd gromacs-2021.2` <br>
   `mkdir build` <br>
   `cd build` <br>
   `cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON` <br>
   `make` <br>
   `make check` <br>
   `sudo make install` <br>
   `source /usr/local/gromacs/bin/GMXRC` <br>

<br>
GROMACS2021.2 installed...
