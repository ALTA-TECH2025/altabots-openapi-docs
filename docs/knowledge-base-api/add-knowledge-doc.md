_Last updated at: 2025-10-20_

# **Add Text Docs (file)**

Batch upload text files, and sequentially perform chunking/slicing, embedding/vectorization, and storage.  
Note: The embedding model used is the default model and cannot be defined within the API.  
Note: Only return the upload results, do not return the final embedding results. You can obtain the final results through the "Query Document Status" API.

## **Request Method**

`POST`

## **Request URL**

`https://altatech.ai/v1/bot/doc/text/add`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl --location 'https://altatech.ai/v1/bot/doc/text/add' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data '{
    "knowledge_base_id": "67457fea6f658672d6482542",
    "chunk_token": 700,
    "splitter": "\n",
    "files": [
        {
            "file_url": "https://altatech.ai/docs/article_1.pdf",
            "file_base64": "SGVsbG8sIEJhc2U2NCBFbmNvZGluZyE=",
            "source_url": "https://altatech.ai/docs/article_1.pdf",
            "file_name": "article_1.pdf"
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
| ----- | ----- | ----- | ----- |
| knowledge_base_id | String | No | The target knowledge base to which the document is added. If not filled, it defaults to the "Default" knowledge base. |
| files | Array<Object> | Yes | List of documents to be added. Supports adding up to 20 documents simultaneously. |
| file_url | String | No | The URL of the document to be added. Supported formats: pdf/txt/md/doc/docx. Maximum size for PDF is 30MB, and for other formats, it is 10MB. Note: Either URL or base64 must be provided. If both are provided, base64 takes precedence. |
| file_base64 | String | No | The base64 of the document to be added. Supported formats: pdf/txt/md/doc/docx. Maximum size for PDF is 30MB, and for other formats, it is 10MB. Note: Either URL or base64 must be provided. If both are provided, base64 takes precedence. |
| file_name | String | Yes | The name of the document to be added. 1-200 characters. |
| source_url | String | No | The source URL of the document to be added. Must comply with URL format specifications. |
| chunk_token | Integer | No | The maximum number of tokens for a single knowledge chunk during chunking. Default value is 600. Range is 1-1000. Note: Either maximum token count or delimiter must be provided. If both are provided, delimiter takes precedence. |
| splitter | String | No | The delimiter used during chunking. Default is empty. You can use "\n" as a line break delimiter. Note: Either maximum token count or delimiter must be provided. If both are provided, delimiter takes precedence. |

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
        "file_1",
        "file_2"
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---: | :---: | :---: |
| doc | Array<Object> | List of added documents. |
| doc_id | String | ID of the added document. |
| doc_name | String | Name of the added document. |
| failed | Array<Object> | List of failed added document names. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Int | Error code. |
| message | String | Error details. |
