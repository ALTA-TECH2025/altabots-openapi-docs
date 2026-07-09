_Last updated at: 2025-10-20_

# **Get Correlated Dataset**

Retrieve the knowledge base data referenced by the Agent's answer.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/correlate/dataset`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```
curl -X GET 
	-H 'Authorization: Bearer your_apikey' 		
	"https://altatech.ai/v1/correlate/dataset?message_id=65e04591a0e1e42392696d78"
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
    "conversation_id": "65dc320df07244300b25b993",
    "question_id": "65dc323ef07244300b25b9c5",
    "answer_id": "65dc323ef07244300b25b9c6",
    "correlate_dataset": [
        {
            "content": "The Great Wall of China was built to resist the invasion of northern nomadic tribes.",
            "data_id": "65dc3234f07244300b25b9b9",
            "data_name": "Chinese History",
            "source_url": "https://www.example.com/chinese-history",
            "score": 0.93492633
        }
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| conversation\_id | string | Conversation ID |
| question\_id | string | Message ID of user question |
| answer\_id | string | Message ID of Agent response |
| correlate\_dataset | JSON Array | Correlate Dataset |
|     content | string | Content of knowledge slice |
|     data\_id | string | Document ID |
|     data\_name | string | Document name |
|     source\_url | string | Document source URL |
|     score | string | The semantic relevance of knowledge slices and problems. |

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
