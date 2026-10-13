_Last updated at: 2026-10-13_

# **Create MCP**

Supports creating an MCP under a specified organization and fetching the tools exposed by the MCP Server. You can use this endpoint to create an MCP under a specified organization and fetch the tools exposed by the MCP Server.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/org/mcp/create`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication, and requires the calling account to have organization MCP creation permission.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/org/mcp/create' \
-H 'Authorization: Basic ${BASIC_TOKEN}' \
-H 'Content-Type: application/json' \
-d '{
  "org_id": "p-xxxx",
  "name": "crm-mcp",
  "display_name": "CRM MCP",
  "description": "CRM MCP server",
  "logo": "https://cdn.example.com/mcp.png",
  "url": "https://mcp.example.com/sse",
  "show_request": true,
  "mcp_transport_type": "SSE",
  "headers": [{"key": "Authorization", "value": "Bearer token"}],
  "queries": [{"key": "tenant", "value": "demo"}]
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
| name | String | Yes | MCP name, up to 20 characters. |
| display\_name | String | No | MCP display name, up to 50 characters. |
| description | String | Yes | MCP description, up to 100 characters. |
| logo | String | Yes | MCP icon URL. |
| url | String | Yes | MCP Server URL, must be a public `http/https` address. |
| show\_request | Boolean | Yes | Whether to display the request content during the call. |
| mcp\_transport\_type | String | Yes | MCP transport type, supports `SSE`, `STREAMABLE_HTTP`. |
| headers | Object[] | No | MCP request headers, up to 10; each item contains `key` and `value`. |
| queries | Object[] | No | MCP query parameters, up to 30; each item contains `key` and `value`. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "mcp_id": "mcp-xxxx",
    "available": true,
    "action_count": 3
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| mcp\_id | String | The newly created MCP ID. |
| available | Boolean | Whether the MCP is available. |
| action\_count | Integer | Number of Actions fetched. |

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
