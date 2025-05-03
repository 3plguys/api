# 3PLGuys Public API Documentation

Welcome to the official documentation for the 3PLGuys Public API.

This API provides access to real-time logistics, inventory, and warehouse operations. You can query product stock, manage shipments, track tasks, and integrate with ERP systems or custom portals.

---

## 🔗 Swagger / OpenAPI

Use our OpenAPI 3.0-compliant spec to explore, generate client SDKs, or test endpoints.

* **Swagger UI:** [https://api.3plguys.com](https://api.3plguys.com)
* **OpenAPI JSON:** [https://api.3plguys.com/openapi.json](https://api.3plguys.com/openapi.json)
* **OpenAPI YAML:** [https://api.3plguys.com/openapi.yaml](https://api.3plguys.com/openapi.yaml)

Compatible with:

* Postman (Import OpenAPI)
* Insomnia
* ReDoc
* Swagger Codegen / OpenAPI Generator

---

## 🔐 Authentication (OAuth 2.0)

All endpoints require Bearer token authentication using the Authorization Code Flow.

### Steps

**Step 1: Redirect to authorize**

GET
[https://account.3plguys.com/auth/app-authorize](https://account.3plguys.com/auth/app-authorize)
?response\_type=code
\&client\_id=YOUR\_CLIENT\_ID
\&redirect\_uri=[https://yourapp.com/callback](https://yourapp.com/callback)
\&scope=inventory shipments
\&state=random\_string

**Step 2: Exchange code for tokens**

POST
[https://api.3plguys.com/oauth/token](https://api.3plguys.com/oauth/token)
Body (x-www-form-urlencoded):
grant\_type=authorization\_code
code=RECEIVED\_CODE
client\_id=YOUR\_CLIENT\_ID
client\_secret=YOUR\_CLIENT\_SECRET
redirect\_uri=[https://yourapp.com/callback](https://yourapp.com/callback)

**Step 3: Use the access token**

Header:
Authorization: Bearer YOUR\_ACCESS\_TOKEN

**Token Expiration:** 1 hour
**Refresh Token:** Valid for 30 days

---

## 🌍 API Environments

Use environment variables to switch between sandbox and production:

| Environment | URL                                                        | Purpose            | Rate Limits | Data        |
| ----------- | ---------------------------------------------------------- | ------------------ | ----------- | ----------- |
| Sandbox     | [https://sandbox.3plguys.com](https://sandbox.3plguys.com) | Testing & dev only | Higher      | Mock        |
| Production  | [https://api.3plguys.com](https://api.3plguys.com)         | Live operations    | Enforced    | Real orders |

Use separate credentials for each environment.

---

## 🚦 Rate Limits

To maintain stability and fairness:

| Endpoint Category  | Limit        | Window     |
| ------------------ | ------------ | ---------- |
| Authentication     | 10 requests  | per minute |
| Inventory Queries  | 300 requests | per minute |
| Shipment Creation  | 60 requests  | per minute |
| Webhook Management | 30 requests  | per minute |

You’ll receive these headers on every response:

* `X-RateLimit-Limit`
* `X-RateLimit-Remaining`
* `X-RateLimit-Reset`

**If limit exceeded:** `429 Too Many Requests`

---

## 📦 Payload Size Limits

| Type          | Max Size |
| ------------- | -------- |
| Request Body  | 10 MB    |
| Response Body | 25 MB    |

### Best Practices:

* Max 1000 items per batch request
* Use pagination for large queries
* Use filters to minimize payload size

---

## 🧪 Pagination Example

GET
/v0/inventory?limit=100\&page=2

Response headers:

* `X-Pagination-Total`: 1250
* `X-Pagination-Pages`: 13
* `X-Pagination-Current`: 2
* `X-Pagination-Limit`: 100

---

## 🔄 Long-Running Tasks

Some operations (e.g. bulk inventory updates) return `202 Accepted`. A task ID is provided for polling status:

GET
/v0/tasks/{taskId}

States:

* `pending`
* `processing`
* `completed`
* `failed`

---

## 🪝 Webhooks

You can register webhook endpoints to receive real-time updates:

* Inventory changes
* Shipment status
* Errors

Requirements:

* HTTPS URL
* Respond with 2xx status
* Retry logic for failures is automatic

---

## 🧰 Tools and Libraries

You can auto-generate SDKs using the OpenAPI file via:

* [OpenAPI Generator](https://openapi-generator.tech/)
* [Swagger Codegen](https://github.com/swagger-api/swagger-codegen)

---

## 🛠 Reporting Issues or Requesting Features

Use [GitHub Issues](https://github.com/3plguys/api/issues) to report:

* Bugs (include endpoint, payload, and env)
* Feature requests (with use case)
* General questions

Please include:

* Endpoint and full request info (redact tokens)
* Expected vs actual behavior
* Sandbox or Production
* Steps to reproduce

---

## 💬 Support

For direct technical questions:

* Email: [support@3plguys.com](mailto:support@3plguys.com)
* GitHub: [github.com/3plguys/api](https://github.com/3plguys/api)
