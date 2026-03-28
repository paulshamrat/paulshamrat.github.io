let currentSort = {
  criterion: 'year',
  order: 'desc'
};

function sortPublications(criterion) {
  const bibliography = document.querySelector('.bibliography');
  if (!bibliography) {
    return;
  }

  // Use childNodes to find all <li> elements
  const items = Array.from(bibliography.children).filter(el => el.tagName === 'LI');
  
  if (items.length === 0) return;

  // Toggle order if same criterion, else reset to default for that criterion
  if (currentSort.criterion === criterion) {
    currentSort.order = currentSort.order === 'asc' ? 'desc' : 'asc';
  } else {
    currentSort.criterion = criterion;
    currentSort.order = (criterion === 'title') ? 'asc' : 'desc';
  }

  updateSortIcons(criterion, currentSort.order);

  items.sort((a, b) => {
    let valA, valB;

    if (criterion === 'title') {
      const rowA = a.querySelector('.pub-row');
      const rowB = b.querySelector('.pub-row');
      valA = (rowA ? rowA.getAttribute('data-title') || "" : "").toLowerCase().trim();
      valB = (rowB ? rowB.getAttribute('data-title') || "" : "").toLowerCase().trim();
      return currentSort.order === 'asc' ? valA.localeCompare(valB) : valB.localeCompare(valA);
    } 
    
    if (criterion === 'year') {
      const yearA = a.querySelector('.pub-year');
      const yearB = b.querySelector('.pub-year');
      valA = yearA ? parseInt(yearA.textContent.trim()) || 0 : 0;
      valB = yearB ? parseInt(yearB.textContent.trim()) || 0 : 0;
    } else if (criterion === 'citations') {
      const countSpanA = a.querySelector('.count-value');
      const countSpanB = b.querySelector('.count-value');
      
      const parseCite = (span) => {
        if (!span) return -1;
        let text = span.textContent.trim();
        if (text === '...' || text === '') return -1;
        // Handle cases like "12 Citations"
        let count = parseInt(text.replace(/[^0-9]/g, ''));
        return isNaN(count) ? 0 : count;
      };
      
      valA = parseCite(countSpanA);
      valB = parseCite(countSpanB);
    }

    if (currentSort.order === 'asc') {
      if (valA !== valB) return valA > valB ? 1 : -1;
    } else {
      if (valA !== valB) return valA < valB ? 1 : -1;
    }

    // Secondary sort: Title (always ascending A-Z for consistency)
    const rowA = a.querySelector('.pub-row');
    const rowB = b.querySelector('.pub-row');
    const titleA = (rowA ? rowA.getAttribute('data-title') || "" : "").toLowerCase().trim();
    const titleB = (rowB ? rowB.getAttribute('data-title') || "" : "").toLowerCase().trim();
    return titleA.localeCompare(titleB);
  });

  items.forEach(item => bibliography.appendChild(item));
}

function updateSortIcons(activeCriterion, order) {
  const criteria = ['title', 'citations', 'year'];
  
  criteria.forEach(c => {
    const header = document.getElementById(`sort-${c}`);
    if (!header) return;
    
    const icon = header.querySelector('.sort-icon');
    if (c === activeCriterion) {
      icon.className = `fa-solid fa-sort-${order === 'asc' ? 'up' : 'down'} sort-icon`;
      icon.style.opacity = "1";
    } else {
      icon.className = "fa-solid fa-sort sort-icon";
      icon.style.opacity = "0.3";
    }
  });
}

// Global exposure
window.sortPublications = sortPublications;
