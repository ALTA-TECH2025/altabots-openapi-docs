_Last updated at: 2025-10-20_

# **Create Conversation**

Used to request and get a conversation ID. The conversation ID is the basic carrier for users to chat with the Agent. Capabilities like chat history, long-term memory, and short-term memory are all based on the conversation ID.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/conversation`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```
curl -X POST https://altatech.ai/v1/conversation \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json' \
  -d '{
        "user_id": "your_user_id"
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
| user\_id | string | Yes | User ID defined by developer to uniquely identify a user in the Agent. Max length 32 chars. |

## **Response**

### **Response Example**

```
{
  "conversation_id": "657303a8a764d47094874bbe" 
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| conversation\_id | string | Conversation identifier. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Parameter error |
| 40127 | Developer authentication failed |
| 40378 | Agent deleted |
