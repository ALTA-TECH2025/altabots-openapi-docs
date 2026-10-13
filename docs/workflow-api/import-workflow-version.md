_Last updated at: 2026-10-13_

# **Import Workflow Version**

Supports uploading a `.flow` file to replace the current Workflow configuration and save it as a new version.

This endpoint authenticates with the target Workflow's own API Key, and can only be called by a Workflow that has version management permission enabled.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/workflow/version/import`

## **Request Authentication**

See Overview for authentication details. Please use the target Workflow's API Key as the token.

## **Request**

### **Request Example**

```bash
curl -X POST 'https://altatech.ai/v1/workflow/version/import' \
-H 'Authorization: Bearer ${token}' \
-F 'file=@/path/to/workflow.flow' \
-F 'versionDesc=Update workflow nodes'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${token} | Use the target Workflow's API Key for call authentication. |
| Content-Type | multipart/form-data | File upload form. |

### **Request Parameters (Form Data)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| file | File | Yes | `.flow` file. |
| versionDesc | String | No | Version description. |

## **Response**

### **Response Example**

```json
{
    "code": 0,
    "message": "OK",
    "data": {
        "botId": "workflow-xxxx",
        "botType": "FLOW_AGENT",
        "version": "v2",
        "warning": null
    }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| botId | String | Target Workflow ID. |
| botType | String | Bot type. |
| version | String | The saved version number, which also becomes the current version. |
| warning | String | Import warning message; `null` if none. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error message. |

### **Error Codes**

| Status Code | Description |
| :---- | :---- |
| 200 | Success |
| 400 | Parameter error |
| 401 | Unauthorized |
| 403 | Insufficient permissions, or the API Key does not have version management permission enabled |
| 429 | Too many requests |
| 500 | Server error |
