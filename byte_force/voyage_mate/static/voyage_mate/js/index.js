async function getCountry() {
    try {
        // Get the IP address
        const ipResponse = await fetch('https://api.ipify.org/?format=json');
        if (!ipResponse.ok) {
            throw new Error('Failed to fetch IP address');
        }
        const ipData = await ipResponse.json();
        const ip = ipData.ip;

        // Fetch the country information
        const geoResponse = await fetch(`https://ipinfo.io/${ip}/geo`);
        if (!geoResponse.ok) {
            throw new Error('Failed to fetch geo information');
        }
        const geoData = await geoResponse.json();
        return geoData.country;
    } catch (error) {
        console.error(error);
        return null;
    }
}

// Usage example
getCountry().then(country => console.log('Country:', country));

// pop ups

const messages = [
    "Pack your bags, adventure awaits! ✈️",
    "Don’t forget to pack your sunscreen for the beach!",
    "Jet lag is just a myth... until you get there. 😜",
    "Your passport is more valuable than gold. 🌍",
    "Time to wander and get lost... on purpose! 🌏",
    "Don’t forget to wear your adventure shoes! 👟",
    "The world is calling... and it’s saying ‘come to the beach!’ 🏖️",
    "Your next adventure is just a flight away. Buckle up! 🛫",
    "Good things come to those who travel. Ready for your next trip? 🌟",
    "The world is your oyster. Go ahead, crack it open! 🦪",
    "Taking off to new destinations… The sky’s the limit! 🌈",
    "Pack light, travel far, and make memories! 🌍",
    "Exploring the world one passport stamp at a time! 📸",
    "Don’t worry, the plane won’t leave without you. Maybe. 😅",
    "Catch flights, not feelings… but feel free to catch the sunsets. 🌅",
    "Your luggage is packed, your heart is ready… let’s go! 💼"
  ];

  // Initialize the toast element and toast instance
  const toastElement = document.getElementById('liveToast');
  const toastBody = document.getElementById('toastBody');
  const toast = new bootstrap.Toast(toastElement);

  // Function to get a random message from the array
  function getRandomMessage() {
    const randomIndex = Math.floor(Math.random() * messages.length);
    return messages[randomIndex];
  }

  // Show the toast with a random message at specific intervals (e.g., every 5 seconds)
  setInterval(() => {
    toastBody.textContent = getRandomMessage(); // Update the message in the toast
    toast.show(); // Display the toast
  }, 1200); // 5000 milliseconds = 5 seconds

  // Optional: If you want to show the toast once when a button is clicked:
  document.getElementById('liveToastBtn').addEventListener('click', () => {
    toastBody.textContent = getRandomMessage(); // Set random message when button is clicked
    toast.show();
  });