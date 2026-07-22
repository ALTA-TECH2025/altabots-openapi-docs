_Last updated at: 2026-07-22_

# **Delete Metadata Field**

Batch delete metadata fields by ID. System-predefined fields cannot be deleted. Up to 50 fields can be deleted per request. `ids` is passed as a comma-separated URL query parameter, not in the request body.

## **Request Method**

`DELETE`

## **Request URL**

`https://altatech.ai/v1/bot/doc/metadata/field/delete`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl --location --request DELETE 'https://altatech.ai/v1/bot/doc/metadata/field/delete?ids=665f1c8a9b2e4d001a3f0001,665f1c8a9b2e4d001a3f0002' \
--header 'Authorization: Bearer YOUR_API_KEY'
```

### **Request Header**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use `Authorization: Bearer {token}` for authentication. Get the key from the API Keys page as token. |

### **Request Parameters**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| ids | String | Yes | Comma-separated field IDs, up to 50 per request. |

## **Response**

### **Response Example**

```json
{
    "success_count": 1,
    "failure_count": 2,
    "results": [
        {
            "id": "665f1c8a9b2e4d001a3f0001",
            "success": true
        },
        {
            "id": "665f1c8a9b2e4d001a3f0003",
            "success": false,
            "error_message": "field not found"
        },
        {
            "id": "665f1c8a9b2e4d001a3f0004",
            "success": false,
            "error_message": "predefined field cannot be deleted"
        }
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| success_count | Integer | Number of fields deleted successfully. |
| failure_count | Integer | Number of fields that failed to be deleted. |
| results | Array<Object> | Per-ID results. |
| id | String | Field ID. |
| success | Boolean | Whether the deletion succeeded. |
| error_message | String | Failure reason: `field not found` (field does not exist) / `predefined field cannot be deleted` (a system-predefined field). |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |
