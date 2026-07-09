_Last updated at: 2026-07-09_

# **Create Knowledge Base**

Use this API to create a new knowledge base for the Agent bound to the API Key.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/bot/knowledge/base/create`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl -X POST 'https://altatech.ai/v1/bot/knowledge/base/create' \
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json' \
-d '{
    "name": "Product Knowledge Base",
    "desc": "A knowledge base for product manuals, FAQs, and business materials",
    "graph_enable": false,
    "access_control_enabled": false
}'
```

### **Request Header**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${API Key} | Use Authorization: Bearer ${API Key} for authentication. Get API key from API Key page. |

### **Request Parameters**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| name | String | Yes | Name of the knowledge base. |
| desc | String | Yes | Description of the knowledge base. |
| graph_enable | Boolean | No | Whether to enable the knowledge graph. |
| kg_ner_extraction_user_prompt | String | No | Triple extraction prompt. If empty, the system default configuration is used. |
| access_control_enabled | Boolean | No | Whether to enable access control, i.e., role- or document-level permission filtering. |

## **Response**

### **Response Example**

```json
{
    "knowledge_base_id": "6a475ee61d276b3d062a1bcb"
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| knowledge_base_id | String | ID of the newly created knowledge base. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |
