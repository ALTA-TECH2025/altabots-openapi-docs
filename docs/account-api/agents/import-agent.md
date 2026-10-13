_Last updated at: 2026-10-13_

# **Import and Create Agent**

Upload a `.bot` file and import it as an Agent under an organization. After a successful import, an API Key is created automatically, but version management is disabled by default for that key.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/org/agent/import`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication, and requires the calling account to have organization Agent creation permission.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/org/agent/import' \
-H 'Authorization: Basic ${BASIC_TOKEN}' \
-F 'file=@/path/to/agent.bot' \
-F 'org_id=p-xxxx' \
-F 'custom_name=Imported Agent' \
-F 'enable_api=true' \
-F 'group_id=group-xxxx'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |
| Content-Type | multipart/form-data | File upload form. |

### **Request Parameters (Form Data)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| file | File | Yes | `.bot` file. MultiAgent files are not supported. |
| org\_id | String | Yes | Organization ID. |
| custom\_name | String | No | Custom Agent name after import. |
| enable\_api | Boolean | No | Whether to attempt to enable the API, defaults to `true`. If the plan does not support the API, the import still succeeds and returns `api_enabled=false`. |
| group\_id | String | No | Join the specified Agent group after a successful import. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "agent_id": "bot-xxxx",
    "name": "Imported Agent",
    "bot_type": "AGENT",
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
| agent\_id | String | The Agent ID after import. |
| name | String | Agent name. |
| bot\_type | String | Agent type: `Agent`, `FlowAgent`, `LoopAgent`, `Audio`. |
| api\_key | String | The automatically created API Key, returned only once. This key does not have publishing permission; if you need to publish, you must create a Key manually (see [Create API Key](../create-api-key.md)). |
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
