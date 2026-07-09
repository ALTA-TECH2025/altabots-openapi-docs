_Last updated at: 2025-10-20_

# **Create Database Table**

Supports creating new database tables and their fields for the Agent via this API.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/database/create-table`

## **Authentication**

For details, refer to the authentication method description in API Overview.

## **Request**

### **Request Example**

```bash
curl -X POST https://altatech.ai/v1/database/create-table \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "test_api",
    "description": "Test all database APIs",
    "fields": [
        {
            "name": "id",
            "description": "id",
            "type": "TEXT",
            "required": true,
            "unique": true
        },
        {
            "name": "boolean",
            "description": "boolean",
            "type": "BOOLEAN",
            "required": true,
            "unique": false
        },
        {
            "name": "int",
            "description": "int",
            "type": "INT",
            "required": true,
            "unique": true
        },
        {
            "name": "datetime",
            "description": "datetime",
            "type": "DATETIME",
            "required": true,
            "unique": false
        },
        {
            "name": "float",
            "description": "float",
            "type": "FLOAT",
            "required": false,
            "unique": false
        }
    ]
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Obtain the token from the API key page. |
| Content-Type | application/json | Data type, set to application/json. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| name | string | Yes | Table name: 64 characters, a~z/numbers and underscores, starting with a letter. |
| description | string | Yes | Table description: 128 characters, to help LLM understand the data structure of the table. |
| fields | array | Yes | Array of table fields. |
| fields[].name | string | Yes | Field name: 34 characters, a~z/numbers and underscores. |
| fields[].description | string | Yes | Field description: 128 characters, to help LLM understand the data structure of the table. |
| fields[].type | string | Yes | Data type: TEXT/INT/FLOAT/DATETIME/BOOLEAN. |
| fields[].required | boolean | No | Required: true/false. |
| fields[].unique | boolean | No | Unique: true/false. |

### **Response**

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Message type code. |
| message | string | Message description. |
| data | object | Response content, the unique identifier of the data table. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Invalid parameters |
| 40008 | Agent RPM request limit exceeded. Please contact the service provider to increase the limit. |
| 40127 | Developer authentication failed |
| 40353 | This feature is only available after upgrading your plan |
| 403100 | Invalid table name |
| 403103 | Invalid field name |
| 50000 | Internal system error |
