document.addEventListener("DOMContentLoaded", function() {
  const pubRows = document.querySelectorAll('.pub-row');
  const totalCitationsSpan = document.getElementById('total-citations-value');

  function updateTotalCitations() {
    if (!totalCitationsSpan) return;
    let total = 0;
    document.querySelectorAll('.count-value').forEach(span => {
      const val = parseInt(span.textContent);
      if (!isNaN(val)) total += val;
    });
    totalCitationsSpan.textContent = total;
  }
  
  pubRows.forEach(row => {
    const doi = row.getAttribute('data-doi');
    const countSpan = row.querySelector('.count-value');
    
    if (doi && doi.trim() !== "") {
      const cleanDoi = doi.trim();
      const encodedDoi = encodeURIComponent(cleanDoi);
      
      const currentCount = parseInt(countSpan.textContent) || 0;
      
      // Fetch and only update if the new count is HIGHER than the current (manual or old) count
      const updateValue = (newValue) => {
        const value = parseInt(newValue);
        if (!isNaN(value) && value > currentCount) {
          countSpan.textContent = value;
          updateTotalCitations();
        }
      };
      
      // Step 1: Try OpenAlex
      fetch(`https://api.openalex.org/works/https://doi.org/${cleanDoi}`)
        .then(response => {
          if (!response.ok) throw new Error('OpenAlex failed');
          return response.json();
        })
        .then(data => {
          if (data && data.cited_by_count !== undefined) {
            updateValue(data.cited_by_count);
          } else {
            throw new Error('No count in OpenAlex');
          }
        })
        .catch(() => {
          // Step 2: Fallback to Semantic Scholar
          fetch(`https://api.semanticscholar.org/graph/v1/paper/DOI:${cleanDoi}?fields=citationCount`)
            .then(res => {
              if (!res.ok) throw new Error('SS failed');
              return res.json();
            })
            .then(data => {
              if (data && data.citationCount !== undefined) {
                updateValue(data.citationCount);
              } else {
                throw new Error('No count in SS');
              }
            })
            .catch(() => {
              // Step 3: Fallback to Crossref
              fetch(`https://api.crossref.org/works/${encodedDoi}?mailto=shamratpaul@gmail.com`)
                .then(res => res.json())
                .then(data => {
                  if (data && data.message && data.message['is-referenced-by-count'] !== undefined) {
                    updateValue(data.message['is-referenced-by-count']);
                  }
                })
                .catch(e => {
                  console.error(`All APIs failed for DOI ${cleanDoi}:`, e);
                  // Keep the existing manual count if fetch fails
                });
            });
        });
    } else {
      // If no DOI, only set to '0' if it's currently '...' (no manual count)
      if (countSpan.textContent.trim() === "...") {
        countSpan.textContent = '0'; 
      }
      updateTotalCitations();
    }
  });
});
