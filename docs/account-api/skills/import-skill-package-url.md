_Last updated at: 2026-10-13_

# **Import Organization Skill via URL**

Supports downloading a skill installation package from a public URL and importing it as an organization Skill. You can use this endpoint to download a `.zip` or `.skill` skill installation package from a public URL and import it as an organization Skill.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/org/skill/import/url`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication, and requires the calling account to have organization Skill creation permission.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/org/skill/import/url' \
-H 'Authorization: Basic ${BASIC_TOKEN}' \
-H 'Content-Type: application/json' \
-d '{
  "org_id": "p-xxxx",
  "package_url": "https://trusted.example.com/refund-policy.skill",
  "file_name": "refund-policy.skill",
  "category_id": "cat-xxxx"
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
| package\_url | String | Yes | Public URL of the skill installation package. Must be `http/https` and match the server-side whitelist `openapi.skill-package.allowed-hosts`. |
| file\_name | String | No | File name; inferred from the URL when not provided. |
| category\_id | String | No | Skill category ID. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "skill_id": "skill-xxxx",
    "name": "refund-policy",
    "owner_type": "ORGANIZATION"
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| skill\_id | String | The Skill ID after import. |
| name | String | Skill name. |
| owner\_type | String | Skill ownership type. |

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
