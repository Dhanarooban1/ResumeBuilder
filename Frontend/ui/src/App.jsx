import React, { useEffect, useState, } from 'react';

function App() {
  const [profileData, setProfileData] = useState(null);

  useEffect(() => {
    // Function to fetch data from the backend
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/fetch-profile-data'); // Adjust the URL to match your Flask app's address
        const data = await response.json();
        setProfileData(data); // Set the fetched data to state
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData(); // Call the function
  }, []); // Empty dependency array means this effect runs once on mount

  return (
    <div>
 
      {profileData ? (
        <pre>{JSON.stringify(profileData, null, 2)}</pre> // Example: Displaying JSON data
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default App;