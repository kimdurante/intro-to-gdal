---
layout: default
title: Installing GDAL
nav_order: 1
---

## Installing GDAL

There are several options for downloading GDAL packages. 

### On a Mac

Download the appropriate framework for your MacOS:

[http://www.kyngchaos.com/software/frameworks/#gdal_complete](http://www.kyngchaos.com/software/frameworks/)

Once installed, open a terminal window and run the folowing command:

```export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH```

Or, save it to your profile:

```echo 'export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH' >> ~/.bash_profile
source ~/.bash_profile```

To test your installation, run the terminal command:

```gdalinfo --version```

### On Windows:

Download the appropriate binary for your Python and bit (32 or 64) version:

[https://www.gisinternals.com/release.php](https://www.gisinternals.com/release.php)

Clicking the link will take you to the list of binaries (installers) to download.

Locate the “core” installer, which has most of the components for GDAL.

After downloading your version, install GDAL with standard settings.

Next, return to the list of GDAL binaries and install the python bindings for your version of Python, this can either be 2.7, 3.1, or 3.2.

Download the Python bindings and install them.
