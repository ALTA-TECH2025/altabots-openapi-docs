_Last updated at: 2026-10-13_

# **Update Agent Private Skill**

You can use this endpoint to update a private Skill for the Agent that the current LoopAgent API Key belongs to. The Skill ID is passed via the multipart form field `skill_id` and does not appear in the URL path.

- Only LoopAgent is supported, and you can only update private Skills owned by the Agent that the current Agent API Key belongs to.
- The target lookup is scoped by `skill_id + projectId + botId`; Skills that do not belong to the current Agent are rejected.
- The file format is the same as the create endpoint: only `.skill` and `.zip` are accepted, and the archive is at most 20 MiB.
- The update only saves a Skill content version, but does not automatically mount the Skill, save an Agent draft version, or publish a production Agent version.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/agent/skill/update`

## **Request Authentication**

Use the Agent Key of the target LoopAgent, and the Key must have version management permission enabled. Refer to API Overview for authentication instructions.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/agent/skill/update' \
-H 'Authorization: Bearer ${API Key}' \
-F 'skill_id=skill-xxxx' \
-F 'file=@/path/to/refund-policy-v2.skill'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${API Key} | Authenticate with the API Key of the target LoopAgent, and the Key must have version management permission enabled. |
| Content-Type | multipart/form-data | Upload the skill package file as a form. |

### **Request Parameters (Form Data)**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| skill\_id | String | Yes | The Agent private Skill ID to update. |
| file | File | Yes | `.skill` or `.zip` skill package. |
| category\_id | String | No | The category ID after the update; can be omitted, in which case the original category is kept. |

The server compares the target Skill's current file and metadata; when they are exactly the same, it returns the current version directly without writing to storage, and the caller does not need to pass an idempotency request header.

## **Response**

### **Response Example**

```
{
    "code": 0,
    "message": "OK",
    "data": {
        "skill_id": "skill-xxxx",
        "name": "refund_policy",
        "version": "1.0.2"
    }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| skill\_id | String | The updated Skill ID, which stays unchanged. |
| name | String | Skill name. |
| version | String | The Skill version number after the update. |

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
