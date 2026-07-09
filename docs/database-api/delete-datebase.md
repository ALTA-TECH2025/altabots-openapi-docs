_Last updated at: 2025-10-20_

# **Delete Table Data**

This API allows you to batch delete specified records from Agent database tables, with a maximum limit of 1000 records per request.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v2/database/delete/record`

## **Authentication**

Refer to the API Overview for the authentication method explanation.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v2/database/delete/record' \
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json' \
-d '{
      "table_id": "673af861ed69656ac0895b07",
      "delete_data":[
        {
          "record_id":"123456",
        },
        {  
          "filter": {
          "id": "789"
        }
      ]
    }'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Obtain the token from the API Key page. |
| Content-Type | application/json | Data type, set to application/json. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| table\_id | string | Yes | ID of the table. |
| delete\_data | array | Yes | Array of records to delete. |
| record\_id | string | No | Choose either record\_id or filter condition. record\_id is recommended. |
| filter | map | No | Custom filter conditions (must use custom unique primary key fields). |

Note: You must specify either record\_id or filter condition, with record\_id being the recommended option. When both are provided, record\_id takes precedence.

## **Response**

### **Response Example**

```
{
    "code": 0,
    "message": "OK"
}

```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Response code indicating the type of message. |
| message | string | Response message description. |

### **Failed Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Detailed error message. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Invalid parameters |
| 50000 | Internal system error |
| 403106 | Table not found |
| 403131 | No permission to access table |
