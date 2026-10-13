_Last updated at: 2026-10-13_

# **Publish Agent Version**

Supports publishing a specified Agent version as the online production version.

This endpoint authenticates with the target Agent's own API Key, and can only be called by an Agent that has version management permission enabled.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/agent/version/release`

## **Request Authentication**

Refer to API Overview for authentication instructions. Please use the target Agent's API Key as the token.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/agent/version/release' \
-H 'Authorization: Bearer ${token}' \
-H 'Content-Type: application/json' \
-d '{
    "version": "v2"
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${token} | Use the target Agent's API Key for call authentication. |
| Content-Type | application/json | Request body format. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| version | String | Yes | The version number to publish online. |

## **Response**

### **Response Example**

```
{
    "code": 0,
    "message": "OK",
    "data": {
        "version": "v2",
        "previous_version": "v1"
    }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| version | String | The version number published this time. |
| previous\_version | String | The online version number before this publish; empty on first publish. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error message. |

### **Status Codes**

| Status Code | Description |
| :---- | :---- |
| 200 | Success |
| 400 | Parameter error |
| 401 | Unauthorized |
| 403 | Insufficient permissions, or the API Key does not have version management permission enabled |
| 429 | Too many requests |
| 500 | Server error |
