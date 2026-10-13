_Last updated at: 2026-10-13_

# **Refresh MCP Tool List**

Supports re-fetching the tools of a specified MCP Server and updating the actions. You can use this endpoint to re-fetch the tools of a specified MCP Server and update the actions.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/org/mcp/refresh`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication, and requires the calling account to have organization MCP management permission.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/org/mcp/refresh' \
-H 'Authorization: Basic ${BASIC_TOKEN}' \
-H 'Content-Type: application/json' \
-d '{
  "org_id": "p-xxxx",
  "id": "mcp-xxxx"
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |
| Content-Type | application/json | Request body format. |

### **Request Parameters (Body Parameters)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| org\_id | String | Yes | Organization ID. |
| id | String | Yes | MCP ID. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "mcp_id": "mcp-xxxx",
    "action_count": 3,
    "available": true
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| mcp\_id | String | MCP ID. |
| action\_count | Integer | Number of Actions after refresh. |
| available | Boolean | Whether the MCP is available. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |

### **Status Codes**

| Status Code | Description |
| :---- | :---- |
| 200 | Success |
| 400 | Parameter error |
| 401 | Unauthorized |
| 403 | Insufficient permissions |
| 429 | Too many requests |
| 500 | Server error |
