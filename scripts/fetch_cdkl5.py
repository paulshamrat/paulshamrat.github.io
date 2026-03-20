import urllib.request
import urllib.parse
import json
import datetime
import os
import re
import time

def load_env():
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, val = line.strip().split('=', 1)
                    os.environ[key] = val
load_env()

def generate_human_digest(start_date, end_date, papers, api_key):
    prompt = (
        f"You are a scientific reporter writing a short Monthly Research Digest for the CDKL5 Deficiency Disorder community. "
        f"Below are the titles, authors, URLs, and abstracts of research published from {start_date} to {end_date}.\n\n"
        f"Write a CONCISE, flowing narrative of MAXIMUM 300 words that highlights the most important trends and findings. "
        f"When citing a paper in the text, you MUST use inline markdown hyperlinks using the paper's URL, like this: [Smith et al.](https://url-to-paper.com). "
        f"Do NOT list every paper. Focus on the 2-3 most impactful themes. "
        f"Avoid excessive bold formatting. Keep it accessible to informed non-specialists.\n\n"
        f"At the very start of your response, output a catchy title on its own line prefixed with EXACTLY 'TITLE: '. "
        f"Then immediately write the article.\n\nPapers:\n"
    )
    
    for i, p in enumerate(papers, 1):
        prompt += f"Paper {i}:\nTitle: {p['title']}\nAuthors: {p['authors']}\nURL: {p['url']}\nAbstract: {p.get('abstractText', 'No abstract available.')}\n\n"
        
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    
    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            text = result['candidates'][0]['content']['parts'][0]['text']
            
            # Extract title
            title_match = re.search(r'TITLE:\s*(.*)', text, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip().replace('"', "'")
                article = text.replace(title_match.group(0), '').strip()
            else:
                title = f"CDKL5 Research Digest ({start_date} to {end_date})"
                article = text.strip()
            
            # Clean up potential markdown headers at start of summary
            article = re.sub(r'^#+.*?\n', '', article).strip()
            return title, article
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return None, None

def create_digest_markdown(start_date, end_date, papers):
    target_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").strftime("%Y-%m-%d %H:%M:%S +0000")
    paper_count = len(papers)
    
    api_key = os.environ.get("GEMINI_API_KEY")
    title, article = None, None
    
    if api_key:
        print(f"Generating cohesive narrative using Gemini for {start_date} to {end_date}...")
        title, article = generate_human_digest(start_date, end_date, papers, api_key)
        time.sleep(2)
        
    if not title or not article:
        title = f"What happened in CDKL5 Research? ({start_date} to {end_date})"
        article = f"Reporting on {paper_count} new research publications discovered in the last month regarding CDKL5 Deficiency Disorder.\n\n"
        for p in papers:
            article += f"- **{p['title']}** ({p['authors']}) [Read]({p['url']})\n"
    
    import random
    BANNERS = [
        ("https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&q=80&w=1000",
         "National Cancer Institute", "https://unsplash.com/@nci"),
        ("https://images.unsplash.com/photo-1576086213369-97a306d36557?auto=format&fit=crop&q=80&w=1000",
         "Alexandr Podvalny", "https://unsplash.com/@podvalny"),
        ("https://images.unsplash.com/photo-1555255707-c07966088b7b?auto=format&fit=crop&q=80&w=1000",
         "Mohamed Nohassi", "https://unsplash.com/@coopery"),
        ("https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&q=80&w=1000",
         "Hal Gatewood", "https://unsplash.com/@halacious"),
        ("https://images.unsplash.com/photo-1628595351029-c2bf17511435?auto=format&fit=crop&q=80&w=1000",
         "Milad Fakurian", "https://unsplash.com/@fakurian")
    ]
    banner_url, banner_author, banner_author_url = random.choice(BANNERS)
    
    filename = f"{end_date}-cdkl5-research-report.md"
    safe_title = title.replace('"', "'")
    safe_summary_preview = article[:150].replace('\n', ' ') + "..."
    
    content = f"""---
layout: post
title: "{safe_title}"
date: {target_date}
categories: cdkl5
tag: "Monthly Digest"
date_range: "{start_date} to {end_date}"
paper_count: {paper_count}
summary: "{safe_summary_preview}"
image: "{banner_url}"
---

![Featured Insight]({banner_url})
*Photo by [{banner_author}]({banner_author_url}) on [Unsplash](https://unsplash.com)*

{article}

---

### References
"""
    for i, p in enumerate(papers, 1):
        content += f"{i}. {p['authors']}. **{p['title']}**. *{p['journal']}*. [Read Full Paper ↗]({p['url']})\n"

    return filename, content

def run():
    print("Generating CDKL5 Monthly Digest for the last month...")
    
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    posts_dir = os.path.join(repo_root, "_cdkl5")
    os.makedirs(posts_dir, exist_ok=True)
    
    # 1 Month interval
    today = datetime.datetime.now()
    end_dt = today
    start_dt = end_dt - datetime.timedelta(days=30)
    
    start_str = start_dt.strftime("%Y-%m-%d")
    end_str = end_dt.strftime("%Y-%m-%d")
    
    print(f"\n--- Processing Month: {start_str} to {end_str} ---")
    
    query = f'("CDKL5 Deficiency Disorder" OR "CDKL5") AND FIRST_PDATE:[{start_str} TO {end_str}]'
    url_search = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(query)}&format=json&resultType=core&pageSize=50"
    
    try:
        req = urllib.request.Request(url_search)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            results = data.get("resultList", {}).get("result", [])
            
        if not results:
            print(f"No papers found in this period. Skipping.")
            return

        print(f"Found {len(results)} papers. Compiling digest...")
        
        papers = []
        for info in results:
            p_id = info.get("id", "unknown")
            title = info.get("title", "No Title")
            pubdate = info.get("firstPublicationDate", "Unknown Date")
            journal = info.get("journalTitle") or info.get("bookOrReportDetails", {}).get("publisher", "Unknown Source")
            
            source_raw = info.get("source", "MED")
            if source_raw == "MED":
                source_db = "PubMed"
                url = f"https://pubmed.ncbi.nlm.nih.gov/{p_id}/"
            elif source_raw == "PPR":
                source_db = "Preprint"
                url = f"https://europepmc.org/article/PPR/{p_id}"
            else:
                source_db = "Europe PMC"
                url = f"https://europepmc.org/article/{source_raw}/{p_id}"
            
            authors_list = info.get("authorList", {}).get("author", [])
            authors = ", ".join([a.get("fullName", "Unknown") for a in authors_list[:3]])
            if len(authors_list) > 3:
                authors += " et al."
                
            papers.append({
                "title": title,
                "date": pubdate,
                "journal": journal,
                "authors": authors,
                "source_db": source_db,
                "url": url,
                "abstractText": info.get("abstractText", "")
            })
        
        papers.sort(key=lambda x: x["date"], reverse=True)
        filename, content = create_digest_markdown(start_str, end_str, papers)
        
        with open(os.path.join(posts_dir, filename), "w") as f:
            f.write(content)
        print(f"Successfully generated digest: {filename}")
                
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    run()
