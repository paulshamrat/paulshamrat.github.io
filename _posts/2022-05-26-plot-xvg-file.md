---
layout: post
title:  "Plot the *.xvg file"
author: paulshamrat
image: assets/data/rmsd-1aki.svg
---

# Plot the *.xvg file.

GROMACS uses the XVG file format. The GRACE program on UNIX/LINUX systems and the GNUPlot program on Windows can display this format graphically. XVG files are plain text files that contain tabular data separated by tabulators as well as two types of comments that include data labels.

However, there is a fun an cool way to visualize the xvg file.

Step 1: Open a file rmsd.ipynb
Step 2: Copy and Paste the following python code inside the code block

```
import numpy as np
import matplotlib.pyplot as plt

x, y = [], []

with open("https://paulshamrat.github.io/assets/data/rmsd-1aki.xvg") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("RMSD")    
ax1.set_xlabel('Time (ns)')
ax1.set_ylabel('RMSD (nm)')
ax1.plot(x,y, c='r', label='1aki')
leg = ax1.legend()
plt.show()  

```
Step final: ...aaaAnd the plot is here:

NB: Before importing data, ensure that you have masked or deleted all headers within the *.xvg file and have only two column data by opening it in an editor.

![rmsd-copy](https://paulshamrat.github.io/assets/data/rmsd-1aki.svg)<br>
RMSD