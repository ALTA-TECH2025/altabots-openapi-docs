_Last updated at: 2026-10-20_

# **Get Conversation Property**

Retrieve the conversation-level property list using the `conversation_id` parameter, including the conversation property name, type, and the current conversation's value. All conversation properties defined on the Agent are returned; if a property has not been assigned a value in the current conversation, `value` falls back to the property's defined default value.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/conversation/property`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/conversation/property?conversation_id=6a55ff78f847452309cae7d4' \
  -H 'Authorization: Bearer your_apikey'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Get the key from the API Keys page as token. |

### **Request Parameters**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| conversation\_id | string | Yes | Conversation identifier. |

## **Response**

### **Response Example**

```
[
    {
        "id": "66aa1b2c3d4e5f60718293a4",
        "name": "vip_level",
        "type": "INTEGER",
        "value": "3"
    },
    {
        "id": "66aa1b2c3d4e5f60718293a5",
        "name": "user_city",
        "type": "STRING",
        "value": "Bangkok"
    },
    {
        "id": "66aa1b2c3d4e5f60718293a6",
        "name": "is_member",
        "type": "BOOLEAN",
        "value": "true"
    }
]
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| id | string | Unique identifier of the conversation property definition. |
| name | string | Conversation property name. |
| type | string | Conversation property type, values: `STRING`, `INTEGER`, `NUMBER`, `BOOLEAN`, `DATETIME`. |
| value | string | Conversation property value, always returned as a string (`DATETIME` as an epoch-millisecond string, `BOOLEAN` as `"true"`/`"false"`). If the property has been assigned a value in the current conversation, the conversation value is returned; otherwise the property's defined default value is returned. |

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
