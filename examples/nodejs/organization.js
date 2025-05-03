const axios = require('axios');
const { getAccessToken } = require('./token');

async function getOrganization() {
  const token = await getAccessToken();
  if (!token) return;

  try {
    const res = await axios.get('https://api.3plguys.com/v0/organization', {
      headers: { Authorization: `Bearer ${token}` }
    });

    const org = res.data;
    console.log(`🏢 ${org.name}`);
    console.log(`Website: ${org.website}`);
    console.log(`Contact: ${org.contact.name} | ${org.contact.phoneNumber}`);
    console.log(`Address: ${org.address.addressline1}, ${org.address.city}, ${org.address.state} ${org.address.zipcode}`);
  } catch (err) {
    console.error('❌ Org error:', err.response?.status, err.response?.data || err.message);
  }
}

getOrganization();
