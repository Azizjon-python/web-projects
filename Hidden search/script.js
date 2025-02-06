const btn = document.querySelector('.btn');
const search = document.querySelector('.search');
const input = document.querySelector('.input');

btn.addEventListener('click', () => {
    search.classList.toggle('active');
    input.focus();
});

input.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        const query = input.value.trim();
        if (query) {
            const googleSearchURL = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
            window.open(googleSearchURL, '_blank');
        }
    }
});