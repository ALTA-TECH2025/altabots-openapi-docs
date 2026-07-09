_Last updated at: 2025-10-20_

# **Update Text Docs (file)**

Batch update documents using files. The system will sequentially perform chunking/slicing, embedding/vectorization, and finally replace the old document content with the new document content, while keeping the document ID unchanged.  
Note: The embedding model used is the default model and cannot be defined within the API.  
Note: Only return the upload results, do not return the final embedding results. You can obtain the final results through the "Query Document Status" API.

## **Request Method**

`PUT`

## **Request URL**

`https://altatech.ai/v1/bot/doc/text/update`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl --location --request PUT 'https://altatech.ai/v1/bot/doc/text/update' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data '{
    "chunk_token": 600,
    "splitter": "\n",
    "files": [
        {
            "doc_id": "675158a5af12af632a4f63f6",
            "file_url": "https://altatech.ai/doc/article_1.pdf",
            "source_url": "https://altatech.ai/doc/article_1.pdf",
            "file_name": "article_1.pdf"
        }
    ]
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use `Authorization: Bearer {token}` for authentication. Get the key from the API Keys page as token. |
| Content-Type | application/json | Data type, set to `application/json`. |

### **Request Body**

| Field | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| files | Array<Object> | Yes | List of documents to be updated. Supports updating up to 200 documents simultaneously. |
| doc_id | String | Yes | The ID of the document to be updated. |
| file_url | String | No | The URL of the document to be updated. Supported formats: pdf/txt/md/doc/docx. Maximum size for PDF documents is 30MB, and for other formats is 10MB. Note: Either URL or base64 must be provided. If both are provided, base64 takes precedence. |
| file_base64 | String | No | The base64 of the document to be updated. Supported formats: pdf/txt/md/doc/docx. Maximum size for PDF documents is 30MB, and for other formats is 10MB. Note: Either URL or base64 must be provided. If both are provided, base64 takes precedence. |
| source_url | String | No | The source URL of the document to be updated. Must comply with URL format specifications. If empty, the system will not update this value. To set this value to empty, please enter `NULL`. |
| chunk_token | Integer | No | The maximum number of tokens for a single knowledge chunk during chunking. Default value is 600. Range: 1-1000. Note: Either maximum token count or splitter must be provided. If both are provided, splitter takes precedence. |
| splitter | String | No | The delimiter used during chunking. Default is empty. You can use "\n" as a line break delimiter. Note: Either maximum token count or splitter must be provided. If both are provided, splitter takes precedence. |

## **Response**

### **Response Example**

```json
{
    "doc": [
        {
            "doc_id": "xxxxxx",
            "doc_name": "test_1.txt"
        },
        {
            "doc_id": "xxxxxx",
            "doc_name": "test_2.pdf"
        }
    ],
    "failed": [
        "xxxxxx",
        "xxxxxx"
    ]
}
```

### **Success Response**

| Field | Type | Description |
| ----- | :---: | :---: |
| doc | Array<Object> | List of documents to be updated. |
| doc_id | String | ID of the document to be updated. |
| doc_name | String | Name of the document to be updated. |
| failed | Array<Object> | List of failed document IDs to be updated. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Int | Error code. |
| message | String | Error details. |
