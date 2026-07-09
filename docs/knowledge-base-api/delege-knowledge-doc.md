_Last updated at: 2025-10-20_

# **Delete Docs**

Delete docs from knowledge base.

## **Request Method**

`DELETE`

## **Request URL**

`https://altatech.ai/v1/bot/doc/batch/delete`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```bash
curl --location --request DELETE 'https://altatech.ai/v1/bot/doc/batch/delete?doc=67501ddb8cf3c334cd0e8e70,12345ddb8cf3c334cd0e0987' \
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
| doc | Array<String> | Yes | Document IDs to be deleted. |

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
