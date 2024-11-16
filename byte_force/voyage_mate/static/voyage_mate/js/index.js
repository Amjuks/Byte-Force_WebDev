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