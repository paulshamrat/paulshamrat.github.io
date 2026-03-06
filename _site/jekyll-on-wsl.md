# jekyll in a new repository

> sudo apt update
> sudo apt install -y ruby-full build-essential zlib1g-dev

> echo '# Add Ruby to PATH' >> ~/.bashrc
> echo 'export PATH="$HOME/.gem/ruby/X.X.0/bin:$PATH"' >> ~/.bashrc
> source ~/.bashrc

> sudo gem install jekyll bundler
> gem install --user-install jekyll bundler

> mkdir ~/.gems
> export GEM_HOME="$HOME/.gems"
> export PATH="$GEM_HOME/bin:$PATH"
> gem install jekyll bundler

> jekyll new mysite
> cd mysite
> bundle install
> bundle exec jekyll serve

# Jekyll in an existing repository

> jekyll new paulshamrat.github.io --force
> cd mysite
> bundle install
> bundle exec jekyll serve

## YES YES after nearly 2 years i am back to jekyll