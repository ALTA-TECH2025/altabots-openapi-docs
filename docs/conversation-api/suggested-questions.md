_Last updated at: 2025-10-20_

# **Generate Suggested Questions**

Based on the agent's response in the conversation, provide the user with several questions that can be used to continue the chat.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/next/question`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```
curl --location 'https://altatech.ai/v1/next/question?answer_id=65deb0cb2bab4d7c8061d87d' \
--header 'Authorization: Bearer your_apikey'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Get the key from the API Keys page as token. |
| Content-Type | application/json | Data type, set to application/json. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| answer\_id | string | true | Message ID of the Agent's response. |

## **Response**

### **Response Example**

```
{
    "questions": [
        "What kind of support do you need about the product?",
        "Do you have any questions about our service?",
        "Do you have any advices about our product?"
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| questions | Array | Generated questions. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Invalid parameter |
| 40379 | Credit not enough |
| 200222 | Agent configuration does not support this feature. |
| 40378 | Agent deleted |
| 20055 | API is forbidden |
| 40127 | Developer authentication failed |
