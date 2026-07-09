_Last updated at: 2025-10-20_

# **Re-embed Failed Docs**

Batch embed all documents in the Agent with a status of "Failed".

## **Request Method**

`POST`

## **Request URL**

`https://altatech.ai/v1/bot/data/retry/batch`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl -X POST https://altatech.ai/v1/bot/data/retry/batch \
    -H 'Authorization: Bearer your_apikey' \
    -H 'Content-Type: application/json' \
    -d '{}'
```
### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Get the key from the API Keys page as token. |
| Content-Type | application/json | Data type, set to application/json. |

### **Request Body**

None.

## **Response**

### **Response Example**

```json
{
    "affectCount": 0
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| affectCount | long | The number of documents re-embedded this time. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Invalid parameter |
| 40127 | Developer authentication failed |
| 20059 | Agent deleted |
