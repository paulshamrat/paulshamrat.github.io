# Al-folio Theme Migration

This branch contains the full migration of the website to the `al-folio` theme.

## 🚀 What's New
- **Refined Navigation**: Removed duplicate links and simplified the menu to About, Publications, CV, and Blog.
- **Enhanced Biography**: Restored detailed PhD research and professional background.
- **Blog Migration**: Successfully ported all 13 original blog posts.
- **Publications**: BibTeX-powered automated rendering and highlighted selected works.
- **Dark Mode**: Fully functional theme toggle enabled in the navbar.
- **News**: Added 2022 fellowship announcement.

## 🛠️ Local Development
To view the site locally, run the following command in your terminal:
```bash
export GEM_HOME="$HOME/.gems"
export PATH="$HOME/.gems/bin:$PATH"
bundle exec jekyll serve --livereload --port 4001
```
Then, open your browser and go to: **[http://127.0.0.1:4001/](http://127.0.0.1:4001/)**

## 📂 Migration Branch
This branch (`al-folio-migration`) is intended for further testing and refinement before merging into `main`.
