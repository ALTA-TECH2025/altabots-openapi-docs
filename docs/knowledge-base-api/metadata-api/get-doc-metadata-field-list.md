_Last updated at: 2026-07-18_

# **Get Metadata Field List**

Query the metadata field definitions under the Agent, returned grouped as: global fields + fields dedicated to each knowledge base. System-predefined fields (such as `document_name`) are not included in the response.

## **Request Method**

`GET`

## **Request URL**

`https://altatech.ai/v1/bot/doc/metadata/field/list`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl --location 'https://altatech.ai/v1/bot/doc/metadata/field/list' \
--header 'Authorization: Bearer YOUR_API_KEY'
```

### **Request Header**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use `Authorization: Bearer {token}` for authentication. Get the key from the API Keys page as token. |

### **Request Body**

None. The Agent is resolved from the API Key.

## **Response**

### **Response Example**

```json
{
    "global_fields": [
        {
            "id": "665f1c8a9b2e4d001a3f0001",
            "name": "category",
            "display_name": "Category",
            "type": "LIST",
            "options": ["Tech", "Product"],
            "description": "Document category",
            "ai_search_filter": true,
            "is_predefined": false
        }
    ],
    "knowledge_bases": [
        {
            "knowledge_base_id": "kb_001",
            "knowledge_base_name": "Product Documentation KB",
            "fields": [
                {
                    "id": "665f1c8a9b2e4d001a3f0009",
                    "name": "product_line",
                    "display_name": "Product Line",
                    "type": "STRING",
                    "options": null,
                    "description": "",
                    "ai_search_filter": false,
                    "is_predefined": false
                }
            ]
        },
        {
            "knowledge_base_id": "kb_002",
            "knowledge_base_name": "After-sales FAQ KB",
            "fields": []
        }
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| global_fields | Array<Object> | Global fields that apply to all documents under the Agent. |
| id | String | Field ID, used when editing or deleting the field. |
| name | String | Internal field identifier, lowercase, unique. |
| display_name | String | Display name of the field, unique. |
| type | String | Field type: STRING / NUMBER / DATETIME / LIST. |
| options | Array<String> | Enum options for LIST type fields; null for other types. |
| description | String | Field description. |
| ai_search_filter | Boolean | Whether the field can be used as an AI Search filter. |
| is_predefined | Boolean | Whether the field is a system-predefined field. |
| knowledge_bases | Array<Object> | Knowledge bases and their dedicated fields. |
| knowledge_base_id | String | Knowledge base ID. |
| knowledge_base_name | String | Knowledge base name. |
| fields | Array<Object> | Dedicated fields of the knowledge base, same structure as global fields. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |
