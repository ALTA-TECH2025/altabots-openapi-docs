_Last updated at: 2025-12-15_

## **Workflow Execution API**

After enabling the Workflow API and creating an API Key, you can trigger a workflow via API by providing input parameters and retrieve the execution result.

---

## **HTTP Method**

POST

---

## **Endpoint**

`https://altatech.ai/v1/workflow/invoke`

---

## **Authentication**

See the Authorization section in the API Overview for details.

---

## **Request**

### **Example Request**

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

### **Request Headers**

| Field         | Type                | Required | Description                                                        |
| ------------- | ------------------- | -------- | ------------------------------------------------------------------ |
| Authorization | Bearer `${API Key}` | Yes      | Use `Authorization: Bearer ${API Key}` for request authentication. |
| Content-Type  | application/json    | Yes      | Must be `application/json`.                                        |



### **Request Body**
| Field             | Type          | Required | Description                                                                                                                                |
| ----------------- | ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| userId            | String        | No       | Used to identify the user for this request.                                                                                                |
| input             | Object        | Yes      | Corresponds to the **Start** node of the workflow. The structure must exactly match the input configuration of the workflow’s Start node.  |
| isAsync           | Boolean       | No       | Determines whether the workflow runs asynchronously. <br>• `true`: asynchronous execution <br>• `false` (default): synchronous execution   |
| webhook           | Array<Object> | No       | When executing asynchronously, workflow results can be sent to the specified webhook(s). Up to **5** webhook configurations are supported. |
| webhook[].method  | String        | Yes      | HTTP method of the webhook request.                                                                                                        |
| webhook[].url     | String        | Yes      | URL of the webhook endpoint.                                                                                                               |
| webhook[].headers | Object        | No       | Custom headers for the webhook request.                                                                                                    |

Note:
If isAsync is set to true, you can query the result via Query Workflow Run Result or receive it through the defined Webhooks. Both methods can be used simultaneously.

## **Response**
Synchronous Execution Example

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

## **Response**
Asynchronous Execution Example

```
{
  "workflowId": "xxxxxxxx",
  "workflowName": "todayNews",
  "workflowVersion": "1.0.1",
  "workflowRunId": "xxxxxxxx",
  "status": "PENDING"
}

```
you can later query the execution result using the returned workflowRunId.


### **Response Body Description**

| Field                 | Type   | Description                                                                                                                                               |
| --------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| workflowId            | String | Workflow ID.                                                                                                                                              |
| workflowName          | String | Workflow name.                                                                                                                                            |
| workflowVersion       | String | Workflow version.                                                                                                                                         |
| workflowRunId         | String | Unique ID for this workflow execution.                                                                                                                    |
| input                 | Object | Input passed to the Start node, identical to the request input.                                                                                           |
| output                | Object | Output from the End node, containing workflow results.                                                                                                    |
| workflowExecutionTime | Number | Execution time in milliseconds.                                                                                                                           |
| status                | String | Execution status: <br>• `SUCCEED` — Completed successfully <br>• `FAILED` — Execution failed <br>• `PENDING` — Queued <br>• `RUNNING` — Currently running |
| totalCost             | Number | Total credits consumed for this execution.                                                                                                                |
| totalTokens           | Number | Total tokens consumed.                                                                                                                                    |
| startTime             | Number | Start timestamp in milliseconds.                                                                                                                          |
| endTime               | Number | End timestamp in milliseconds.                                                                                                                            |


