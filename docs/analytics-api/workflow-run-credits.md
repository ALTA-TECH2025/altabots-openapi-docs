_Last updated at: 2026-10-20_

## **Workflow Run Credit Consumption List**

You can use this API to obtain the detailed credit consumption of a specified Workflow within a time range, aggregated by runId. Data is available for up to 30 days.

## **Request Method**

GET

## **Endpoint**

`https://altatech.ai/v1/account/workflow/run/credits`

## **Authentication**

See the Authentication section in the API Overview for details.

## **Request Frequency**

This API counts toward the per-minute quota of the organization plan's "Statistics API", shared with the other statistics APIs (including organization-level statistics APIs). If the quota is exceeded, `40008` is returned.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/account/workflow/run/credits?start_time=1774837924000&end_time=1775183447000&page=1&page_size=20' \
  -H 'Authorization: Bearer your_apikey'
```

### **Request Headers**

| Field         | Type              | Description                                                                 |
|---------------|-------------------|-----------------------------------------------------------------------------|
| Authorization | Bearer ${token}   | Use Authorization: Bearer ${token} for authentication. Obtain the token from the API key page. |

### **Request Parameters**

| Field      | Type   | Required | Description                                                                                     |
|------------|--------|----------|-------------------------------------------------------------------------------------------------|
| start_time | long   | Yes      | Query start time, in milliseconds.                                                              |
| end_time   | long   | Yes      | Query end time, in milliseconds. The interval between start_time and end_time cannot exceed 30 days. |
| page       | int    | No       | Page number, default is 1.                                                                      |
| page_size  | int    | No       | Number of items per page, default is 20, maximum is 100.                                        |
| run_id     | string | No       | Workflow run ID.                                                                                |

## **Response**

### **Response Example**

```
{
    "list": [
        {
            "run_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "run_start_time": 1774838000000,
            "chat": 2.10,
            "anonymization": 0,
            "asr": 0.50,
            "tts": 0,
            "rerank": 0.30,
            "database_processing": 0,
            "tool_call": 0.80,
            "knowledge_doc_indexing": 0,
            "question_tag": 0,
            "total": 3.70
        }
    ],
    "total": 1,
    "page": 1,
    "page_size": 20,
    "start_time": 1774837924000,
    "end_time": 1775183447000
}
```

### **Success Response**

| Field      | Type   | Description                                           |
|------------|--------|-------------------------------------------------------|
| list       | list   | List of credit consumption details.                   |
| run_id | string | Workflow run ID. |
| run_start_time | long | Workflow run start time (milliseconds timestamp); `null` if the run record has been deleted. |
| chat | decimal | Credits consumed by conversation (LLM chat). |
| anonymization | decimal | Credits consumed by anonymization. |
| asr | decimal | Credits consumed by speech recognition (ASR). |
| tts | decimal | Credits consumed by text-to-speech (TTS). |
| rerank | decimal | Credits consumed by vector re-ranking. |
| database_processing | decimal | Credits consumed by database processing. |
| tool_call | decimal | Credits consumed by tool calls. |
| knowledge_doc_indexing | decimal | Credits consumed by knowledge base indexing. |
| question_tag | decimal | Credits consumed by question tagging. |
| total | decimal | Total credits consumed by this run. |
| total      | long   | Total number of runs matching the criteria (for pagination). |
| page       | int    | Current page number.                                  |
| page_size  | int    | Number of items per page.                             |
| start_time | long   | Query start time.                                     |
| end_time   | long   | Query end time.                                       |

### **Failure Response**

| Field   | Type   | Description              |
|---------|--------|--------------------------|
| code    | int    | Error code.              |
| message | string | Error description.       |

### **Error Codes**

| Code   | Message                                 |
|--------|-----------------------------------------|
| 40000  | Parameter error                         |
| 40001  | Invalid time range (exceeds 30 days)    |
| 50000  | Internal system error                   |
