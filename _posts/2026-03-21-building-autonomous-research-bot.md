---
layout: post
title:  "Building an Autonomous Research Bot with GitHub Actions and Gemini"
image: assets/images/research_bot_setup.png
published: true
---

As part of my ongoing work, I wanted a way to automatically track and summarize the latest research related to a specific protein of interest. To solve this, I built an autonomous pipeline that scrapes new papers, summarizes them, and publishes a weekly digest directly to my personal website. Here's how I set it up.

### The Architecture: Python + Gemini API

The core of the bot is a Python script that runs weekly. It relies on two main components:
1. **Europe PMC API**: To search for recent publications related to the target protein (for example, "p53" or any other molecule).
2. **Google Gemini API**: To synthesize the abstracts and write a cohesive, human-readable narrative.

The fetcher script constructs a query for papers published in the last 7 days. It extracts the titles, authors, and abstracts, passing them to the **Gemini 2.5 Flash** model with a specific prompt:

> "You are a scientific reporter writing a short Weekly Research Digest for our community. Write a CONCISE, flowing narrative of MAXIMUM 300 words that highlights the most important trends and findings... Focus on the 2-3 most impactful themes."

Gemini returns a well-structured markdown summary containing inline citations, which the script then formats into a Jekyll-compatible markdown file with appropriate YAML frontmatter.

### Automation: GitHub Actions Every Week

To make the bot truly autonomous, I leverage **GitHub Actions**. Here is a look at a simplified workflow configuration (`.github/workflows/research-bot.yml`):

```yaml
name: Automated Research Fetcher
on:
  schedule:
    - cron: '0 0 * * 0' # Midnight UTC every Sunday
  workflow_dispatch:

jobs:
  fetch_and_publish:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Run Fetcher Script
        run: python3 scripts/fetch_research.py
      - name: Commit and Push Changes
        run: |
          git config --global user.name "Research Bot"
          git config --global user.email "bot@researchhub.local"
          git add _research/*
          git commit -m "Automated update: Added new research [skip ci]" || echo "No changes to commit"
          git push
```

Every week, the GitHub Action provisions an Ubuntu runner, sets up Python 3.10, and executes the fetcher script. The `GEMINI_API_KEY` is securely injected as a repository secret. If the script detects new papers and generates a new markdown digest in the `_research/` directory, the workflow automatically commits and pushes the file back to the `main` branch. 

### Presentation: Jekyll Collections

With the markdown files committed to the `_research/` directory, my website's Jekyll configuration handles the rest. By defining a custom collection in `_config.yml`:

```yaml
collections:
  research:
    output: true
    permalink: /research/:year/:month/:day/:title.html
```

The site automatically renders the AI-generated digests alongside my portfolio and blog under the `/research/` route. The process is completely hands-off. The bot finds the research, writes the summary, and publishes the page, ensuring that my research hub is always up to date!
