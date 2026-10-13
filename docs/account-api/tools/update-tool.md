_Last updated at: 2026-10-13_

# **Update Tool**

Supports updating the basic information, API definition, and authentication information of a Tool under a specified organization. You can use this endpoint to update the basic information, API definition, and authentication information of a Tool under a specified organization.

## **Request Method**

PUT

## **Request URL**

`https://altatech.ai/v1/org/tool/update`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication, and requires the calling account to have organization Tool management permission.

## **Request**

### **Request Example**

```
curl -X PUT 'https://altatech.ai/v1/org/tool/update' \
-H 'Authorization: Basic ${BASIC_TOKEN}' \
-H 'Content-Type: application/json' \
-d '{
  "org_id": "p-xxxx",
  "tool_id": "tool-xxxx",
  "name": "weather",
  "display_name": "Weather Lookup",
  "description": "Query current weather",
  "logo": "https://cdn.example.com/weather.png",
  "url": "https://api.example.com",
  "show_request": true,
  "api_schema": "{\"openapi\":\"3.0.0\",\"paths\":{}}",
  "auth_provider": "Creator",
  "auth_type": "Bearer",
  "auth_key": "token"
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
| tool\_id | String | Yes | Tool ID. |
| name | String | Yes | Tool name, up to 20 characters. |
| display\_name | String | No | Tool display name, up to 50 characters. |
| description | String | Yes | Tool description, up to 100 characters. |
| logo | String | Yes | Tool icon URL. |
| url | String | Yes | Tool base URL, must be a public `http/https` address. |
| show\_request | Boolean | Yes | Whether to display the request content during the call. |
| api\_schema | String | No | OpenAPI JSON Schema. When not provided, the API definition is not updated. |
| auth\_provider | String | No | Authentication provider. When not provided, the authentication configuration is not updated. |
| auth\_type | String | No | Authentication type. |
| auth\_key | String | No | Authentication key or token. |
| auth\_key\_name | String | No | Authentication key display name. |
| auth\_key\_tip | String | No | Authentication key tip. |
| auth\_secret | String | No | Authentication secret. |
| auth\_secret\_name | String | No | Authentication secret display name. |
| auth\_secret\_tip | String | No | Authentication secret tip. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "affect_count": 1
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| affect\_count | Integer | Number of affected records. |

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
