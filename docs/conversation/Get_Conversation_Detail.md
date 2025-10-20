_Last updated at: 2025-10-20_

# **Get Conversation Detail**

Get all message records within a specified conversation ID.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/messages`

## **Authentication**

See API Overview for authentication details.

## **Request**

### **Example Request**

```
curl -X GET 'https://altatech.ai/v1/messages?conversation_id=xxxxxx&user_id=123456&page=1&page_size=100' \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Get API key from API Key page. |
| Content-Type | application/json | Data type, set to application/json. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| conversation\_id | string | Yes | Conversation identifier. |
| page | int | Yes | Page number to retrieve. |
| page\_size | int | Yes | Number of results per page, max 100\. |

## **Response**

### **Example Response**

```json
{
  "total": 100,
  "messages": [
    {
      "message_id": "645dd86906931c4a9e0ffb1f",
      "parent_message_id": "",
      "message_type": "ANSWER", 
      "text": "Hello, I'm a customer service agent, please ask me anything.",
      "create_time": 1683871849906
    },
    {  
      "message_id": "745dd86906931c4a9e0ffb1f",
      "parent_message_id": "645dd86906931c4a9e0ffb1f",
      "message_type": "QUESTION",
      "text": "What are the features of AltaBots?",
      "create_time": 1683871849906
    },
    {
      "message_id": "845dd86906931c4a9e0ffb1f",
      "parent_message_id": "745dd86906931c4a9e0ffb1f",
      "message_type": "ANSWER",
      "text": "AltaBots is a powerful platform...",
      "create_time": 1683871849906
    }
  ] 
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| total | int | Total number of messages in conversation. |
| messages | JSON Array | Message details. |
|       message\_id | string | Unique message ID. |
|       parent\_message\_id | string | ID of parent message. |
|       message\_type | string | Message type, ANSWER or QUESTION. |
|       text | string | Message text. |
|       create\_time | long | Timestamp message was created. |

### **Failed Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Invalid parameter. |
| 40005 | Page number exceeds total. |
| 40127 | Authentication failed. |
| 40356 | Conversation does not exist. |
| 20059 | Agent deleted |
