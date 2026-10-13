_Last updated at: 2026-10-13_

# **Precheck Agent Import File**

Precheck whether a `.bot` file can be imported, without writing business resources. The precheck only parses and security-scans the file; it does not write the Agent, API Key, skills, data groups, or plugin relationships.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/org/agent/import/precheck`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication, and requires the calling account to have organization Agent creation permission.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/org/agent/import/precheck' \
-H 'Authorization: Basic ${BASIC_TOKEN}' \
-F 'file=@/path/to/agent.bot' \
-F 'org_id=p-xxxx'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |
| Content-Type | multipart/form-data | File upload form. |

### **Request Parameters (Form Data)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| file | File | Yes | `.bot` file. |
| org\_id | String | Yes | Organization ID. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "valid": true,
    "error_message": null,
    "export_type": "BOT",
    "bot_type": "Agent",
    "name": "Imported Agent",
    "logo": "https://cdn.example.com/agent.png",
    "introduction": "Agent introduction",
    "format_version": "1.0"
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| valid | Boolean | Whether the file can be imported. |
| error\_message | String | Error message when the file cannot be imported. |
| export\_type | String | Export file type. |
| bot\_type | String | Agent type: `Agent`, `FlowAgent`, `LoopAgent`, `Audio`. |
| name | String | Resource name within the file. |
| logo | String | Icon URL. |
| introduction | String | Introduction. |
| format\_version | String | File format version. |

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
