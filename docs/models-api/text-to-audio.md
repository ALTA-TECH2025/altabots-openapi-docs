_Last updated at: 2025-10-20_

# **Text to Audio**

Translate the text output by the Agent into voice playback.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/text-to-audio`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```
curl -X POST https://altatech.ai/v1/text-to-audio \ 
	-H 'Authorization: Bearer your_apikey' \ 
	-H 'Content-Type: application/json' \ 
	-d '{
		"id": "Message id"
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
| id | string | Yes | Message ID. |

## **Response**

### **Response Example**

```
Byte stream, streaming return.
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
|  | Byte\[\] | Byte stream. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Invalid parameter |
| 40107 | Credentials expired |
| 40127 | Developer authentication failed |
| 40325 | Invalid file type, only 'm4a', 'mp3', 'webm', 'mp4', 'mpga', 'wav', 'mpeg' supported |
| 50000 | Internal server error |
| 40113 | Unauthorized access to Agent. |
| 20059 | Agent deleted |
| 40371 | Voice content is empty |
| 40379 | Credit not enough |
