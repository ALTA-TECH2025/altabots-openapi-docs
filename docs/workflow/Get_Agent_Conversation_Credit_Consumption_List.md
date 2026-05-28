_Last updated at: 2025-10-20_

## **Get Agent Conversation Credit Consumption List**

You can use this API to retrieve detailed credit consumption records for a specified Agent within a given time range, aggregated by conversationId. Data for up to 30 days can be returned.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/account/agent/conversation/credits`

## **Authentication**

See the authentication method in the API Overview.

## **Request Example**

```
curl -X GET 'https://altatech.ai/v1/account/agent/conversation/credits?start_time=1774837924000&end_time=1775183447000&page=1&page_size=20' \
  -H 'Authorization: Bearer your_apikey'
```

## **Request Headers**

| Field         | Type           | Description                                                                                  |
|---------------|----------------|----------------------------------------------------------------------------------------------|
| Authorization | Bearer ${token} | Use `Authorization: Bearer ${token}` for authentication. Get the token from the API key page.|

## **Request Parameters**

| Field           | Type   | Required | Description                                                                                   |
|-----------------|--------|----------|-----------------------------------------------------------------------------------------------|
| start_time      | long   | Yes      | Query start time, in milliseconds timestamp.                                                   |
| end_time        | long   | Yes      | Query end time, in milliseconds timestamp. The interval between start_time and end_time cannot exceed 30 days. |
| page            | int    | No       | Page number, default is 1.                                                                    |
| page_size       | int    | No       | Number of items per page, default is 20, maximum is 100.                                      |
| conversation_id | string | No       | Conversation ID.                                                                              |

## **Response Example**

```
{
    "list": [
        {
            "conversation_id": "6830a1f2e4b0f1a2b3c4d5e6",
            "conversation_create_time": 1774838000000,
            "chat": 1.50,
            "anonymization": 0,
            "asr": 0,
            "tts": 0,
            "rerank": 0.30,
            "database_processing": 0,
            "tool_call": 0.20,
            "knowledge_doc_indexing": 0,
            "question_tag": 0,
            "moderation": 0.01,
            "total": 2.0
        }
    ],
    "total": 1,
    "page": 1,
    "page_size": 20,
    "start_time": 1774837924000,
    "end_time": 1775183447000
}
```

## **Success Response**

| Field      | Type | Description                                      |
|------------|------|--------------------------------------------------|
| list       | list | Credit consumption detail list.                  |
| total      | long | Total number of matching conversations (for pagination). |
| page       | int  | Current page number.                             |
| page_size  | int  | Number of items per page.                        |
| start_time | long | Query start time.                                |
| end_time   | long | Query end time.                                  |

## **Error Response**

| Field   | Type   | Description             |
|---------|--------|-------------------------|
| code    | int    | Error code.             |
| message | string | Error description.      |

## **Error Codes**

| Code   | Message                        |
|--------|--------------------------------|
| 40000  | Parameter error                |
| 40001  | Invalid time range (over 30 days) |
| 50000  | Internal system error          |
