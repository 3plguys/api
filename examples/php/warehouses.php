<?php

$token = 'your_access_token_here'; // Replace with valid token
$url = 'https://api.3plguys.com/v0/warehouses';

$headers = [
    "Authorization: Bearer $token"
];

$query = http_build_query([
    'take' => 10,
    'skip' => 0
]);

$ch = curl_init("$url?$query");
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($code === 200) {
    $warehouses = json_decode($response, true);
    echo "Found " . count($warehouses) . " warehouse(s):\n";
    foreach ($warehouses as $w) {
        echo "- {$w['name']} (ID: {$w['id']}) – {$w['address']['city']}, {$w['address']['state']}\n";
    }
} else {
    echo "❌ Error $code: $response\n";
}
