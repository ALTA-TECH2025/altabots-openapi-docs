_Last updated at: 2025-12-15_

## **Query Workflow Run Result**

Use `workflowRunId` to query the execution result of a workflow.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/workflow/query/result`

## **Authentication**

For details, please refer to the authentication method described in the API Overview.

## **Request**

### Request Example

```
curl -X POST 'https://altatech.ai/v1/workflow/query/result' \
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json' \
-d '{
    "workflowRunId": "xxxxxxxx"
}'
```

### Request Headers

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Authorization | Bearer ${API Key} | Yes | Use `Authorization: Bearer ${API Key}` for authentication. Please obtain the key from the API Keys page to use as API Key. |
| Content-Type | application/json | Yes | Data type, fixed value is `application/json`. |

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| workflowRunId | String | Yes | The run ID of the workflow. |

## **Response**

### Response Example

```
{
    "workflowId": "xxxxxxxx",
    "workflowName": "todayNews",
    "workflowVersion": "1.0.1",
    "workflowRunId": "xxxxxxxx",
    "input": {
        "topic": "News"
    },
    "output": {
        "news": [
            {
                "summary": "Fatal crash shuts down major highway in Haleiwa. According to Emergency Medical Services, paramedics responded to the scene of the crash Wednesday morning.",
                "media": "Hawaii News Now",
                "title": "Hawaii News Now - Breaking News, Latest News, Weather & Traffic"
            },
            {
                "summary": "Hawaii Crime: Man, 65, critically injured in Waikīkī assault. Jamil Hart found guilty in Mililani murder case. HPD busts illegal gambling room in Nanakuli.",
                "media": "KHON2",
                "title": "KHON2: Hawaii News, Weather, Sports, Breaking News & Live"
            }
        ]
    },
    "workflowExecutionTime": 8347,
    "status": "SUCCEED",
    "totalCost": 0.6928,
    "totalTokens": 1745,
    "startTime": 1758765323024,
    "endTime": 1758765331373
}
```

### Response Body

| Field | Type | Description |
|-------|------|-------------|
| workflowId | String | Workflow ID. |
| workflowName | String | Workflow name. |
| workflowVersion | String | Workflow version number. |
| workflowRunId | String | Workflow run ID, used to uniquely identify this execution. |
| input | Object | Input content of the "Start" node, same as the input in the request. |
| output | Object | Output content of the "End" node, containing the workflow execution results. |
| workflowExecutionTime | Number | Workflow execution time in milliseconds. |
| status | String | Workflow execution status. Possible values include:<br>- SUCCEED: Success<br>- FAILED: Failed<br>- PENDING: In queue<br>- RUNNING: Running |
| totalCost | Number | Total credits consumed for this run. |
| totalTokens | Number | Total tokens consumed for this run. |
| startTime | Number | Start timestamp in milliseconds. |
| endTime | Number | End timestamp in milliseconds. |
