# Shamrat Kumar Paul - Academic Portfolio

This repository contains the source code for my professional academic portfolio website. The site is designed to be minimalist, fast, and content-focused, showcasing my research, publications, and software projects.

🌐 **Live Site:** [paulshamrat.github.io](https://paulshamrat.github.io)

## 🚀 Key Features

- **Professional Sidebar:** A strictly hierarchical metadata display featuring PhD status, affiliation, and space-efficient research interest tags.
- **Dynamic Projects Portfolio:** A dedicated software page featuring cards that dynamically fetch stars, forks, and language stats from GitHub.
- **Automated Publication Stats:** Integrated Google Scholar citation and publication counts displayed via a custom statistics bar.
- **Research Gallery:** A curated visual gallery of scientific illustrations, conference presentations, and art, optimized for low whitespace and high visual impact.
- **Minimalist Aesthetic:** Built with a "less is more" philosophy using a clean typography system (Crimson Pro) and a responsive, mobile-first design.

## 🛠️ Technology Stack

- **Static Site Generator:** [Jekyll](https://jekyllrb.com/)
- **Templating:** Liquid
- **Styling:** Vanilla CSS (Modern, responsive layout)
- **Logic:** Vanilla JavaScript (GitHub API integration, citation fetching)
- **Deployment:** GitHub Pages

## 💻 Local Development

To run this site locally, ensure you have Ruby and Bundler installed, then follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/paulshamrat/paulshamrat.github.io.git
   cd paulshamrat.github.io
   ```

2. **Install dependencies:**
   ```bash
   bundle install
   ```

3. **Start the local server:**
   ```bash
   bundle exec jekyll serve --livereload
   ```

4. **View the site:**
   Open `http://localhost:4000` in your browser.

## 📁 Repository Structure

- `_data/`: Contains YAML files for publications, news, and navigation.
- `_layouts/`: Site templates (homepage, posts, etc.).
- `assets/`: Images, CSS, and JavaScript files.
- `gallery.md`: The visual portfolio page.
- `projects.md`: The dynamic software portfolio.
- `publications.md`: Full list of research papers.

---
© 2026 Shamrat Kumar Paul. Powered by Jekyll.
