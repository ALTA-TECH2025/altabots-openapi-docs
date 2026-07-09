_Last updated at: 2026-07-09_

# **Voice to Text**

Convert input audio content to text output.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/audio-to-text`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/audio-to-text' \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/path/to/your/audio/file.mp3'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Get the key from the API Keys page as token. |
| Content-Type | multipart/form-data | Data type, set to multipart/form-data. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| file | Byte\[\] | Yes | Audio file, max 25 MB. Supported formats: mp3 |

## **Response**

### **Response Example**

```
{
  "text": "Hi, is there anything I can help you?"
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| text | string | Recognized text. |

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
| 40325 | Invalid file type, only 'm4a', 'mp3', 'webm', 'mp4', 'mpga', 'wav', 'mpeg' supported |
| 50000 | Internal server error |
| 20059 | Agent deleted |
| 200116 | Multi-modal voice input function is not turned on |
| 40353 | The function is only available after upgrading the package. |
| 40326 | limited to 25 MB |
| 20059 | bot deleted |
| 20022 | credit not enough |
