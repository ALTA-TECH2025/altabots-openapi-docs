_Last updated at: 2026-10-13_

# **Get Workflow Run List**

Used to get the run log list of a Workflow. The Workflow is determined automatically by API Key authentication, so there is no need to pass an extra `workflow_id`.

| ID Name | Description |
| :---- | :---- |
| log\_id | Workflow run log ID. |
| workflow\_run\_id | Workflow run ID, used to identify a single Workflow execution. |
| input | Input content of this Workflow run. |
| output | Output content of this Workflow run. |

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/workflow/run/logs`

## **Request Authentication**

Use the Workflow API Key for call authentication.

## **Request**

### **Request Example**

```bash
curl -X GET 'https://altatech.ai/v1/workflow/run/logs?conversation_type=API&user_id=your_user_id&start_time=1785125443602&end_time=1785125447498&page=1&page_size=10' \
-H 'Authorization: Bearer ${API Key}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${API Key} | Use Authorization: Bearer ${API Key} for authentication. Please use the Workflow API Key. |

### **Request Parameters**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| conversation\_type | string | Yes | Run source type. Supported values: `ALL`, `API`, `AGENT`, `SHARE`, `C_WORKFLOW`. Test runs (`DEBUG`) are not supported. |
| user\_id | string | No | User identifier, used to filter the Workflow run records of a specific user. |
| start\_time | number | Yes | Query start time, millisecond timestamp. |
| end\_time | number | Yes | Query end time, millisecond timestamp. |
| page | number | Yes | Page number, starting from `1`. |
| page\_size | number | Yes | Number of items per page, ranging from `10-100`. |

## **Response**

### **Response Example**

```json
{
    "list": [
        {
            "log_id": "6a66da44435da934b2e67e49",
            "workflow_run_id": "6a66da44435da934b2e67e49",
            "input": "{}",
            "output": "{\"output\":\"{\\\"text\\\":\\\"Workflow output text\\\",\\\"image\\\":[],\\\"audio\\\":[]}\"}"
        }
    ],
    "total": 1
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| list | array | Workflow run log list. |
| total | number | Total number of records matching the query conditions. |
| list[].log\_id | string | Workflow run log ID. |
| list[].workflow\_run\_id | string | Workflow run ID. |
| list[].input | string | Input content, JSON string. |
| list[].output | string | Output content, JSON string. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Parameter error |
| 40001 | Requests are too frequent |
| 40101 | Header Authorization is empty |
| 40127 | Developer authentication failed |
