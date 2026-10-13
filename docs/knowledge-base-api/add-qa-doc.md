_Last updated at: 2026-10-13_

# **Add Q&A Knowledge Document**

This interface allows you to add a Q&A knowledge document to an Agent's knowledge base. It supports three methods: directly passing Q&A text, uploading a Q&A format file (CSV), or uploading a document to be automatically converted into Q&A pairs.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/bot/doc/qa/add`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

**Via Q&A Text:**

```bash
curl -X POST https://altatech.ai/v1/bot/doc/qa/add \
-H 'Authorization: Bearer your_apikey' \
-H 'Content-Type: application/json' \
-d '{
    "purpose": "QA_TEXT",
    "name": "Frequently Asked Questions",
    "knowledge_base_id": "673af861ed69656ac0895b07",
    "embedding_model_version_id": "6620f06262390a0be1411c5d",
    "qaList": [
        {
            "question": "How to register an account?",
            "answer": "Click the register button in the top right corner of the homepage, fill in your email and password to complete registration."
        },
        {
            "question": "How to reset the password?",
            "answer": "Click forgot password on the login page and follow the prompts to reset it."
        }
    ]
}'
```

**Via Q&A File:**

```bash
curl -X POST https://altatech.ai/v1/bot/doc/qa/add \
-H 'Authorization: Bearer your_apikey' \
-H 'Content-Type: application/json' \
-d '{
    "purpose": "QA_FILE",
    "knowledge_base_id": "673af861ed69656ac0895b07",
    "embedding_model_version_id": "6620f06262390a0be1411c5d",
    "files": [
        {
            "file_url": "https://example.com/qa.csv",
            "file_name": "qa_data.csv"
        }
    ]
}'
```

**Via Document-to-Q&A Conversion:**

```bash
curl -X POST https://altatech.ai/v1/bot/doc/qa/add \
-H 'Authorization: Bearer your_apikey' \
-H 'Content-Type: application/json' \
-d '{
    "purpose": "FILE_2_QA",
    "knowledge_base_id": "673af861ed69656ac0895b07",
    "embedding_model_version_id": "6620f06262390a0be1411c5d",
    "files": [
        {
            "source_url": "https://example.com/product_manual.pdf",
            "file_name": "Product Manual.pdf"
        }
    ]
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${token} | Use Authorization: Bearer ${token} for authentication. Obtain your key from the API Key page to use as the token. |
| Content-Type | application/json | Data type, must be application/json. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| purpose | string | Yes | Data type, options: `QA_TEXT` (Q&A text), `QA_FILE` (Q&A format file), `FILE_2_QA` (document to Q&A). |
| knowledge\_base\_id | string | No | Knowledge base ID. If not provided, the default knowledge base will be used. |
| name | string | Conditional | Document name, required when `purpose` is `QA_TEXT`. |
| qaList | list | Conditional | A list of Q&A pairs, required when `purpose` is `QA_TEXT`. |
| qaList[].question | string | Yes | The content of the question. |
| qaList[].answer | string | Yes | The content of the answer. |
| files | list | Conditional | A list of files, required when `purpose` is `QA_FILE` or `FILE_2_QA`, up to 20 files. |
| files[].source\_url | string | Yes | The source URL of the file. |
| files[].file\_name | string | Yes | The name of the file. |
| files[].doc\_id | string | No | Document ID. |
| files[].file\_url | string | No | The URL of the file. |
| files[].file\_base64 | string | No | The base64 encoded content of the file. |
| header\_row | int | No | The header row number. |
| chunk\_token | int | No | The number of tokens per chunk, default is 600. |
| splitter | string | No | The separator. |
| embedding\_model\_version\_id | string | No | ID of the embedding model version used to vectorize this batch of documents. If omitted, the system default embedding model is used. Obtain a valid value from the `modelId` field returned by Get Model List under the `EMBEDDING` group. |

- When `purpose` is `QA_TEXT`, `name` and `qaList` must be provided.
- When `purpose` is `QA_FILE` or `FILE_2_QA`, `files` must be provided, with a maximum of 20 files.

## **Response**

### **Response Example**

```json
{
    "doc": [
        {
            "doc_id": "680d1a2b3c4d5e6f7a8b9c0d",
            "doc_name": "Frequently Asked Questions"
        }
    ],
    "failed": []
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| doc | list | A list of successfully added documents. |
| doc[].doc\_id | string | Document ID. |
| doc[].doc\_name | string | Document name. |
| failed | list | A list of file names that failed to be added. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error description message. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Parameter error |
| 40000 | The embedding\_model\_version\_id does not exist: the given model version ID is not found in the platform model catalog |
| 40000 | The embedding\_model\_version\_id is not an embedding model: the given ID refers to a non-embedding model (for example, a chat model `modelId`) |
| 40000 | The embedding\_model\_version\_id is not an available embedding model: the provider of this embedding model does not yet support being specified via the API |
| 50000 | Internal system error |

> Note: If `embedding_model_version_id` fails validation, no documents in the batch are created and none appear in the `failed` list; the error response above is returned directly.
