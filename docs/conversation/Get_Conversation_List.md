_Last updated at: 2025-10-20_

# **Get Conversation List**

Get the list of all conversation IDs within a specified time range.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/bot/conversation/page`

## **Request Authentication**

Please refer to the API Overview for authentication methods.

## **Request**

### **Request Example**

```
curl --location 'https://altatech.ai/v1/bot/conversation/page?page=1&conversation_type=API&start_time=1691942400000&end_time=1699868066999&page_size=50&user_id=1234567890'  \
	--header 'Authorization: Bearer your_apikey' \
	--header 'Content-Type: application/json'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Get the key from the API Keys page as token. |
| Content-Type | application/json | Data type, set to application/json. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| conversation\_type | string | Yes | Conversation type. ALL \- All conversation IDs SPACE |
| user\_id | string | No | User ID. If not filled in, it is considered unrestricted. |
| start\_time | long | Yes | Start time of the recent conversation, in timestamp format. |
| end\_time | long | Yes | End time of the recent conversation, in timestamp format. |
| page | int | Yes | Page number, indicating which page to request, starting from 1\. |
| page\_size | int | Yes | Number of data entries per page, range 1-100. |

## **Response**

### **Response Example**

```
{
  "list": [
    {
      "conversation_id": "AaACmo05Yrqb6bOSTbsg",
      "user_id": "3",
      "recent_chat_time": 1694572952383,
      "subject": "2+3=?",
      "conversation_type": "API",
      "message_count": 2,
      "cost_credit": 0.01,
      "bot_id": "64b902a84f1ff25d1c60c10b"
    },
    {
      "conversation_id": "64ec1508c9c1ed5605e6ff28",
      "user_id": "33",
      "recent_chat_time": 1693194862160,
      "subject": "Hello!",
      "conversation_type": "API",
      "message_count": 20,
      "cost_credit": 0.59,
      "bot_id": "64b902a84f1ff25d1c60c10b"
    }
  ],
  "total": 2
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| list | JSON Array | List of conversations. |
|       conversation\_id | string | Conversation ID. |
|       user\_id | string | User ID. |
|       recent\_chat\_time | long | Recent conversation time. |
|       subject | string | Conversation subject. |
|       conversation\_type | string | Conversation type. |
|       message\_count | int | Total number of messages in the conversation. |
|       cost\_credit | float | Number of credits consumed by the conversation. |
|       bot\_id | string | Agent ID. |
|       total | int | Number of conversations returned. |

### **Error Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Invalid parameter |
| 20059 | Agent deleted |
