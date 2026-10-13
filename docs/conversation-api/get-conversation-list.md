_Last updated at: 2026-10-13_

# **Get Conversation List**

Retrieves information about all conversations for an Agent within specified filter criteria, including `conversation_id`, `user_id`, recent chat time, conversation subject, conversation type, total message count, and credit consumption.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/bot/conversation/page`

## **Request Authentication**

Please refer to the API Overview for authentication methods.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/bot/conversation/page?page=1&conversation_type=ALL&start_time=1691942400000&end_time=1699868066999&page_size=50&user_id=1234567890' \
-H 'Authorization: Bearer ${API Key}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${API Key} | Use Authorization: Bearer ${API Key} for authentication. Get API key from API Key page. |

### **Request Parameters**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| conversation\_type | string | Yes | Conversation ID source type. Can be set to: `ALL`, `API`, `EMBED`, and other source types. |
| user\_id | string | No | User ID. If not filled in, it is considered unrestricted. |
| start\_time | long | Yes | Start time of the recent conversation, in timestamp format. |
| end\_time | long | Yes | End time of the recent conversation, in timestamp format. |
| page | int | Yes | Page number, indicating which page to request, starting from 1\. |
| page\_size | int | Yes | Number of data entries per page, range 10-100. |

Note: For the possible values of `conversation_type`, refer to the Conversation Type Table in [User Overview](../user-api/user-overview.md).

## **Response**

### **Response Example**

```
{
  "list": [
    {
      "conversation_id": "AaACmo05Yrqb6bOSTbsg",
      "user_id": "3",
      "anonymous_id": "202607000198150",
      "recent_chat_time": 1694572952383,
      "subject": "2+3=?",
      "conversation_type": "API",
      "source_page": null,
      "message_count": 2,
      "cost_credit": 0.01,
      "bot_id": "64b902a84f1ff25d1c60c10b",
      "quality_score": null
    },
    {
      "conversation_id": "64ec1508c9c1ed5605e6ff28",
      "user_id": "33",
      "anonymous_id": "202607000198151",
      "recent_chat_time": 1693194862160,
      "subject": "Hello!",
      "conversation_type": "LIVECHAT",
      "source_page": "https://www.livechat.com/",
      "message_count": 20,
      "cost_credit": 0.59,
      "bot_id": "64b902a84f1ff25d1c60c10b",
      "quality_score": null
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
|       user\_id | string | User ID. May be null for conversations from third-party channels such as LINE or Telegram; use `anonymous_id` to identify the user in that case. |
|       anonymous\_id | string | Anonymous ID, generated automatically by AltaBots based on the user's source platform. |
|       recent\_chat\_time | long | Recent conversation time. |
|       subject | string | Conversation subject. |
|       conversation\_type | string | Conversation type. |
|       source\_page | string | The source page of the user's first message. Currently, only the LIVECHAT channel supports this field; the value is null when `conversation_type` is not `LIVECHAT`. |
|       message\_count | int | Total number of messages in the conversation. |
|       cost\_credit | float | Number of credits consumed by the conversation. |
|       bot\_id | string | Agent ID. |
|       quality\_score | float | Conversation quality score. null if the conversation has not been scored. |
| total | int | Total number of conversations matching the filter criteria (not the number returned on the current page). |

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
| 40127 | Developer authentication failed |
