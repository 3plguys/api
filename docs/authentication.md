# Authentication

All API requests require OAuth 2.0 authorization.

## Authorization Flow

1. Redirect user to authorize endpoint.
2. Exchange code for access token.
3. Use access token in requests.

## Example

**Step 1** – Authorize:
```

GET [https://account.3plguys.com/auth/app-authorize](https://account.3plguys.com/auth/app-authorize)
?response\_type=code
\&client\_id=YOUR\_CLIENT\_ID
\&redirect\_uri=[https://yourapp.com/callback](https://yourapp.com/callback)

```

**Step 2** – Token Exchange:
```

POST [https://api.3plguys.com/oauth/token](https://api.3plguys.com/oauth/token)
grant\_type=authorization\_code
code=CODE
client\_id=YOUR\_CLIENT\_ID
client\_secret=YOUR\_SECRET

```

**Step 3** – Use:
```

Authorization: Bearer YOUR\_TOKEN

```