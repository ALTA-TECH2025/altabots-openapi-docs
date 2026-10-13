_Last updated at: 2026-10-13_

# **Import Agent Version**

Supports uploading a `.bot` file to replace the current Agent configuration and save it as a new version.

This endpoint authenticates with the target Agent's own API Key, and can only be called by an Agent that has version management permission enabled.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/agent/version/import`

## **Request Authentication**

Refer to API Overview for authentication instructions. Please use the target Agent's API Key as the token.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/agent/version/import' \
-H 'Authorization: Bearer ${API Key}' \
-F 'file=@/path/to/agent.bot' \
-F 'versionDesc=Update prompt and tools'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${token} | Use the target Agent's API Key for call authentication. |
| Content-Type | multipart/form-data | File upload form. |

### **Request Parameters (Form Data)**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| file | File | Yes | `.bot` file. |
| versionDesc | String | No | Version description. |

## **Response**

### **Response Example**

```
{
    "code": 0,
    "message": "OK",
    "data": {
        "botId": "bot-xxxx",
        "botType": "Agent",
        "version": "v2",
        "warning": null
    }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| botId | String | Target Agent ID. |
| botType | String | Agent type: `Agent`, `FlowAgent`, `LoopAgent`, `Audio`. |
| version | String | The saved version number, which also becomes the current version. |
| warning | String | Import warning message; null if none. |

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
