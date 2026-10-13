_Last updated at: 2026-10-13_

# **Query Workflow Version List**

Supports querying the version history list of a target Workflow.

This endpoint authenticates with the target Workflow's own API Key, and can only be called by a Workflow that has version management permission enabled.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/workflow/version/list`

## **Request Authentication**

See Overview for authentication details. Please use the target Workflow's API Key as the token.

## **Request**

### **Request Example**

```bash
curl -X GET 'https://altatech.ai/v1/workflow/version/list' \
-H 'Authorization: Bearer ${token}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${token} | Use the target Workflow's API Key for call authentication. |

### **Request Parameters**

None.

## **Response**

### **Response Example**

```json
{
    "code": 0,
    "message": "OK",
    "data": [
        {
            "id": "bv-xxxx",
            "bot_id": "workflow-xxxx",
            "create_time": 1786327712000,
            "release_time": 1786327812000,
            "version": "v2",
            "version_desc": "Update workflow nodes",
            "version_status": "PUBLISHED",
            "creator_email": "owner@example.com"
        }
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| id | String | Version record ID. |
| bot\_id | String | Workflow ID. |
| create\_time | Long | Version creation time, millisecond timestamp. |
| release\_time | Long | Publish time, millisecond timestamp; empty if not published. |
| version | String | Version number. |
| version\_desc | String | Version description. |
| version\_status | String | Version status. |
| creator\_email | String | Creator's email. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error message. |

### **Error Codes**

| Status Code | Description |
| :---- | :---- |
| 200 | Success |
| 401 | Unauthorized |
| 403 | Insufficient permissions, or the API Key does not have version management permission enabled |
| 429 | Too many requests |
| 500 | Server error |
