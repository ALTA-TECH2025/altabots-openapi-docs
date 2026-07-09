_Last updated at: 2026-07-09_

# **List Database Tables**

Supports retrieving the list of all database tables under a specified Agent or Workflow via this API. It returns the basic information of each table (name, description, field number, record count, etc.).

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/database/tables/page`

## **Authentication**

For details, refer to the authentication method description in API Overview.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/database/tables/page' \
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json' \
-d '{
    "agent_id": "680d1a2b3c4d5e6f7a8b9c0d"
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${API Key} | Use Authorization: Bearer ${API Key} for authentication. Get API key from API Key page. |
| Content-Type | application/json | Data type, value is application/json. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| agent_id | string | Yes | You can pass either agent_id or workflow_id. |

## **Response**

### **Response Example**

```
{
    "tables": [
        {
            "table_id": "680d1a2b3c4d5e6f7a8b9c0d",
            "name": "Customer Info Table",
            "description": "Stores basic customer information",
            "field_number": 8,
            "record_count": 1250
        },
        {
            "table_id": "680d1a2b3c4d5e6f7a8b9c0e",
            "name": "Order Table",
            "description": "Stores order data",
            "field_number": 12,
            "record_count": 5430
        }
    ]
}
```

### **Successful Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| tables | list | Database table list. |
| table_id | string | Unique identifier of the database table. |
| name | string | Table name. |
| description | string | Table description. |
| field_number | int | Number of fields. |
| record_count | int | Record count (number of data rows). |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error description. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Invalid parameters |
| 50000 | Internal system error |
