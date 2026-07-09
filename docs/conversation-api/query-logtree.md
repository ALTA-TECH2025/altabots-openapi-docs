_Last updated at: 2026-07-09_

# **Query LogTree**

Use this API to query the corresponding LogTree trace data by message ID.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/bot/logtree/query`

## **Request Authentication**

Refer to API Overview for authentication instructions.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/bot/logtree/query?msgid=6a475fa11d276b3d062a1be8' \
-H 'Authorization: Bearer ${API Key}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${API Key} | Use Authorization: Bearer ${API Key} for authentication. Get API key from API Key page. |

### **Request Parameters**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| msgid | String | Yes | Message ID, usually the message_id returned by the conversation API. |

## **Response**

### **Response Example**

```
{
    "treeData": [
        {
            "children": null,
            "actionId": "START_001",
            "traceId": "lyyqYMnfFSW5vWF5qdj5lR0t0DpjQR3icJi1lxm2CvUWpW8oI1-1783062433496",
            "msgId": "6a475fa11d276b3d062a1be8",
            "botId": "664ed07a277ef442b132feba",
            "logComponentId": "1lwSWOnjxuQK",
            "logComponentName": "Start",
            "logComponentTitle": null,
            "logComponentType": "Start",
            "isComponent": true,
            "actionType": "Start",
            "actionName": "Start",
            "startTimestampMillis": 1783062433496,
            "endTimestampMillis": 1783062433654,
            "runningStatus": "SUCCESS",
            "latencyMillis": 0,
            "input": {
                "content": [
                    {
                        "type": "Text",
                        "text": "1+1=?"
                    }
                ]
            },
            "output": {
                "content": [
                    {
                        "type": "Text",
                        "text": "1+1=?"
                    }
                ]
            },
            "inputTokens": 0,
            "outputTokens": 0,
            "totalTokens": "0",
            "extension": "{}",
            "createTime": 1783062433679,
            "uuid": "e53dcbb9-07d1-4019-9b66-e9d32b28bcbf",
            "workflowExecutionId": "",
            "parentId": "1lwSWOnjxuQK"
        }
    ],
    "summary": {
        "runningStatus": "SUCCESS",
        "botId": "664ed07a277ef442b132feba",
        "startTimestampMillis": 1783062433498,
        "endTimestampMillis": 1783062434933,
        "totalLatencyMillis": 1437,
        "totalTokens": 34,
        "stepCount": 3,
        "credit": -0.0031
    },
    "msgId": "6a475fa11d276b3d062a1be8",
    "conversationId": "6a475fa11d276b3d062a1be5",
    "traceId": "lyyqYMnfFSW5vWF5qdj5lR0t0DpjQR3icJi1lxm2CvUWpW8oI1-1783062433496"
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| treeData | Array\<Object\> | List of LogTree nodes; see the table below for node parameters. May be null when no trace data is available. |
| summary | Object | Message-level summary. May be null when no trace data is available. |
| runningStatus | String | Overall running status, e.g. SUCCESS, FAILED, RUNNING. |
| botId | String | Agent ID. |
| startTimestampMillis | Long | Start timestamp in milliseconds. |
| endTimestampMillis | Long | End timestamp in milliseconds. |
| totalLatencyMillis | Long | Total latency in milliseconds. |
| totalTokens | Long | Total number of tokens. |
| stepCount | Integer | Number of steps, derived from the number of returned LogTree nodes. |
| credit | Number | Credits consumed. May be null when no credit data is available. |
| msgId | String | Message ID. |
| conversationId | String | Conversation ID. |
| traceId | String | Trace ID. |

#### **treeData Node Parameters**

| Field | Type | Description |
| :---- | :---- | :---- |
| children | Array\<Object\> | Child nodes with the same structure as this table. May be null for leaf nodes. |
| actionId | String | Action ID. |
| traceId | String | Trace ID. |
| msgId | String | Message ID. |
| botId | String | Agent ID. |
| logComponentId | String | Component ID. |
| logComponentName | String | Component name. |
| logComponentTitle | String | Component title. |
| logComponentType | String | Component type. |
| isComponent | Boolean | Whether the node is a component node. |
| actionType | String | Action type. |
| actionName | String | Action name. |
| runningStatus | String | Running status of the node. |
| startTimestampMillis | Long | Node start timestamp in milliseconds. |
| endTimestampMillis | Long | Node end timestamp in milliseconds. |
| latencyMillis | Long | Node latency in milliseconds. |
| input | Object/String/Array | Node input. |
| output | Object/String/Array | Node output. |
| inputTokens | Integer | Number of input tokens. |
| outputTokens | Integer | Number of output tokens. |
| totalTokens | Integer/String | Total number of tokens, following the existing LogTree return type. |
| extension | String/Object | Extension information. |
| createTime | Long | Creation timestamp in milliseconds. |
| uuid | String | Unique identifier of the node. |
| workflowExecutionId | String | Workflow execution ID. |
| parentId | String | Parent node ID. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |
