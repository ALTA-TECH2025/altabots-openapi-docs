_Last updated at: 2026-10-13_

# **Delete Tool**

Supports deleting a Tool under a specified organization. You can use this endpoint to delete a Tool under a specified organization. A Tool already mounted by an Agent follows the console's deletion protection.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/org/tool/delete`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication, and requires the calling account to have organization Tool deletion permission.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/org/tool/delete' \
-H 'Authorization: Basic ${BASIC_TOKEN}' \
-H 'Content-Type: application/json' \
-d '{
  "org_id": "p-xxxx",
  "id": "tool-xxxx"
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |
| Content-Type | application/json | Request body format. |

### **Request Parameters (Body Parameters)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| org\_id | String | Yes | Organization ID. |
| id | String | Yes | Tool ID. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "affect_count": 1
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| affect\_count | Integer | Number of affected records. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |

### **Status Codes**

| Status Code | Description |
| :---- | :---- |
| 200 | Success |
| 400 | Parameter error |
| 401 | Unauthorized |
| 403 | Insufficient permissions |
| 429 | Too many requests |
| 500 | Server error |
