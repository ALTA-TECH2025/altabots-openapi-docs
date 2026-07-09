_Last updated at: 2026-07-09_

# **Vector Similarity Matching**

Retrieve and recall knowledge slices from the Agent/Workflow knowledge base based on the provided query content or keywords. Developers can specify the retrieval scope using `group_ids` or `data_ids`, set the `top_k` parameter, and personalize retrieval through knowledge relevance scoring and reranking for customized Retrieval-Augmented Generation (RAG) capabilities.

## **Request Method**

`POST`

## **Request URL**

`https://altatech.ai/v1/vector/match`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl -X POST 'https://altatech.ai/v1/vector/match' \
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json' \
-d '{
    "embedding_rate": 0.9,
    "prompt": "What APIs does AltaBots offer?",
    "group_ids": ["1234567890", "1230987654"],
    "data_ids": ["1234567890", "1230987654"],
    "top_k": 10,
    "rerank_version": "Jina-reranker-v2-base-multilingual",
    "doc_correlation": 0.70
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${API Key} | Use Authorization: Bearer ${API Key} for authentication. Get API key from API Key page. |
| Content-Type | application/json | Data type; the value should be application/json. |

### **Request Parameters**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| embedding_rate | float | No | Specifies the weight ratio between keyword-based and semantic-based retrieval. Value range: [0,1], default is 1. For example: 0 = keyword-only; 1 = semantic-only; 0.4 = 40% keyword, 60% semantic. |
| prompt | string | Yes | Keywords or query content used for vector similarity matching with documents in the Agent/Workflow. |
| group_ids | array | No | Knowledge base IDs for vector retrieval within specified knowledge bases. If one or more knowledge base IDs are provided, retrieval is performed within their union. If null or not provided, defaults to all knowledge bases. If `[]`, no knowledge base is retrieved. |
| data_ids | array | No | Document IDs for vector retrieval within specified knowledge documents. If one or more document IDs are provided, retrieval is performed within their union. If null or not provided, defaults to all knowledge documents. If `[]`, no knowledge document is retrieved. |
| top_k | int | Yes | After performing vector similarity matching between keywords and document IDs, returns the top K results. Valid range: [1,50]. |
| rerank_version | string | No | Name of the knowledge reranking model for more precise search. Options include: BGE-Rerank, Jina-reranker-v2-base-multilingual, Jina-colbert-v2, BCE-Rerank. |
| doc_correlation | float | No | Knowledge relevance score, representing the similarity between the user question and a knowledge chunk. Higher scores indicate greater relevance, but excessively high values may result in no available knowledge chunks. Range: [0.1,0.95]. |

When both `group_ids` and `data_ids` are provided, retrieval is performed within the union of their respective knowledge scopes. If both are null or not provided, all knowledge bases are searched by default. If both are empty arrays (`[]`), no knowledge is retrieved.

## **Response**

### **Response Example**

```json
{
    "total": 2,
    "list": [
        {
            "content": "Test data",
            "data_id": "aS1CNvPK4XCckDKQNj7azC9a",
            "document_name": "demo.md",
            "score": 0.75
        },
        {
            "content": "Test data",
            "data_id": "aS1CNvPK4XCckDKQNj7azC9a",
            "document_name": "demo.md",
            "score": 0.75
        }
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| total | int | Total number of returned chunks. |
| list | JSON Array | List of chunks. |
| content | string | Chunk content. |
| data_id | string | Source document. |
| document_name | string | Source document name. |
| score | float | Similarity score. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Parameter error |
| 40127 | Developer authentication failed |
| 20059 | Agent/Workflow deleted |
