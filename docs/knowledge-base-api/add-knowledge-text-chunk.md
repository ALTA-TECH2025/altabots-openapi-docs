_Last updated at: 2025-10-20_

# **Add Chunks (Text)**

Add knowledge blocks to text documents. The system will sequentially perform chunking/slicing, embedding/vectorization, and finally add new knowledge blocks to the document.  
Note: The embedding model used is the default model and cannot be defined within the API.

## **Request Method**

`POST`

## **Request URL**

`https://altatech.ai/v1/bot/doc/chunks/add`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl --location 'https://altatech.ai/v1/bot/doc/chunks/add' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data '{
    "doc_id": "675174292b8b977ba6316191",
    "chunks": [
        {
            "content": "This is a chunk.",
            "keywords": ["This","chunk"]
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
| doc_id | String | Yes | The ID of the document to which the knowledge block will be added. |
| chunks | Array<Object> | Yes | The content of the knowledge blocks. |
|     content | String | Yes | The content of the knowledge block, up to 1000 Tokens long. |
|     keywords | Array<String> | No | The keywords for the knowledge block. |

## **Response**

### **Response Example**

```json
{
    "code": 0,
    "message": "OK"
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Int | Response code. |
| message | String | Response details. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Int | Error code. |
| message | String | Error details. |
