---
layout: post
title:  "Install Texlive on WSL"
image: assets/images/wsl2.png
---
Markdown and LaTeX are both powerful tools for document creation. When combined with Visual Studio Code (VS Code) and Windows Subsystem for Linux (WSL), you get a high-performance environment for typesetting professional research papers and reports.

## Installing LaTeX on WSL

To set up TeX Live on your Ubuntu WSL distribution, run the following commands:

```bash
# Update the package list
sudo apt update

# Option A: Install the base TeX Live distribution (minimal)
sudo apt install -y texlive-base

# Option B: Install the full TeX Live distribution (recommended for most users)
# This includes all packages and can take significant disk space.
sudo apt install -y texlive-full

# Optional: Install an editor and PDF viewer for Linux
sudo apt install -y texmaker evince
```

Verify your installation:
```bash
tex --version
```

## Configuring VS Code for LaTeX

To write and compile LaTeX documents directly within VS Code, you can use the **LaTeX Workshop** extension.

1. **Install Extension:** Open the Extensions view (`Ctrl+Shift+X`), search for "LaTeX Workshop," and install it.
2. **Configure Tools:** Open your `settings.json` (File > Preferences > Settings > Search for "json") and add the following configuration to enable `latexmk`:

```json
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
]
```

## Conclusion

With TeX Live installed on WSL and the LaTeX Workshop extension configured in VS Code, you can now write, compile, and preview professional documents seamlessly. Happy typesetting!