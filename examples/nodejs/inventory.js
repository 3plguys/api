const axios = require('axios');

const TOKEN = 'your_access_token_here';
const BASE_URL = 'https://api.3plguys.com';

async function getCartons() {
  try {
    const res = await axios.get(`${BASE_URL}/v0/inventory/cartons/breakdown`, {
      headers: { Authorization: `Bearer ${TOKEN}` }
    });

    const items = res.data; // adjust if it's wrapped in { items: [...] }
    console.log(`📦 ${items.length} carton(s):`);
    items.forEach(c => {
      const d = c.dimensions;
      console.log(`- ${c.name} | Qty: ${c.quantity} | ${d.length}x${d.width}x${d.height} mm`);
    });
  } catch (err) {
    console.error('❌ Carton error:', err.response?.status, err.response?.data || err.message);
  }
}

async function getProducts() {
  try {
    const res = await axios.get(`${BASE_URL}/v0/inventory/products/breakdown`, {
      headers: { Authorization: `Bearer ${TOKEN}` }
    });

    const items = res.data; // adjust if wrapped
    console.log(`📦 ${items.length} product(s):`);
    items.forEach(p => {
      console.log(`- ${p.name} | SKU: ${p.sku} | Qty: ${p.quantity}`);
    });
  } catch (err) {
    console.error('❌ Product error:', err.response?.status, err.response?.data || err.message);
  }
}

getCartons();
getProducts();
