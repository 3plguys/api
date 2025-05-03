# 3PLGuys Public API Documentation

Welcome to the official documentation for the 3PLGuys Public API.

This API enables seamless integration with our logistics and warehouse management systems. You can use it to query inventory, manage shipments, and synchronize with external platforms.

# Swagger / OpenAPI

You can explore and test our API using Swagger UI.

- [Swagger UI](https://api.3plguys.com)
- [OpenAPI JSON](https://api.3plguys.com/openapi.json)
- [OpenAPI YAML](https://api.3plguys.com/openapi.yaml)

Use with Postman, Insomnia, Stoplight, etc.


# Authentication

All API requests require OAuth 2.0 authorization.

## Authorization Flow

1. Redirect user to authorize endpoint.
2. Exchange code for access token.
3. Use access token in requests.

## Example

**Step 1** – Authorize:

**GET**
```
https://account.3plguys.com/auth/app-authorize
?response_type=code
&client_id=YOUR_CLIENT_ID
&redirect_uri=https://yourapp.com/callback
```

**Step 2** – Token Exchange:

**POST**
```
https://api.3plguys.com/oauth/token?
grant_type=authorization_code
code=CODE
client_id=YOUR_CLIENT\_ID
client_secret=YOUR_SECRET
```

**Step 3** - Usage

```
Authorization: Bearer YOUR_TOKEN
```

# API Environments

## Production
- URL: `https://api.3plguys.com`
- Live data
- Rate limited

## Sandbox
- URL: `https://sandbox.3plguys.com`
- Mock data
- No real orders

# Rate Limits

API is rate-limited to ensure fair usage.

| Endpoint Category     | Limit           | Window     |
|-----------------------|------------------|------------|
| Authentication        | 10 requests      | per minute |
| Inventory Queries     | 300 requests     | per minute |
| Shipment Creation     | 60 requests      | per minute |
| Webhook Management    | 30 requests      | per minute |

**Error:** `429 Too Many Requests`

# Payload Size

To ensure stability, we enforce payload limits.

| Type            | Max Size |
|-----------------|----------|
| Request Body    | 10 MB    |
| Response Body   | 25 MB    |

## Batch Guidelines
- Max 1000 items per request
- Use pagination for large data



# Reporting Issues & Feature Requests

Use GitHub Issues to report:

- Bugs
- Feature ideas
- API suggestions

Please include:
- Endpoint and request
- Expected vs actual result
- Sandbox or Production environment