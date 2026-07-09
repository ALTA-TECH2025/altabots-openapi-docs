_Last updated at: 2025-10-20_

# **Update Table Data**

This interface allows you to update the values of specific records in the Agent data table.

```
-The total JSON request body size for updates is limited to 5MB.
-Each request can update a maximum of 100 records.
```

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v2/database/update/record`

## **Authentication**

For details, refer to the API Overview for authentication methods.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v2/database/update/record' \ 
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json' \
-d '{
      "table_id": "673af861ed69656ac0895b07",
      "is_create": true,
      "update_data":[
        {
          "record_id":"123456",
          "updated_fields": {
          "name": "andy",
          "age": "30"
        },
        {  
          "filter": {
          "id": "789"
          },
          "updated_fields": {
          "name": "mop",
          "age": "32"
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
| ----- | ----- | ----- | ----- |
| table\_id | string | Yes | Table ID. |
| is\_create | bool | No | Whether to create a new record when the target record does not exist. |
| update\_data | list | Yes | The collection of data to update. |
|  record\_id |  string |  No  |  Either record\_id or filter must be provided. record\_id is recommended. |
| filter | map | No | User-defined filter condition. Must include a field with `"unique": true`. Only one field is supported. |
| updated\_fields | list | Yes | Set of data to be updated. |

\-Either record\_id or filter must be provided, with record\_id being the recommended option. When both are provided, record\_id takes precedence.  
\-The default value of is\_create is false. When is\_create is not provided, new records will not be automatically created.  
\-When is\_create is set to true, if the record\_id or filter of a record to be updated does not exist in the data table, the record will be automatically created.

## **Response**

### **Response Example**

```
{
    "totalCount": 4,
    "success_count": 2,
    "fail_count": 2,
    "fail_detail": [
        {
            "upsert_data": {
                "record_id": "123456",
                "value": {
                    "name": "test user",
                    "email": "invalid_email"
                }
            },
            "fail_reason": "Invalid email format"
        },
        {
            "upsert_data": {
                "filter": {
                    "id": "789"
                },
                "value": {
                    "name": "test user",
                    "email": "invalid_email"
                }
            },
            "fail_reason": "Invalid email format"
        }
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| totalCount | int | Total number of records in this update operation |
| success\_count | string | Number of successfully updated records |
| fail\_count | string | Number of failed update operations |
| fail\_detail | array | Detailed information about failed updates |
| upsert\_data | 	array | The requested data for updating this row |
| fail\_reason | 	array | The reason for the failure to update this row |

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
