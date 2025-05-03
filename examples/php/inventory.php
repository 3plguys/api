<?php

$token = 'your_access_token_here';
$base = 'https://api.3plguys.com';

function get($endpoint) {
    global $token, $base;
    $ch = curl_init("$base$endpoint");
    curl_setopt($ch, CURLOPT_HTTPHEADER, ["Authorization: Bearer $token"]);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $res = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    return [$code, $res];
}

function showCartons() {
    list($code, $res) = get('/v0/inventory/cartons/breakdown');
    if ($code === 200) {
        $cartons = json_decode($res, true);
        echo "📦 " . count($cartons) . " carton(s):\n";
        foreach ($cartons as $c) {
            $d = $c['dimensions'];
            echo "- {$c['name']} | Qty: {$c['quantity']} | {$d['length']}x{$d['width']}x{$d['height']} mm\n";
        }
    } else {
        echo "❌ Carton error $code: $res\n";
    }
}

function showProducts() {
    list($code, $res) = get('/v0/inventory/products/breakdown');
    if ($code === 200) {
        $products = json_decode($res, true);
        echo "📦 " . count($products) . " product(s):\n";
        foreach ($products as $p) {
            echo "- {$p['name']} | SKU: {$p['sku']} | Qty: {$p['quantity']}\n";
        }
    } else {
        echo "❌ Product error $code: $res\n";
    }
}

showCartons();
showProducts();
