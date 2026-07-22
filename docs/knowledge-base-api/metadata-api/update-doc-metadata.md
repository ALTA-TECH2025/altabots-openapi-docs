_Last updated at: 2026-07-22_

# **Update Doc Metadata Value**

Update metadata values on the specified documents, locating the document by document ID and the field by field name. Merges incrementally: only fields that are passed are changed, fields not passed are left untouched; passing an empty string `""` for a field clears its value. Up to 50 documents can be updated per request.

## **Request Method**

`PUT`

## **Request URL**

`https://altatech.ai/v1/bot/doc/metadata/update`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl --location --request PUT 'https://altatech.ai/v1/bot/doc/metadata/update' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data '{
    "documents": [
        {
            "doc_id": "doc_001",
            "metadata": { "category": "Tech", "priority": "P1" }
        },
        {
            "doc_id": "doc_002",
            "metadata": { "category": "Product", "priority": "" }
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
| documents | Array<Object> | Yes | List of documents to update, up to 50 per request. |
| doc_id | String | Yes | Document ID. |
| metadata | Object | No | `field name → value`. An empty string clears the field's value; fields not passed are left unchanged. Field names must already be defined within that document's scope. |

**Notes:**

- For LIST-type fields, only values already defined in the field's `options` can be passed; otherwise that document entry fails with `field 'x' contains value not in options`.
- Within the same request, only the first value passed for a given metadata key under the same `doc_id` is applied; any later document entry containing that duplicate key fails entirely with `duplicate metadata key 'x' for doc_id 'y'; only the first value is applied`.
- `doc_id` must belong to the Agent resolved from the API Key, otherwise returns `doc not found`.

## **Response**

### **Response Example**

```json
{
    "success_count": 1,
    "failure_count": 2,
    "results": [
        {
            "doc_id": "doc_001",
            "success": true
        },
        {
            "doc_id": "doc_002",
            "success": false,
            "error_message": "field 'priority2' is not defined"
        },
        {
            "doc_id": "doc_003",
            "success": false,
            "error_message": "doc not found"
        }
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| success_count | Integer | Number of documents updated successfully. |
| failure_count | Integer | Number of documents that failed to be updated. |
| results | Array<Object> | Per-document results. |
| doc_id | String | Document ID. |
| success | Boolean | Whether the update succeeded. |
| error_message | String | Failure reason, e.g. `doc not found` (document does not exist or does not belong to the Agent), `field 'x' is not defined` (field name is undefined), `field 'x' contains value not in options` (LIST value not in the allowed options), `duplicate metadata key 'x' for doc_id 'y'; only the first value is applied` (duplicate field within the request, first value applied). |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |
