_Last updated at: 2026-01-10_ Note: The next major update is scheduled for late January 2026.

## **Run Workflow**

After enabling the Workflow API and creating an API Key, you can run workflows by passing parameters through the API and retrieve the workflow execution results.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/workflow/invoke`

## **Authentication**

Please refer to the authentication method described in the API Overview.

## **Request**

### Request Example

```
curl -X POST 'https://altatech.ai/v1/workflow/invoke' \
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json' \
-d '{
    "userId": "<your_user_id>",
    "input": {
        <your_workflow_input_params>
    },
    "isAsync": true,
    "webhook": [
        {
            "method": "POST",
            "url": "https://example-1.com",
            "headers": {
                "Accept": "application/json",
                "Authorization": "Bearer <your_token>"
            }
        },
        {
            "method": "GET",
            "url": "https://example-2.com?fr=google",
            "headers": {
                "Accept": "application/json",
                "Authorization": "Bearer <your_token>"
            }
        }
    ]
}'
```

### Request Headers

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Authorization | Bearer ${API Key} | Yes | Use `Authorization: Bearer ${API Key}` for authentication. Please obtain the key from the API Key page as the API Key. |
| Content-Type | application/json | Yes | Data type, fixed value is `application/json`. |

### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| userId | String | No | Used to mark the user ID for this request. |
| input | Object | Yes | The "Start" node of the workflow. This object must contain input parameters that exactly match the configuration in the workflow's "Start" node. |
| isAsync | Boolean | No | Defines whether this request runs asynchronously.<br>- `true`: Asynchronous execution.<br>- `false`: (Default) Synchronous execution.<br>Note: If `true`, you can use "Query Workflow Run Result" to check the result, or send the result to the address defined in "Webhook". These two methods are not mutually exclusive. |
| webhook | Array Object | No | When performing asynchronous operations, workflow execution results can be sent to specified Webhooks. Up to 5 Webhook configurations can be defined. |
| webhook[].method | String | Yes | The request method for the Webhook. |
| webhook[].url | String | Yes | The request URL for the Webhook. |
| webhook[].headers | Object | No | Header information for the Webhook request, can be customized. |

## **Response**

### Response Example

For synchronous execution, the result example is as follows:

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

For asynchronous execution, the API will immediately return a result as follows:

```
{
    "workflowId": "xxxxxxxx",
    "workflowName": "todayNews",
    "workflowVersion": "1.0.1",
    "workflowRunId": "xxxxxxxx",
    "status": "PENDING"
}
```

You can use the obtained `workflowRunId` to asynchronously query the execution result.

### Response Body

| Field | Type | Description |
|-------|------|-------------|
| workflowId | String | Workflow ID. |
| workflowName | String | Workflow name. |
| workflowVersion | String | Workflow version number. |
| workflowRunId | String | Workflow run ID, used to uniquely identify this execution. |
| input | Object | Input content of the "Start" node, same as the `input` in the request. |
| output | Object | Output content of the "End" node, containing the workflow execution results. |
| workflowExecutionTime | Number | Workflow execution time in milliseconds. |
| status | String | Workflow invocation status, possible values include:<br>- `SUCCEED`: Success<br>- `FAILED`: Failed<br>- `PENDING`: In queue<br>- `RUNNING`: Running |
| totalCost | Number | Total credits consumed for this run. |
| totalTokens | Number | Total tokens consumed for this run. |
| startTime | Number | Start timestamp in milliseconds. |
| endTime | Number | End timestamp in milliseconds. |
