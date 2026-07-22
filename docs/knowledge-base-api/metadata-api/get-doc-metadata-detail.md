_Last updated at: 2026-07-22_

# **Get Doc Metadata**

Batch query metadata values on documents by document ID. Returns both `auto_metadata` (system-populated, read-only) and `metadata` (custom field values). Up to 50 documents can be queried per request.

## **Request Method**

`GET`

## **Request URL**

`https://altatech.ai/v1/bot/doc/metadata/detail`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl --location 'https://altatech.ai/v1/bot/doc/metadata/detail?doc_ids=doc_001,doc_002' \
--header 'Authorization: Bearer YOUR_API_KEY'
```

### **Request Header**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use `Authorization: Bearer {token}` for authentication. Get the key from the API Keys page as token. |

### **Request Parameters**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| doc_ids | String | Yes | Comma-separated document IDs, up to 50 per request. All documents must belong to the Agent resolved from the API Key; if any document does not exist or does not belong to the Agent, the whole request fails and returns `one or more doc_ids do not exist or do not belong to the current bot`. |

## **Response**

### **Response Example**

```json
{
    "documents": [
        {
            "doc_id": "doc_001",
            "auto_metadata": {
                "document_name": "API-Spec.pdf",
                "upload_time": "2026-01-15T10:30:00Z"
            },
            "metadata": {
                "category": "Tech",
                "priority": "P1"
            }
        }
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| documents | Array<Object> | Metadata for each document; documents with no metadata records are omitted. |
| doc_id | String | Document ID. |
| auto_metadata | Object | System-populated metadata (document name, upload time, uploader, source, etc.), read-only. |
| metadata | Object | Custom metadata values, formatted as `field name → value`. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |
