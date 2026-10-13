_Last updated at: 2026-10-13_

# **Add Text-type Documents**

Batch upload **text-type** documents, which will be processed sequentially through chunking/slicing, embedding/vectorization, and storage to obtain new document IDs.

Note: You can specify the embedding model with `embedding_model_version_id`; if omitted, the system default embedding model is used.  
Note: Only upload results are returned, not the final embedding results. You can obtain the final results through the "Query Document Status" API.

## **Request Method**

`POST`

## **Request URL**

`https://altatech.ai/v1/bot/doc/text/add`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl -X POST 'https://altatech.ai/v1/bot/doc/text/add' \
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json' \
-d '{
    "knowledge_base_id": "67457fea6f658672d6482542",
    "embedding_model_version_id": "6620f06262390a0be1411c5d",
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
| Authorization | Bearer ${API Key} | Use `Authorization: Bearer ${API Key}` for authentication. Get the key from the API Keys page. |
| Content-Type | application/json | Data type, set to `application/json`. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| knowledge\_base\_id | String | No | The target knowledge base to which the document is added. If not filled, it defaults to the "Default" knowledge base. |
| files | Array&lt;Object&gt; | Yes | List of documents to be added. Supports adding up to 20 documents simultaneously. |
| files[].file\_url | String | No | The URL of the document to be added. Supported formats: pdf/txt/md/doc/docx. Maximum size for PDF is 30MB, and for other formats, it is 10MB. Note: Either URL or base64 must be provided. If both are provided, base64 takes precedence. |
| files[].file\_base64 | String | No | The base64 of the document to be added. Supported formats: pdf/txt/md/doc/docx. Maximum size for PDF is 30MB, and for other formats, it is 10MB. Note: Either URL or base64 must be provided. If both are provided, base64 takes precedence. |
| files[].file\_name | String | Yes | The name of the document to be added. 1-200 characters. |
| files[].source\_url | String | No | The source URL of the document to be added. Must comply with URL format specifications. |
| embedding\_model\_version\_id | String | No | ID of the embedding model version used to vectorize this batch of documents. If omitted, the system default embedding model is used. Obtain a valid value from the `modelId` field returned by Get Model List under the `EMBEDDING` group. |
| chunk\_token | Integer | No | Maximum number of tokens per knowledge chunk during segmentation. Default value is 600. Valid range is 1-1000. Note: Either `chunk_token` or `splitter` must be specified. When both are specified, the splitter takes precedence. If neither is provided, the request still succeeds, but the document fails during vectorization (status `FAIL_STORE`), so always provide at least one. |
| splitter | String | No | Delimiter used for text chunking. Default is empty. Can use a custom string (e.g. `"\n"`) as delimiter. Note: Either `chunk_token` or `splitter` must be specified. When both are specified, the splitter takes precedence. If neither is provided, the request still succeeds, but the document fails during vectorization (status `FAIL_STORE`), so always provide at least one. |

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
| :---- | :---- | :---- |
| doc | Array&lt;Object&gt; | List of added documents. |
| doc[].doc\_id | String | ID of the added document. |
| doc[].doc\_name | String | Name of the added document. |
| failed | Array&lt;Object&gt; | List of failed added document names. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Int | Error code. |
| message | String | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Parameter error |
| 40000 | The embedding\_model\_version\_id does not exist: the given model version ID is not found in the platform model catalog |
| 40000 | The embedding\_model\_version\_id is not an embedding model: the given ID refers to a non-embedding model (for example, a chat model `modelId`) |
| 40000 | The embedding\_model\_version\_id is not an available embedding model: the provider of this embedding model does not yet support being specified via the API |
| 40127 | Developer authentication failed |
| 20059 | Agent deleted |

> Note: If `embedding_model_version_id` fails validation, no documents in the batch are created and none appear in the `failed` list; the error response above is returned directly.
