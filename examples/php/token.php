<?php

$clientId = 'your_client_id';
$clientSecret = 'your_client_secret';
$redirectUri = 'your_redirect_uri';
$authCode = 'your_authorization_code';

$data = http_build_query([
    'grant_type' => 'authorization_code',
    'code' => $authCode,
    'client_id' => $clientId,
    'client_secret' => $clientSecret,
    'redirect_uri' => $redirectUri
]);

$ch = curl_init('https://api.3plguys.com/oauth/token');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/x-www-form-urlencoded']);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($code === 200) {
    $json = json_decode($response, true);
    echo "✅ Access token: " . $json['access_token'] . "\n";
} else {
    echo "❌ Token error $code: $response\n";
}
