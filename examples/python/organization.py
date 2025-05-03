import requests
from token import get_access_token

API_URL = 'https://api.3plguys.com/v0/organization'

def get_organization(token):
    """
    Fetches organization details from the 3PLGuys Public API.
    """
    headers = {'Authorization': f'Bearer {token}'}
    res = requests.get(API_URL, headers=headers)

    if res.status_code == 200:
        org = res.json()
        print(f"🏢 {org['name']}")
        print(f"Website: {org['website']}")
        print(f"Contact: {org['contact']['name']} | {org['contact']['phoneNumber']}")
        addr = org['address']
        print(f"Address: {addr['addressline1']}, {addr['city']}, {addr['state']} {addr['zipcode']}")
    else:
        print(f"❌ Org error {res.status_code}: {res.text}")


if __name__ == '__main__':
    token = get_access_token()
    if token:
        get_organization(token)
