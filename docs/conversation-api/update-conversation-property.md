_Last updated at: 2026-10-20_

# **Update Conversation Property**

Update (upsert) the conversation-level property values using the `conversation_id` parameter. Only conversation properties defined on the Agent are saved (undefined property names are ignored), and values are normalized according to the conversation property's defined type. Only the properties passed in this request are updated; other properties are not affected.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/conversation/property/update`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```
curl -X POST https://altatech.ai/v1/conversation/property/update \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json' \
  -d '{
        "conversation_id": "6a55ff78f847452309cae7d4",
        "properties": [
            { "name": "vip_level", "value": "3" },
            { "name": "user_city", "value": "Bangkok" },
            { "name": "is_member", "value": "true" }
        ]
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Get the key from the API Keys page as token. |
| Content-Type | application/json | Data type, set to application/json. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| conversation\_id | string | Yes | Conversation identifier. |
| properties | JSON Array | Yes | List of conversation properties to update. |
| properties.name | string | Yes | Conversation property name. Must be a conversation property defined on the Agent; undefined names are ignored. |
| properties.value | string | No | Conversation property value, always passed as a string: `DATETIME` as an epoch-millisecond string, `BOOLEAN` as `"true"`/`"false"`, `NUMBER`/`INTEGER` as a numeric string, `STRING` as is. The backend automatically normalizes the value according to the conversation property's defined type. |

## **Response**

### **Response Example**

```
{
    "code": 0,
    "message": "OK"
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Return code, 0 means success. |
| message | string | Description message. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Invalid parameters |
| 40127 | Developer authentication failed |
| 40356 | Conversation does not exist |
| 20059 | Agent has been deleted |
