_Last updated at: 2025-10-20_

# **Agent Response Feedback**

Feedback on Agent responses to help Agent developers optimize.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/message/feedback`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```
curl -X POST https://altatech.ai/v1/message/feedback \ 
  -H 'Authorization: Bearer your_apikey' \ 
  -H 'Content-Type: application/json' \ 
  -d '{
        "answer_id": "123456789",
			"feedback": "POSITIVE"
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
| answer\_id | string | Yes | Message ID of Agent response. |
| feedback | string | Yes | Feedback on Agent response. \- POSITIVE: Positive, Like, Thumbs up, Approval \- NEGATIVE: Negative, Dislike, Thumbs down, Disapproval \- CANCELED: Cancel feedback |

## **Response**

### **Response Example**

```
{
    "affectCount": 0
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| affectCount | long | The number of successful feedback. It's 1 if succeed. |

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
