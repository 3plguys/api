---
name: Bug Report
about: Report an issue or unexpected behavior in the API
title: "[Bug] "
labels: bug
assignees: ''
---
  
# Bug Report

## Description
A clear and concise description of the bug.

## API Endpoint
- URL: `https://api.3plguys.com/v1/endpoint/path`
- Method: `GET/POST/PUT/DELETE`

## Request
```json
{
  "property": "value",
  "anotherProperty": 123
}
```

## Response
Status code: `400 Bad Request`

```json
{
  "error": "Invalid request",
  "message": "Property 'x' is required"
}
```

## Expected Behavior
A clear and concise description of what you expected to happen.

## Environment
- API Version: v1.2.0
- Environment: Production/Sandbox

## Additional Context
Add any other context about the problem here.
