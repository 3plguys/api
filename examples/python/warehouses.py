import requests

# Base URL of the 3PLGuys API
API_BASE = 'https://api.3plguys.com'

# Replace this with a valid OAuth 2.0 access token
TOKEN = 'your_access_token_here'

def get_warehouses(take=10, skip=0):
    """
    Fetches a list of warehouses from the 3PLGuys Public API.

    Args:
        take (int): Number of items to retrieve (default: 10).
        skip (int): Number of items to skip for pagination (default: 0).
    """

    # Prepare headers with the Bearer token
    headers = {
        'Authorization': f'Bearer {TOKEN}'
    }

    # Pagination parameters
    params = {
        'take': take,
        'skip': skip
    }

    # Send GET request to the /v0/warehouses endpoint
    response = requests.get(f'{API_BASE}/v0/warehouses', headers=headers, params=params)

    # Check for success
    if response.status_code == 200:
        warehouses = response.json()
        print(f"Found {len(warehouses)} warehouse(s):")
        for w in warehouses:
            print(f"- ID: {w['id']}, Name: {w['name']}, Country: {w['address']['countryCode']}")
    else:
        # Print error message if request fails
        print(f"Error {response.status_code}: {response.text}")

if __name__ == '__main__':
    get_warehouses()
