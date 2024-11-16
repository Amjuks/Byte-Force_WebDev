async function showTagPhrase() {
    fetch('https://cors-anywhere.herokuapp.com/https://ipapi.co/json/', {
        headers: {
          'Origin': 'https://example.com', // Replace with your website's URL
          'X-Requested-With': 'XMLHttpRequest'
        }
      })
    .then(response => response.json())
    .then(data => console.log(data.country_code, data.country))
    .catch(error => console.error('Error:', error));  
}

document.addEventListener('DOMContentLoaded', async () => {
    const tagPhrase = document.getElementById('tagPhrase');
    tagPhrase.textContent = await showTagPhrase();
})