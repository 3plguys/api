# Rate Limits

API is rate-limited to ensure fair usage.

| Endpoint Category     | Limit           | Window     |
|-----------------------|------------------|------------|
| Authentication        | 10 requests      | per minute |
| Inventory Queries     | 300 requests     | per minute |
| Shipment Creation     | 60 requests      | per minute |
| Webhook Management    | 30 requests      | per minute |

**Error:** `429 Too Many Requests`