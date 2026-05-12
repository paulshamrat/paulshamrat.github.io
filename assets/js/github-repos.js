document.addEventListener("DOMContentLoaded", function() {
    const repos = document.querySelectorAll("[data-repo]");
    
    repos.forEach(card => {
        const repoName = card.getAttribute("data-repo");
        if (!repoName) return;

        fetch(`https://api.github.com/repos/${repoName}`)
            .then(response => {
                if (!response.ok) throw new Error("Repo not found");
                return response.json();
            })
            .then(data => {
                // Update Stars
                const starEl = card.querySelector(".gh-stars");
                if (starEl) starEl.innerText = data.stargazers_count;

                // Update Forks
                const forkEl = card.querySelector(".gh-forks");
                if (forkEl) forkEl.innerText = data.forks_count;

                // Update Description if placeholder exists or is empty in data-target
                const descEl = card.querySelector(".gh-description");
                if (descEl && !descEl.innerText.trim()) {
                    descEl.innerText = data.description || "No description provided.";
                }

                // Update Language
                const langEl = card.querySelector(".gh-language");
                const langDot = card.querySelector(".gh-language-dot");
                if (data.language) {
                    if (langEl) langEl.innerText = data.language;
                    if (langDot) {
                        langDot.style.backgroundColor = getLanguageColor(data.language);
                        langDot.style.display = "inline-block";
                    }
                }
            })
            .catch(err => {
                console.error(`Error fetching data for ${repoName}:`, err);
            });
    });
});

function getLanguageColor(lang) {
    const colors = {
        "Python": "#3572A5",
        "JavaScript": "#f1e05a",
        "Jupyter Notebook": "#DA5B0B",
        "Shell": "#89e051",
        "C++": "#f34b7d",
        "HTML": "#e34c26",
        "CSS": "#563d7c",
        "R": "#198CE7"
    };
    return colors[lang] || "#8b949e";
}
