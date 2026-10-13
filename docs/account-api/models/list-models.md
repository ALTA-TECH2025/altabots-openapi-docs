_Last updated at: 2026-10-13_

# **Query Platform Model List**

Query the platform model list; passing `org_id` returns the models actually available to that organization, including the organization's self-configured models.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/model/list`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/model/list?org_id=p-xxxx&agent_type=LOOP_AGENT' \
-H 'Authorization: Basic ${BASIC_TOKEN}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |

### **Request Parameters (Query Parameters)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| org\_id | String | Yes | Organization ID. When provided, organization membership is verified and the models available to that organization are returned. |
| agent\_type | String | Yes | Agent type. Supports `AGENT`, `FLOW_AGENT`, `LOOP_AGENT`, `WORKFLOW`. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "CHAT": {
      "OPEN_AI": [
        {
          "model_name": "GPT-4o",
          "aiModelVersion": "gpt-4o",
          "modelId": "mv-xxxx",
          "capabilities": ["pluginSupport", "ImageRecognition", "jsonSchema"]
        }
      ]
    }
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| model\_name | String | Model display name. |
| aiModelVersion | String | Model version name. |
| modelId | String | Model version ID, used when other endpoints reference the model. |
| capabilities | String[] | List of model capabilities. |

Models in `data` are grouped by model category (e.g. `CHAT`) and then by provider (e.g. `OPEN_AI`).

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
