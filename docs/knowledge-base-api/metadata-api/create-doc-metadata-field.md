_Last updated at: 2026-07-22_

# **Create Metadata Field**

Batch create metadata fields. Omit `knowledge_base_id` to create a global field (applies to all documents under the Agent); pass it to create the field for that knowledge base only. `name` and `display_label` must each be unique.

Batch rules:

- Up to 50 fields can be created per request; requests exceeding 50 are rejected entirely.
- Duplicate entries within the request: only the first is kept, the rest are marked as failed.
- Conflicts with existing fields: the conflicting entry is dropped, the rest are written normally.

## **Request Method**

`POST`

## **Request URL**

`https://altatech.ai/v1/bot/doc/metadata/field/create`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl --location 'https://altatech.ai/v1/bot/doc/metadata/field/create' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data '{
    "knowledge_base_id": "kb_001",
    "fields": [
        {
            "name": "category",
            "display_label": "Category",
            "type": "LIST",
            "options": ["Tech", "Product"],
            "description": "Document category",
            "ai_search_filter": true
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
| knowledge_base_id | String | No | If omitted, creates a global field (all documents under the Agent); if provided, applies to that knowledge base only. The knowledge base must belong to the Agent resolved from the API Key, otherwise returns `knowledge_base_id not found`. |
| fields | Array<Object> | Yes | List of fields to create, up to 50 per request. |
| name | String | Yes | Internal field identifier. Format `^[a-z][a-z0-9_]{0,31}$` (starts with a lowercase letter, length 1-32), unique. |
| display_label | String | Yes | Display name of the field, up to 64 characters, unique. |
| type | String | Yes | Field type: STRING / NUMBER / DATETIME / LIST (case-sensitive). |
| options | Array<String> | No | Enum options. Required and non-empty when `type` is LIST. |
| description | String | No | Field description, up to 50 characters. |
| ai_search_filter | Boolean | No | Whether the field can be used as an AI Search filter. |

## **Response**

### **Response Example**

```json
{
    "success_count": 1,
    "failure_count": 2,
    "results": [
        {
            "name": "category",
            "success": true,
            "id": "665f1c8a9b2e4d001a3f0001"
        },
        {
            "name": "priority",
            "success": false,
            "error_message": "name or display_label already exists"
        },
        {
            "name": "category",
            "success": false,
            "error_message": "duplicate name in request"
        }
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| success_count | Integer | Number of fields created successfully. |
| failure_count | Integer | Number of fields that failed to be created. |
| results | Array<Object> | Per-field results, returned in request order. |
| name | String | Field name. |
| success | Boolean | Whether creation succeeded. |
| id | String | System-generated field ID (returned on success, used when editing/deleting). |
| error_message | String | Failure reason: `name or display_label already exists` (name or display_label conflicts with an existing field) / `duplicate name in request` (duplicate within the request) / `field limit exceeded` (total field limit exceeded). |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |
