_Last updated at: 2026-10-13_

# **Create Tool**

Supports creating a Tool under a specified organization and automatically generating actions from an OpenAPI Schema. You can use this endpoint to create a Tool under a specified organization. When `api_schema` is provided, actions are generated at the same time; when it is not provided, only a Tool shell is created.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/org/tool/create`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication, and requires the calling account to have organization Tool creation permission.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/org/tool/create' \
-H 'Authorization: Basic ${BASIC_TOKEN}' \
-H 'Content-Type: application/json' \
-d '{
  "org_id": "p-xxxx",
  "name": "weather",
  "display_name": "Weather Lookup",
  "description": "Query current weather by city name",
  "logo": "https://cdn.example.com/weather.png",
  "url": "https://api.example.com",
  "show_request": true,
  "api_schema": "{\"openapi\":\"3.0.0\",\"paths\":{}}"
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |
| Content-Type | application/json | Request body format. |

### **Request Parameters (Body Parameters)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| org\_id | String | Yes | Organization ID. |
| name | String | Yes | Tool name, up to 20 characters. |
| display\_name | String | No | Tool display name, up to 50 characters. |
| description | String | Yes | Tool description, up to 100 characters. |
| logo | String | Yes | Tool icon URL. |
| url | String | Yes | Tool base URL, must be a public `http/https` address. |
| show\_request | Boolean | Yes | Whether to display the request content during the call. |
| api\_schema | String | No | OpenAPI JSON Schema. When provided, actions are generated and `available=true` on success; when not provided, `available=false`. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "tool_id": "tool-xxxx",
    "name": "weather",
    "available": true
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| tool\_id | String | The newly created Tool ID. |
| name | String | Tool name. |
| available | Boolean | Whether the Tool is available. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |

### **Status Codes**

| Status Code | Description |
| :---- | :---- |
| 200 | Success |
| 400 | Parameter error |
| 401 | Unauthorized |
| 403 | Insufficient permissions |
| 429 | Too many requests |
| 500 | Server error |
