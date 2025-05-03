import requests
from token import get_access_token

# API base URLs
BASE_URL = 'https://api.3plguys.com'
CARTONS_URL = f'{BASE_URL}/v0/inventory/cartons/breakdown'
PRODUCTS_URL = f'{BASE_URL}/v0/inventory/products/breakdown'


def get_carton_breakdown(token):
    """
    Fetch carton inventory breakdown.
    """
    headers = {'Authorization': f'Bearer {token}'}
    res = requests.get(CARTONS_URL, headers=headers)

    if res.status_code == 200:
        cartons = res.json()
        print(f"📦 {len(cartons)} carton(s) found:")
        for c in cartons:
            print(f"  - {c['name']} | Qty: {c['quantity']} | Dimensions: {c['dimensions']['length']}x{c['dimensions']['width']}x{c['dimensions']['height']} mm")
    else:
        print(f"❌ Carton error: {res.status_code} - {res.text}")


def get_product_breakdown(token):
    """
    Fetch product inventory breakdown.
    """
    headers = {'Authorization': f'Bearer {token}'}
    res = requests.get(PRODUCTS_URL, headers=headers)

    if res.status_code == 200:
        products = res.json()
        print(f"📦 {len(products)} product(s) found:")
        for p in products:
            print(f"  - {p['name']} | SKU: {p['sku']} | Total Qty: {p['quantity']}")
    else:
        print(f"❌ Product error: {res.status_code} - {res.text}")


if __name__ == '__main__':
    token = get_access_token()
    if token:
        get_carton_breakdown(token)
        get_product_breakdown(token)
