_Last updated at: 2026-10-13_

# **Rollback Workflow Version**

Supports rolling back a specified historical Workflow version and saving it as a new version, with the option to publish immediately.

This endpoint authenticates with the target Workflow's own API Key, and can only be called by a Workflow that has version management permission enabled.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/workflow/version/rollback`

## **Request Authentication**

See Overview for authentication details. Please use the target Workflow's API Key as the token.

## **Request**

### **Request Example**

```bash
curl -X POST 'https://altatech.ai/v1/workflow/version/rollback' \
-H 'Authorization: Bearer ${token}' \
-H 'Content-Type: application/json' \
-d '{
    "version": "v1",
    "new_version": "v3",
    "release": true,
    "version_desc": "Rollback to stable workflow"
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${token} | Use the target Workflow's API Key for call authentication. |
| Content-Type | application/json | Request body format. |

### **Request Parameters (Body Parameters)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| version | String | Yes | The source version number to roll back. |
| new\_version | String | No | The new version number saved after rollback; auto-generated when empty. |
| release | Boolean | No | Whether to publish immediately after the rollback is saved. |
| version\_desc | String | No | New version description. |

## **Response**

### **Response Example**

```json
{
    "code": 0,
    "message": "OK",
    "data": {
        "source_version": "v1",
        "new_version": "v3",
        "created": true,
        "released": true,
        "warnings": []
    }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| source\_version | String | The source version number of the rollback. |
| new\_version | String | The new version number that was saved. |
| created | Boolean | Whether a new version was created. |
| released | Boolean | Whether it has been published. |
| warnings | String[] | Rollback notes. |

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
