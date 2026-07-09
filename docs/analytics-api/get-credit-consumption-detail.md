_Last updated at: 2025-10-20_

# **Get Detailed Credit Consumption**

Retrieve the details of Agent's credits consumption within a specified time range, returning the data by day.

Note: A maximum of 90 days of data can be queried.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/account/bill/page`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```
curl --location 'https://altatech.ai/v1/account/bill/page?page=1&page_size=10&start_time=1732982400000&end_time=1735660799999' \
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
[
    {
        "date": "2022-02-02",
        "total": 100,
        "chat": 10,
        "knowledge_doc_indexing": 10,
        "knowledge_doc_storage": 10,
        "rerank": 10,
        "database_processing": 10,
        "tool_call": 10,
        "asr": 10,
        "tts": 10
    },
    {
        "date": "2022-02-03",
        "total": 100,
        "chat": 10,
        "knowledge_doc_indexing": 10,
        "knowledge_doc_storage": 10,
        "rerank": 10,
        "database_processing": 10,
        "tool_call": 10,
        "asr": 10,
        "tts": 10
    }
]
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| start\_date | String | Start date. |
| end\_date | String | End date. |
| total | Number | Total credits. |
| chat | Number | Credits consumed in text dialogue. |
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
