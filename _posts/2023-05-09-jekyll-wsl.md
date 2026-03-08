---
layout: post
title:  "Install Jekyll on WSL"
author: paulshamrat
image: assets/data/rmsd-1aki.svg
---
# Introduction:
Jekyll is a powerful static site generator that allows you to manage websites using plain text files. By using Windows Subsystem for Linux (WSL), you can run a full Jekyll development environment directly on your Windows machine. This guide covers the installation and setup process.

## Installation Steps

Open your WSL terminal (e.g., Ubuntu) and run the following commands:

### 1. Install Ruby and Build Dependencies
```bash
sudo apt update
sudo apt install -y ruby-full build-essential zlib1g-dev
```

### 2. Configure Local Gem Path
To avoid using `sudo` for installing gems and to ensure they persist correctly, add these lines to your `~/.bashrc`:

```bash
echo '# Ruby Gems Environment' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/.gems"' >> ~/.bashrc
echo 'export PATH="$HOME/.gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### 3. Install Jekyll and Bundler
```bash
gem install jekyll bundler
```

## Creating a New Site

If you are starting a new project:
```bash
jekyll new my-awesome-site
cd my-awesome-site
bundle install
bundle exec jekyll serve
```

## Working with an Existing Repository

If you're maintaining an existing Jekyll site (like a GitHub Pages blog):
```bash
cd your-repo-name
bundle install
bundle exec jekyll serve
```
Your site will be available at `http://localhost:4000`.

---

### Troubleshooting Tips
- If gems seem to go missing after a restart, ensure that your `GEM_HOME` and `PATH` are correctly exported in your `~/.bashrc`.
- Always use `bundle exec jekyll serve` to ensure you are using the versions specified in your `Gemfile`.

