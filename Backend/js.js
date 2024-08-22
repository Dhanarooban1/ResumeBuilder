let api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
let api_key = 'P0OOCEge5a6N0m7wY7Gy2A'
let headers = {'Authorization': 'Bearer ' + api_key}
let params = {
    'linkedin_profile_url': 'https://www.linkedin.com/in/dhanarooban-life-journey/',
    'extra': 'include',
    'github_profile_id': 'include',
    'facebook_profile_id': 'include',
    'twitter_profile_id': 'include',
    'personal_contact_number': 'include',
    'personal_email': 'include',
    'inferred_salary': 'include',
    'skills': 'include',
    'use_cache': 'if-present',
    'fallback_to_cache': 'on-error',
}



const fetchProfileData = async () => {
  const corsProxy = "https://cors-anywhere.herokuapp.com/";
  const queryString = new URLSearchParams(params).toString();

  try {
      const response = await fetch(`${corsProxy}${api_endpoint}?${queryString}`, {
          method: 'GET',
          headers: headers,
      });

      if (!response.ok) {
          throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log(data);
  } catch (error) {
      console.error('Error fetching LinkedIn profile data:', error);
  }
};

fetchProfileData();



// const fetchProfileData = async () => {
//     const queryString = new URLSearchParams(params).toString();
  
//     try {
//       const response = await fetch(`${api_endpoint}?${queryString}`, {
//         method: 'GET',
//         headers: headers,
//       });
  
//       if (!response.ok) {
//         throw new Error('Network response was not ok');
//       }
  
//       const data = await response.json();
//       console.log(data);
//     } catch (error) {
//       console.error('Error fetching LinkedIn profile data:', error);
//     }
//   };
  

// fetchProfileData();