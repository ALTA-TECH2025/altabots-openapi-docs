_Last updated at: 2026-10-13_

# **Import Organization Skill from File**

Supports uploading a skill installation package and importing it as an organization Skill. You can use this endpoint to upload a `.zip` or `.skill` skill installation package and import it as an organization Skill.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/org/skill/import`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication, and requires the calling account to have organization Skill creation permission.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/org/skill/import' \
-H 'Authorization: Basic ${BASIC_TOKEN}' \
-F 'file=@/path/to/refund-policy.skill' \
-F 'org_id=p-xxxx' \
-F 'category_id=cat-xxxx'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |
| Content-Type | multipart/form-data | File upload form. |

### **Request Parameters (Form Data)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| file | File | Yes | `.zip` or `.skill` skill installation package. |
| org\_id | String | Yes | Organization ID. |
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
