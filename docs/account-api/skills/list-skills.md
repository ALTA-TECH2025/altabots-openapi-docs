_Last updated at: 2026-10-13_

# **Query Skill List**

Supports querying the Skill list under a specified organization. You can use this endpoint to query the Skill list under a specified organization.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/org/skill/list`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/org/skill/list?org_id=p-xxxx&keyword=refund&owner_type=ORGANIZATION&enable=true' \
-H 'Authorization: Basic ${BASIC_TOKEN}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |
| Locale | String | Optional. Language of the response text, defaults to `en_US`. |

### **Request Parameters (Query Parameters)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| org\_id | String | Yes | Organization ID. |
| keyword | String | No | Keyword. |
| category\_id | String | No | Skill category ID. |
| owner\_type | String | No | Skill ownership type, e.g. `ORGANIZATION`. |
| owner\_agent\_id | String | No | The Agent ID that owns the private Skill. |
| enable | Boolean | No | Whether to return only enabled or disabled Skills. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": [
    {
      "id": "skill-xxxx",
      "name": "refund-policy",
      "display_name": "Refund Policy",
      "owner_type": "ORGANIZATION",
      "enable": true
    }
  ]
}
```

### **Success Response**

The response items reuse the console's Skill list fields, including Skill ID, name, description, owner, category, version, enable status, and other information.

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
