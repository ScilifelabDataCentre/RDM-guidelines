document.addEventListener('DOMContentLoaded', function () {
  const searchInput = document.getElementById('search-input');
  const searchResults = document.getElementById('search-results');

  function debounce(func, delay) {
    let timeout;
    return (...args) => {
      clearTimeout(timeout);
      timeout = setTimeout(() => func(...args), delay);
    };
  }

  let fuse = null; // delay initialization

  fetch('/search/index.json')
    .then(response => response.json())
    .then(data => {
      // Initialize Fuse.js with weighted keys (higher = priority) and adjusted threshold
      fuse = new Fuse(data, {
        keys: [
          { name: 'permalink', weight: 0.4 },
          { name: 'title', weight: 0.3 },
          { name: 'tags', weight: 0.2 },
          { name: 'summary', weight: 0.1 },
        ],
        threshold: 0.2,           // allow some fuzziness but favors close matches
        useExtendedSearch: true,  // enable exact phrase matching
        ignoreLocation: true,     // ignore the position of the query in the field
        includeScore: true,       // include scores to sort exact matches explicitly
      });
    })
    .catch(error => {
      console.error('Error fetching search index:', error);
      searchResults.innerHTML = '<p class="text-danger">Failed to load search results. Please try again later.</p>';
    });

  searchInput.addEventListener('input', debounce(() => {
    if (!fuse) {
      searchResults.innerHTML = '<p class="text-muted-dark">Initializing search...</p>';
      return;
    }
    const query = searchInput.value.trim();
    handleSearch(query);
  }, 300));

  /**
   * Handle search results and batch them into fragments before appending to DOM.
   */
  function handleSearch(query) {
    searchResults.innerHTML = '';

    if (query) {
      let results = fuse.search(query);

      if (results.length === 0) {
        searchResults.innerHTML = '<p class="text-muted-dark">No results found.</p>';
      } else {
        // Display all results using DocumentFragment
        const fragment = document.createDocumentFragment();
        const lowerQuery = query.toLowerCase();

        results.forEach(({ item }) => {
          const resultDiv = document.createElement('div');
          resultDiv.classList.add('mb-4', 'pb-3', 'border-bottom');

          const highlightedTitle = item.title.replace(
            new RegExp(`(${query})`, 'gi'),
            match => `<mark>${match}</mark>`
          );

          resultDiv.innerHTML = `
            <span class="mb-1">
              <a href="${item.permalink}">${highlightedTitle}</a>
            </span>
          `;
          fragment.appendChild(resultDiv);
        });
        searchResults.appendChild(fragment);
      }
    } else {
      searchResults.innerHTML = '<p class="text-muted-dark">Start typing to see results ...</p>';
    }
  }

  /**
   * Checks if the query is an exact match for any of the prioritized keys.
   */
  function isExactMatch(item, query) {
    const lowerQuery = query.toLowerCase();
    return ['permalink', 'title', 'summary'].some(
      key => item[key]?.toLowerCase() === lowerQuery
    ) || item.tags?.some(tag => tag.toLowerCase() === lowerQuery);
  }

  /**
   * Function to calculate priority based on field presence.
   * Higher priority = Lower numerical value.
   */
  function getPriority(item) {
    const fields = [
      { key: 'permalink', weight: 0.4 },
      { key: 'title', weight: 0.3 },
      { key: 'tags', weight: 0.2 },
      { key: 'summary', weight: 0.1 },
    ];
    const lowerQuery = searchInput.value.toLowerCase();

    return fields.reduce((priority, { key, weight }) => {
      if (key === 'tags') {
        if (item.tags?.some(tag => tag.toLowerCase().includes(lowerQuery))) {
          return Math.min(priority, 1 / weight);
        }
      } else if (item[key]?.toLowerCase().includes(lowerQuery)) {
        return Math.min(priority, 1 / weight);
      }
      return priority;
    }, Number.MAX_VALUE);
  }
});
