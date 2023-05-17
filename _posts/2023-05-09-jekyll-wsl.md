---
layout: post
title:  "Install Jekyll on WSL"
author: paulshamrat
image: assets/data/rmsd-1aki.svg
---
# Introduction:
Jekyll is a popular static site generator that allows you to create and manage websites using plain text files. If you're using the Windows Subsystem for Linux (WSL), you can leverage the power of Jekyll right on your Windows machine. In this guide, we will walk you through the process of setting up Jekyll on WSL, from installation to serving your first Jekyll site.

Command lines

# run jekyll in a new rep
```
sudo apt update
sudo apt install -y ruby-full build-essential zlib1g-dev
echo '# Add Ruby to PATH' >> ~/.bashrc
echo 'export PATH="$HOME/.gem/ruby/X.X.0/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
sudo gem install jekyll bundler
gem install --user-install jekyll bundler
mkdir ~/.gems
export GEM_HOME="$HOME/.gems"
export PATH="$GEM_HOME/bin:$PATH"
gem install jekyll bundler
jekyll new mysite
cd mysite
bundle install
bundle exec jekyll serve

# run this in existing repo
jekyll new paulshamrat.github.io --force
cd paulshamrat.github.io
bundle install
bundle exec jekyll serve

## YES YES after nearly 2 years i am back to jekyll

>> update 230512
- probably gems are deleted when session ends
- then again need to install it from the beginning commands
- and run bundle install as existing repo for "paulshamrat.github.io"


>> update 230514
- single command
```
sudo apt update; sudo apt install -y ruby-full build-essential zlib1g-dev; echo '# Add Ruby to PATH' >> ~/.bashrc; echo 'export PATH="$HOME/.gem/ruby/X.X.0/bin:$PATH"' >> ~/.bashrc; source ~/.bashrc; sudo gem install jekyll bundler; gem install --user-install jekyll bundler; mkdir ~/.gems; export GEM_HOME="$HOME/.gems"; export PATH="$GEM_HOME/bin:$PATH"; gem install jekyll bundler
```

```
