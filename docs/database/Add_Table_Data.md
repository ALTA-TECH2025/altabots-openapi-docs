_Last updated at: 2025-10-20_

# **Add Table Data**

This API supports adding up to 1000 rows of data in a single operation to the specified Agent's data table for use and query in conversations.

**Note:**

- The value length of a field with uniqueness enabled must not exceed 256 characters.
- The value length of a field without uniqueness enabled must not exceed 4,294,967,295 characters (this is actually limited by network issues, so it is recommended to limit the data length).
- Data transmitted through the interface will be converted to CSV data. The CSV file size must not exceed 10 MB.

## **Request Method**

`POST`

## **Request URL**

`https://altatech.ai/v1/database/import/records`

## **Authentication**

Refer to the API Overview for the authentication method explanation.

## **Request**

### **Request Example**

```bash
curl -X POST https://altatech.ai/v1/database/import/records \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json' \
  -d '{
    "table_id": "673af861ed69656ac0895b07",
      "records": [
        {
                "id": "7424489",
                "name": "4455566777777"
        }, 
        {
                "id": "7852549",
                "name": "446656677665"
        }
    ]
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
| records | list | Yes | The collection of data to be imported. |
| table_id | string | Yes | ID of the table. |

**Note:**
When the data table contains unique fields, all of these unique fields must be included in the records.
The values of the unique fields in records must not be duplicated, must not be empty, and must not already exist in the database.
Otherwise, an error will be reported and the records will be discarded.

## **Response**

### **Response Example**

```json
{
    "code": 0,
    "message": "OK",
    "data": [
        "673e9cda9f7bc178002dbd9c"
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | The type code of the message. |
| message | string | Description of the message. |
| data | object | Response content, which is the unique identifier of the task. |

### **Failed Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Parameter error |
| 50000 | Internal system error |
