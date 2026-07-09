_Last updated at: 2025-10-20_

# **Get Correlated Document**

Gets the document data referenced by the Agent's answer.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/bot/data/references` 

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```
curl -X POST 
	-H 'Authorization: Bearer your_apikey' 		
	-H 'Content-Type: application/json'
	-d '{"message_id": "xxxxx"}'
	"https://altatech.ai/v1/bot/data/references"
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Get the key from the API Keys page as token. |
| Content-Type | application/json | Data type, set to application/json. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| message\_id | string | true | Message ID of Agent's response. |

## **Response**

### **Response Example**

```
{
    "code": 0,
    "msg": "success",
    "data": {
        "conversationId": "65dc320df07244300b25b993",
        "questionId": "65dc323ef07244300b25b9c5",
        "answerId": "65dc323ef07244300b25b9c6",
        "refDoc": [
            {
                "dataId": "65dc3234f07244300b25b9b9",
                "dataName": "History Reference",
                "sourceUrl": "https://www.example.com/history"
            }
        ]
    }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| conversationId | string | Conversation ID |
| questionId | string | Message ID of user question |
| answerId | string | Message ID of Agent response |
| refDoc | JSON Array | Referenced Document Data |
| dataId | string | Document ID |
| dataName | string | Document Name |
| sourceUrl | string | Document source URL |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| msg | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Invalid parameter |
| 40379 | Credit not enough |
| 40378 | Agent deleted |
| 20055 | API is forbidden |
| 40127 | Developer authentication failed |
