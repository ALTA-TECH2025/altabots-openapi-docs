_Last updated at: 2026-10-13_

# **Query Tool / MCP List**

Supports querying the Tool and MCP lists under a specified organization. You can use this endpoint to query the Tool and MCP lists under a specified organization.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/org/tool/list`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/org/tool/list?org_id=p-xxxx&plugin_type=TOOL&available=true&keyword=weather' \
-H 'Authorization: Basic ${BASIC_TOKEN}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |

### **Request Parameters (Query Parameters)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| org\_id | String | Yes | Organization ID. |
| keyword | String | No | Keyword, filters by name or description. |
| plugin\_type | String | No | Resource type, supports `TOOL`, `MCP`; when not provided, both Tool and MCP are returned. |
| available | Boolean | No | Whether to return only available or unavailable resources. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": [
    {
      "resource_id": "tool-xxxx",
      "name": "weather",
      "display_name": "Weather Lookup",
      "description": "Query current weather",
      "logo": "https://cdn.example.com/weather.png",
      "url": "https://api.example.com",
      "plugin_type": "TOOL",
      "available": true,
      "action_count": 2,
      "create_time": 1785826041000,
      "update_time": 1785826041000
    }
  ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| resource\_id | String | Tool or MCP ID. |
| name | String | Resource name. |
| display\_name | String | Display name. |
| description | String | Description. |
| logo | String | Icon URL. |
| url | String | Service address. |
| plugin\_type | String | Resource type, `TOOL` or `MCP`. |
| available | Boolean | Whether it is available. |
| action\_count | Integer | Number of Actions. |
| create\_time | Long | Creation time, millisecond timestamp. |
| update\_time | Long | Update time, millisecond timestamp. |

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
