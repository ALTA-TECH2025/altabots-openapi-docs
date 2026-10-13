_Last updated at: 2026-10-13_

# **Update Organization Skill**

You can use a specified `skill_id` to update the Skill of a specified organization; publishing is completed automatically once the update finishes.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/org/skill/update`

## **Request Authentication**

Uses the organization account's DevKey and DevSecret for HTTP Basic authentication. The calling account must have Skill management permission for the target organization.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/org/skill/update' \
-H 'Authorization: Basic ${BASIC_TOKEN}' \
-F 'org_id=org-xxxx' \
-F 'skill_id=skill-xxxx' \
-F 'file=@/path/to/refund-policy-v2.skill' \
-F 'category_id=category-xxxx'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |
| Content-Type | multipart/form-data | File upload form. |

### **Request Parameters (Form Data)**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| skill\_id | String | Yes | The organization shared Skill ID to update. |
| org\_id | String | Yes | The organization ID that the Skill belongs to; must match the target Skill. |
| file | File | Yes | `.skill` or `.zip` skill package. |
| category\_id | String | No | The category ID after the update; keeps the original category when not provided. |

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
| skill\_id | String | The updated organization shared Skill ID. |
| name | String | The `name` in the `SKILL.md` frontmatter of this skill package. |
| owner\_type | String | Fixed as `ORGANIZATION`. |

### **Usage Boundaries**

- Only updates shared Skills with `owner_type=ORGANIZATION` that are not bound to an Agent.
- Agent private Skills, historical private records with a `bot_id`, and SYSTEM Skills are all rejected.
- Only `.skill` and `.zip` are accepted; the archive is at most 20 MiB and must contain `SKILL.md`, whose frontmatter must contain `name`.
- `POST /v1/org/skill/import` is only used to create an organization Skill and does not carry update semantics.

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
