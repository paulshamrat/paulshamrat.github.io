# iT takes estimated time: 
# Step 1: Install necessary packages
!apt-get update -qq
!apt-get install -y -qq cmake wget

# Step 2: Download GROMACS source code
!wget ftp://ftp.gromacs.org/pub/gromacs/gromacs-2021.3.tar.gz

# Step 3: Extract GROMACS source code
!tar xfz gromacs-2021.3.tar.gz

# Step 4: Compile and install GROMACS
!mkdir build
%cd build
!cmake ../gromacs-2021.3 -DCMAKE_INSTALL_PREFIX=/content/gromacs -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON
!make -j 2
!make check
!make install

# Step 5: Set up environment for using GROMACS inline in Google Colab
module_path = '/content/gromacs/bin/'
import os
os.environ['PATH'] = module_path + ':' + os.environ['PATH']
