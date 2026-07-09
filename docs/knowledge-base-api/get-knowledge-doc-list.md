_Last updated at: 2025-10-20_

# **Get Doc List**

Get a list of knowledge documents in the knowledge base within the Agent.

## **Request Method**

`GET`

## **Request URL**

`https://altatech.ai/v1/bot/doc/query/page`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl --location 'https://altatech.ai/v1/bot/doc/query/page?page=1&page_size=10&knowledge_base_id=67457fea6f658672d6482542' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json'
```

### **Request Header**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use `Authorization: Bearer {token}` for authentication. Get the key from the API Keys page as token. |
| Content-Type | application/json | Data type, set to `application/json`. |

### **Request Body**

| Field | Type | Required | Description |
| ----- | ----- | ----- | ----- |
| knowledge_base_id | String | Yes | The ID of the knowledge base. |
| page | Integer | Yes | Page number, starting from 1. |
| page_size | Integer | Yes | Number of documents per page. Fill in the range 10-100. |

## **Response**

### **Response Example**

```json
{
    "list": [
        {
            "id": "xxxxxx",
            "name": "My Doc",
            "format": "pdf",
            "source_url": "https://altatech.ai/article_1.pdf",
            "status": "ACTIVE",
            "chunk": 100,
            "token": 1000000,
            "char_count": 10000000,
            "create_time": 1699843200,
            "update_time": 1699843200,
            "creator_id": "xxxxxx",
            "creator_email": "johnlee@AltaBots.ai"
        },
        {
            "id": "xxxxxx",
            "name": "My Doc 2",
            "format": "txt",
            "source_url": "https://altatech.ai/article_2.html",
            "status": "ACTIVE",
            "chunk": 100,
            "token": 1000000,
            "char_count": 10000000,
            "create_time": 1699843200,
            "update_time": 1699843200,
            "creator_id": "xxxxxx",
            "creator_email": "johnlee@AltaBots.ai"
        }
    ],
    "total": 100
}
```

### **Success Response**

| Field Name | Type | Description |
| ----- | ----- | ----- |
| list | Array<Object> | Document list. |
| id | String | Document ID. |
| name | String | Document name. |
| format | String | Document format. |
| source_url | String | Document source URL. |
| status | String | Document status. |
| chunk | Integer | Number of knowledge chunks in the document. |
| token | Integer | Number of tokens in the document. |
| char_count | Integer | Number of characters in the document. |
| create_time | Long | Document creation time, timestamp. |
| update_time | Long | Document update time, timestamp. |
| creator_id | String | Creator ID of the document. |
| creator_email | String | Creator's email of the document. |
| total | Integer | Total number of documents found. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Int | Error code. |
| message | String | Error details. |
