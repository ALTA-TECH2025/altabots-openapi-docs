_Last updated at: 2025-10-20_

## **Update Spreadsheet Documents**

Batch update spreadsheet-type documents. The system will sequentially perform chunking/slicing, embedding/vectorization, and finally replace the old document content with the new document content, but the document ID remains unchanged.

**Note:**
- The embedding model used is the default model and cannot be defined within the API.
- Only returns the upload result, not the final embedding result. You can obtain the final result through the "Query Document Status" API.

## **Request Method**

PUT

## **Request URL**

`https://altatech.ai/v1/bot/doc/spreadsheet/update`

## **Authentication**

For details, please refer to the authentication method description in the API Overview.

## **Request**

**Request Example**

```
curl -X PUT 'https://altatech.ai/v1/bot/doc/spreadsheet/update' \
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json' \
-d '{
    "knowledge_base_id": "67457fea6f658672d6482542",
    "chunk_token": 700,
    "header_row": 5,
    "files": [
        {
            "doc_id": "67457fea6f658672d6482542",
            "file_url": "https://www.altatech.ai/doc/spreadsheet.xlsx",
            "source_url": "https://www.altatech.ai/doc/spreadsheet.xlsx",
            "file_name": "spreadsheet_1.pdf"
        }
    ]
}'
```

**Request Headers**

| Field | Type | Description |
|-------|------|-------------|
| Authorization | Bearer ${API Key} | Use Authorization: Bearer ${API Key} for authentication. Please obtain the key from the API Keys page as the API Key. |
| Content-Type | application/json | Data type, value is application/json. |

**Request Body**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| files | Array<Object> | Yes | List of documents to update. Maximum 20 documents can be updated simultaneously. |
| doc_id | String | Yes | ID of the document to update. |
| file_url | String | No | URL of the document to add. Supported formats: csv/xls/xlsx. Maximum 10MB per document. Note: Choose either URL or base64. When both are provided, base64 takes priority. |
| file_base64 | String | No | Base64 of the document to add. Supported formats: csv/xls/xlsx. Maximum 10MB per document. Note: Choose either URL or base64. When both are provided, base64 takes priority. |
| source_url | String | No | Source URL of the document to update. Must comply with URL format specifications. If empty, the system will not update this value. To set this value to empty, please enter NULL. |
| chunk_token | Integer | No | Maximum number of tokens per knowledge chunk during chunking. Default value is 600. Range: 1-1000. |
| header_row | Integer | No | Maximum number of rows to be used as headers. Spreadsheet documents are chunked in units of "header + data rows". Default value is 1. Range: 1-5. |

## **Response**

**Response Example**

```
{
    "doc": [
        {
            "doc_id": "xxxxxx",
            "doc_name": "test_1.csv"
        },
        {
            "doc_id": "xxxxxx",
            "doc_name": "test_2.xlsx"
        }
    ],
    "failed": [
        "xxxxxx",
        "xxxxxx"
    ]
}
```

**Success Response**

| Field | Type | Description |
|-------|------|-------------|
| doc | Array<Object> | List of updated documents. |
| doc_id | String | ID of the updated document. |
| doc_name | String | Name of the updated document. |
| failed | Array<Object> | List of document IDs that failed to update. |

**Error Response**

| Field | Type | Description |
|-------|------|-------------|
| code | Integer | Error code. |
| message | String | Error details. |
