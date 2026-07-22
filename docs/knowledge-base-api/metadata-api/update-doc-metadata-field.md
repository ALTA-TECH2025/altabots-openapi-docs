_Last updated at: 2026-07-22_

# **Edit Metadata Field**

Batch edit metadata fields. Only `display_label`, `description`, and `ai_search_filter` can be changed — a field is only updated if it's passed in, otherwise it keeps its current value. Up to 50 fields can be edited per request.

Batch rules:

- Up to 50 fields can be edited per request; requests exceeding 50 are rejected entirely.
- Duplicate `id` within the request: only the first is kept, the rest are marked as failed.

## **Request Method**

`PUT`

## **Request URL**

`https://altatech.ai/v1/bot/doc/metadata/field/update`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl --location --request PUT 'https://altatech.ai/v1/bot/doc/metadata/field/update' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data '{
    "fields": [
        {
            "id": "665f1c8a9b2e4d001a3f0001",
            "display_label": "Document Category",
            "description": "Business category the document belongs to",
            "ai_search_filter": false
        }
    ]
}'
```

### **Request Header**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use `Authorization: Bearer {token}` for authentication. Get the key from the API Keys page as token. |
| Content-Type | application/json | Data type, set to `application/json`. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| fields | Array<Object> | Yes | List of fields to edit, up to 50 per request. |
| id | String | Yes | Metadata field ID, used to locate the field. |
| display_label | String | No | New display name, up to 64 characters. Only changed if passed; must be unique. |
| description | String | No | New field description, up to 50 characters. Only changed if passed. |
| ai_search_filter | Boolean | No | New AI Search filter setting. Only changed if passed. |

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
            "id": "665f1c8a9b2e4d001a3f0002",
            "success": false,
            "error_message": "display_label already exists"
        },
        {
            "id": "665f1c8a9b2e4d001a3f0001",
            "success": false,
            "error_message": "duplicate id in request"
        }
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| success_count | Integer | Number of fields edited successfully. |
| failure_count | Integer | Number of fields that failed to be edited. |
| results | Array<Object> | Per-field results, returned in request order. |
| id | String | Field ID. |
| success | Boolean | Whether the edit succeeded. |
| error_message | String | Failure reason: `display_label already exists` (display name conflicts with an existing field) / `duplicate id in request` (duplicate id within the request) / `field not found` (field does not exist). |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |
