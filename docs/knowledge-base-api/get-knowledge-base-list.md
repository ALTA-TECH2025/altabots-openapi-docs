_Last updated at: 2025-10-20_

# **Get Knowledge Base List**

Retrieve the list of knowledge bases within the Agent.

## **Request Method**

`GET`

## **Request URL**

`https://altatech.ai/v1/bot/knowledge/base/page`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl --location 'https://altatech.ai/v1/bot/knowledge/base/page' \
--header 'Authorization: Bearer YOUR_API_KEY' \
--header 'Content-Type: application/json'
```

### **Request Header**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use `Authorization: Bearer {token}` for authentication. Get the key from the API Keys page as token. |
| Content-Type | application/json | Data type, set to `application/json`. |

### **Request Body**

None.

## **Response**

### **Response Example**

```json
{
    "knowledge_base": [
        {
            "id": "xxxxxx",
            "name": "My Knowledge Base",
            "desc": "This is my knowledge base.",
            "doc": 10,
            "chunk": 1000,
            "token": 1000000,
            "owner_id": "xxxxxx",
            "owner_email": "johnlee@AltaBots.ai"
        },
        {
            "id": "xxxxxx",
            "name": "My Knowledge Base 2",
            "desc": "This is my knowledge base 2.",
            "doc": 10,
            "chunk": 1000,
            "token": 1000000,
            "owner_id": "xxxxxx",
            "owner_email": "jasonwong@AltaBots.ai"
        }
    ]
}
```

### **Success Response**

| Field | Type | Description |
| ----- | ----- | ----- |
| knowledge_base | Array<Object> | List of knowledge bases. |
| id | String | ID of the knowledge base. |
| name | String | Name of the knowledge base. |
| desc | String | Description of the knowledge base. |
| doc | Integer | Number of documents in the knowledge base. |
| chunk | Integer | Number of knowledge chunks in the knowledge base. |
| token | Number | Number of tokens in the knowledge base. |
| owner_id | String | Owner ID of the knowledge base. |
| owner_email | String | Owner's email of the knowledge base. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Int | Error code. |
| message | String | Error details. |

```