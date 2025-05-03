const axios = require('axios');

const TOKEN = 'your_access_token_here'; // Replace with valid token
const API_URL = 'https://api.3plguys.com/v0/warehouses';

async function getWarehouses(take = 10, skip = 0) {
  try {
    const res = await axios.get(API_URL, {
      headers: { Authorization: `Bearer ${TOKEN}` },
      params: { take, skip }
    });

    console.log(`Found ${res.data.length} warehouse(s):`);
    res.data.forEach(w =>
      console.log(`- ${w.name} (ID: ${w.id}) – ${w.address.city}, ${w.address.state}`)
    );
  } catch (err) {
    console.error('❌ Error:', err.response?.status, err.response?.data || err.message);
  }
}

getWarehouses();
