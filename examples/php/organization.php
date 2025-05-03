<?php

$token = 'your_access_token_here';

$ch = curl_init('https://api.3plguys.com/v0/organization');
curl_setopt($ch, CURLOPT_HTTPHEADER, ["Authorization: Bearer $token"]);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($code === 200) {
    $org = json_decode($response, true);
    echo "🏢 " . $org['name'] . "\n";
    echo "Website: " . $org['website'] . "\n";
    echo "Contact: " . $org['contact']['name'] . " | " . $org['contact']['phoneNumber'] . "\n";
    echo "Address: " . $org['address']['addressline1'] . ", " . $org['address']['city'] . ", " .
        $org['address']['state'] . " " . $org['address']['zipcode'] . "\n";
} else {
    echo "❌ Org error $code: $response\n";
}
