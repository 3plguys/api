import requests

# === Replace these with your actual credentials ===
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'your_redirect_uri'
AUTH_CODE = 'your_authorization_code'
# ================================================

# OAuth token endpoint
TOKEN_URL = 'https://api.3plguys.com/oauth/token'


def get_access_token():
    """
    Exchanges an OAuth2 authorization code for an access token.

    Returns:
        str: Bearer token string if successful, None otherwise.
    """
    payload = {
        'grant_type': 'authorization_code',
        'code': AUTH_CODE,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI
    }

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    try:
        res = requests.post(TOKEN_URL, data=payload, headers=headers)
        res.raise_for_status()
        token = res.json()['access_token']
        print("✅ Access token retrieved.")
        return token
    except requests.RequestException as e:
        print(f"❌ Token request failed: {e}")
        return None


if __name__ == '__main__':
    get_access_token()
