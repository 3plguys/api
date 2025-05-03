const axios = require('axios');

const CLIENT_ID = 'your_client_id';
const CLIENT_SECRET = 'your_client_secret';
const REDIRECT_URI = 'your_redirect_uri';
const AUTH_CODE = 'your_authorization_code';

async function getAccessToken() {
  try {
    const res = await axios.post('https://api.3plguys.com/oauth/token',
      new URLSearchParams({
        grant_type: 'authorization_code',
        code: AUTH_CODE,
        client_id: CLIENT_ID,
        client_secret: CLIENT_SECRET,
        redirect_uri: REDIRECT_URI
      }),
      { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
    );
    console.log('✅ Access token:', res.data.access_token);
    return res.data.access_token;
  } catch (err) {
    console.error('❌ Token error:', err.response?.status, err.response?.data || err.message);
  }
}

module.exports = { getAccessToken };
