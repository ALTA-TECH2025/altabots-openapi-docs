_Last updated at: 2025-10-20_

# **Get Q&A List**

Get the Q\&A list from the Agent chat history.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/message/qa/record/page`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```
curl --location 'https://altatech.ai/v1/message/qa/record/page?page=1&page_size=10&start_time=1732982400000&end_time=1735660799999&user_feedback=ALL' \
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
| user\_feedback | String | Yes | User feedback. ALL: All. NONE: No feedback. GOOD: Positive feedback, likes, praise. BAD: Negative feedback, dislikes, complaints. |
| start\_time | Long | Yes | The start time of the query range, in timestamp format. The query object is the time of the questions (Q) in QA. |
| end\_time | Long | Yes | The end time of the query range, in timestamp format. The query object is the time of the questions (Q) in QA. |
| page | Integer | Yes | Page number, starting from 1\. |
| page\_size | Integer | Yes | Number of documents per page. Fill in the range of 10-100. |

## **Response**

### **Response Example**

```
{
    "qa": [
        {
            "id": "xxxxxx",
            "q_time": 1699891200,
            "q": "xxxxxx",
            "a": "xxxxxx",
            "user_feedback": "GOOD",
            "convo_id": "xxxxxx",
            "convo_type": "API",
            "aid": "xxxxxx",
            "user_id": "xxxxxx"
        },
        {
            "id": "xxxxxx",
            "q_time": 1699891214,
            "q": "xxxxxx",
            "a": "xxxxxx",
            "user_feedback": "BAD",
            "convo_id": "xxxxxx",
            "convo_type": "API",
            "aid": "xxxxxx",
            "user_id": "xxxxxx"
        }
    ]
}
```

### **Success Response**

| Field Name | Type | Description |
| :---- | :---- | :---- |
| qa | Array\<Object\> | List of Q\&A. |
| id | String | ID of the Q\&A. |
| q\_time | Long | Timestamp of when the question (Q) was issued. |
| q | String | Content of the question. |
| a | String | Content of the answer. |
| user\_feedback | String | User feedback. |
| convo\_id | String | ID of the associated conversation. |
| convo\_type | String | Type of the associated conversation. |
| user\_id | String | User ID. A custom ID marked by the agent developer through third-party means, used to identify the specific identity of the user. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Int | Error code. |
| message | String | Error details. |
