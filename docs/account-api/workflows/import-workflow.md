_Last updated at: 2026-10-13_

# **Import and Create Workflow**

Upload a `.flow` file and import it as a Workflow under an organization. After a successful import, an API Key is created automatically, with version management disabled by default.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/org/workflow/import`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication, and requires the calling account to have organization Workflow creation permission.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/org/workflow/import' \
-H 'Authorization: Basic ${BASIC_TOKEN}' \
-F 'file=@/path/to/workflow.flow' \
-F 'org_id=p-xxxx' \
-F 'custom_name=Imported Workflow' \
-F 'enable_api=true'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |
| Content-Type | multipart/form-data | File upload form. |

### **Request Parameters (Form Data)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| file | File | Yes | `.flow` file. |
| org\_id | String | Yes | Organization ID. |
| custom\_name | String | No | Custom Workflow name after import. |
| enable\_api | Boolean | No | Whether to attempt to enable the API, defaults to `true`. If the plan does not support the API, the import still succeeds and returns `api_enabled=false`. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "workflow_id": "workflow-xxxx",
    "name": "Imported Workflow",
    "api_key": "app-xxxx",
    "api_enabled": true,
    "version_manage_enabled": false,
    "warning": null
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| workflow\_id | String | The Workflow ID after import. |
| name | String | Workflow name. |
| api\_key | String | The automatically created API Key, returned only once. |
| api\_enabled | Boolean | Whether the API is enabled. |
| version\_manage\_enabled | Boolean | Whether version management is allowed; disabled by default on import. |
| warning | String | Import warning. |

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
