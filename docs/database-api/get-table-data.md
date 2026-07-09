_Last updated at: 2025-10-20_

# **Retrieve Database Records**

This API interface supports sending requests to retrieve paginated record data from a specified data table.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/database/records/page`

## **Authentication**

For details, refer to the authentication method description in API Overview.

## **Request**

### **Request Example**

```
curl -X POST https://altatech.ai/v1/database/records/page \ 
  -H 'Authorization: Bearer your_apikey' \ 
  -H 'Content-Type: application/json' \ 
  -d '{
    "table_id": "673d7d00ce119a7e9f47d152"
    "page": 1,
    "page_size": 10,
    "filter": {         // Either user-defined filter conditions or keyword must be chosen
        "id": "1",
        "int": 100
    },
    "keyword":"keyword"
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
| table\_id | string | Yes | Table ID. |
| page | int | Yes | Page number, starting from 1\. |
| page\_size | int | Yes | Number of records per page, range 1-100. |
| filter | map | No | User-defined filter condition. Must include a field with `"unique": true`, and only one field is supported. |
| keyword | string | No | Keyword, supports fuzzy search. |

## **Response**

### **Response Example**

```
{
    "code": 0,
    "message": "OK",
    "data": {
        "table_info": {
            "id": "673e9c7a9f7bc178002dbce8",
            "name": "test_api",
            "description": "Test all database APIs",
            "field_count": 5,
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
            ],
            "bot_id": "673e93aca7c4223becf6caf0",
            "project_id": "665465e2b5c78e6c7ab92d2b",
            "owner_id": "665465e2b5c78e6c7ab92d28"
        },
        "records": [
            {
                "id": "541278230707963208",
                "value": {
                    "id": "1",
                    "boolean": true,
                    "int": 1,
                    "datetime": "2029-10-01 12:00:00",
                    "float": 2024.21
                },
                "created_at": 1732156566000,
                "updated_at": 1732156607000
            }
        ],
        "total_count": 2
    }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Message type code. |
| message | string | Message description. |
| total\_count | int | Total record count. |
| records | array | Array of data records. |
| records\[\].id | string | Data ID. |
| records\[\].value | object | Data values. |
| records\[\].created\_at | long | Creation time. |
| records\[\].updated\_at | long | Update time. |
| table\_info | object | Information about the data table, including the following attributes: |

#### **tableInfo Attributes**

| Field | Type | Description |
| :---- | :---- | :---- |
| id | string | Unique identifier of the data table. |
| name | string | Data table name. |
| description | string | Data table description. |
| fieldCount | int | Number of fields. |
| fields | array | Array of fields, including detailed information for each field. |
| fields\[\].name | string | Field name. |
| fields\[\].description | string | Field description. |
| fields\[\].type | string | Data type, such as TEXT, INT, FLOAT, etc. |
| fields\[\].required | boolean | Whether the field is required. |
| fields\[\].unique | boolean | Whether the field is unique. |
| bot\_id | string | Agent ID. |
| project\_id | string | Project ID. |
| owner\_id | string | Owner ID of the data table. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Parameter error |
| 50000 | Internal system error |
| 403106 | Table not found |
| 403131 | No access to the data table |
