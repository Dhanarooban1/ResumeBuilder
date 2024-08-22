from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Apply CORS to all routes

API_ENDPOINT = 'https://nubela.co/proxycurl/api/v2/linkedin'
API_KEY = 'P0OOCEge5a6N0m7wY7Gy2A'
HEADERS = {'Authorization': f'Bearer {API_KEY}'}
PARAMS = {
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

def fetch_profile_data():
    query_string = '&'.join([f'{key}={value}' for key, value in PARAMS.items()])
    url = f"{API_ENDPOINT}?{query_string}"
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching LinkedIn profile data: {e}")
        return None

@app.route('/fetch-profile-data')
def get_profile_data():
    data = fetch_profile_data()
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Failed to fetch profile data"}), 500

if __name__ == '__main__':
    app.run(debug=True)