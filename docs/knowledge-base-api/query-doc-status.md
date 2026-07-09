_Last updated at: 2025-10-20_

# **Query Doc Status**

Query the status of the knowledge base document.

## **Request Method**

`GET`

## **Request URL**

`https://altatech.ai/v1/bot/data/detail/list`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl --location https://altatech.ai/v1/bot/data/detail/list?data_ids=65e18b26e121ab08cefb4a53\&data_ids=65e18b26e121ab08cefb4a5333 \
    -H 'Authorization: Bearer your_apikey' \
    -H 'Content-Type: application/json'
```
### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Get the key from the API Keys page as token. |
| Content-Type | application/json | Data type, set to application/json. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| data_ids | array | Yes | Document ID, multiple can be submitted. |

## **Response**

### **Response Example**

```json
[
    {
        "data_id": "65e18b26e121ab08cefb4a53",
        "data_status": "AVAILABLE"
    }
]
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| doc | JSON Array | Doc info. |
| data_id | string | Doc id. |
| data_status | string | Doc status. |

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
