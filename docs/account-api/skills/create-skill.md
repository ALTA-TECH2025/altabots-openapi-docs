_Last updated at: 2026-10-13_

# **API Create Organization Skill**

Supports creating an organization-level Skill under a specified organization. You can use this endpoint to create an organization-level Skill under a specified organization.

- Only `.skill` and `.zip` are accepted; the archive is at most 20 MiB.
- The archive must contain `SKILL.md` in the root directory or the single top-level directory, and its frontmatter must contain `name`.
- After a successful creation, use `POST /v1/org/skill/update` and pass `skill_id` in the Form Data to update the Skill. See [Update Organization Skill](update-skill-package.md).

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/org/skill/create`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication, and requires the calling account to have organization Skill creation permission.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/org/skill/create' \
-H 'Authorization: Basic ${BASIC_TOKEN}' \
-F 'org_id=org-xxxx' \
-F 'file=@/path/to/refund-policy.skill'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |
| Content-Type | multipart/form-data | File upload form. |

### **Request Parameters (Form Data)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| org\_id | String | Yes | The organization ID under which to create the shared Skill. |
| file | File | Yes | `.skill` or `.zip` skill package. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "skill_id": "skill-xxxx",
    "name": "refund_policy",
    "owner_type": "ORGANIZATION"
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| skill\_id | String | The newly created Skill ID. |
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
