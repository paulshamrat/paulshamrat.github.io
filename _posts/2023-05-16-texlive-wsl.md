---
layout: post
title:  "Install Texlive in WSL"
image: assets/images/wsl2.png
---
# Code Summary: Install latex on wsl
```
sudo apt-get update
sudo apt-get install texlive-base
sudo apt-get install texlive-package-name
sudo apt-get install texlive-full
sudo apt-get install texlive-latex-base
sudo apt-get install texmaker evince
tex --version
```

# Setting Up LaTeX in VS Code with WSL on Windows

## Introduction:
LaTeX is a powerful typesetting system used for creating professional-quality documents, such as research papers, reports, and presentations. If you're using Visual Studio Code (VS Code) with Windows Subsystem for Linux (WSL), you can leverage the benefits of both environments to create LaTeX documents seamlessly. In this blog post, we'll guide you through the process of installing LaTeX in WSL, configuring the necessary extensions in VS Code, and verifying the installation.

## Installing LaTeX on WSL:
To get started, we need to install LaTeX on WSL. Follow these steps:
Launch your WSL terminal.

- Update the package list by running the following command:
```sudo apt-get update```
- Install the LaTeX base package:
```sudo apt-get install texlive-base```
- If you have specific package requirements, install them using:
```sudo apt-get install texlive-package-name```
- Replace texlive-package-name with the desired package(s) you need.
- If you want to install the complete TeXLive distribution, which includes a comprehensive set of packages, run:
```sudo apt-get install texlive-full```
- Additionally, install some essential LaTeX packages:
```sudo apt-get install texlive-latex-base```
- For a convenient LaTeX editor, you can install Texmaker and a PDF viewer like Evince:
```sudo apt-get install texmaker evince```

## Configuring VS Code:
Now that we have LaTeX installed on WSL, let's configure VS Code to work with it. Follow these steps:
- Install the "LaTeX Workshop" extension in VS Code. 
- Open the Extensions view (Ctrl+Shift+X), search for "LaTeX Workshop," and click "Install."
- Once the extension is installed, go to the Settings in VS Code (File > Preferences > Settings) and search for "latex-workshop.latex.tools" in the search bar.
- Click on "Edit in settings.json" to open the settings file.
- Add the following lines to the settings file:

```
json
Copy code
"latex-workshop.latex.tools": [
    {
        "name": "latexmk",
        "command": "latexmk",
        "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "-pdf",
            "%DOC%"
        ]
    }
],
"latex-workshop.latex.recipes": [
    {
        "name": "latexmk",
        "tools": [
            "latexmk"
        ]
    }
],
```

- Verifying the Installation:
- To confirm that LaTeX is installed correctly, let's check the version. 
- Run the following command in the WSL terminal:
```tex --version```

This command will display the version information of TeXLive installed on your WSL distribution.

## Conclusion:
Congratulations! You have successfully installed LaTeX on WSL and configured VS Code to work with it. With the LaTeX Workshop extension, you can now write, compile, and preview LaTeX documents seamlessly within VS Code. Enjoy the powerful typesetting capabilities of LaTeX while leveraging the convenience of the VS Code development environment. Happy typesetting!