_Last updated at: 2025-10-20_

# **Get Total Credit Consumption**

Retrieve the total credits consumed by the Agent within a specified time range.

Note: Data can be queried for a maximum range of 365 days.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/account/bill/total`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```
curl --location 'https://altatech.ai/v1/account/bill/total?start_time=1732982400000&end_time=1735660799999' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json'
```

### **Request Header**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Get the key from the API Keys page as token. |
| Content-Type | application/json | Data type, set to application/json. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| start\_time | String | Yes | Start time. |
| end\_time | String | Yes | End time. |

## **Response**

### **Response Example**

```
{
    "start_date": "2022-02-02",
    "end_date": "2022-02-03",
    "total": 100.0000,
    "chat": 10.0000,
    "knowledge_doc_indexing": 10.0000,
    "knowledge_doc_storage": 10.0000,
    "rerank": 10.0000,
    "database_processing": 10.0000,
    "tool_call": 10.0000,
    "asr": 10.0000,
    "tts": 10.0000
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| start\_date | String | Start date. |
| end\_date | String | End date. |
| total | Number | Total credits. |
| chat | Number | Credits consumed in text conversations. |
| knowledge\_doc\_indexing | Number | Credits consumed for knowledge document indexing. |
| knowledge\_doc\_storage | Number | Credits consumed for knowledge document storage. |
| rerank | Number | Credits consumed for reranking. |
| database\_processing | Number | Credits consumed for database processing. |
| tool\_call | Number | Credits consumed for tool calls. |
| asr | Number | Credits consumed for speech-to-text. |
| tts | Number | Credits consumed for text-to-speech. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Int | Error code. |
| message | String | Error details. |
