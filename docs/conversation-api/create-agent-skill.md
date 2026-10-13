_Last updated at: 2026-10-13_

# **Create Agent Private Skill**

You can use this endpoint to create a private Skill for the LoopAgent that the current Agent API Key belongs to.

- Only LoopAgent is supported; regular Agent, Flow Agent, and Workflow are not supported.
- Only creates a private Skill for the Agent that the current Agent API Key belongs to.
- Only `.skill` and `.zip` are accepted; the archive is at most 20 MiB, with a maximum of 200 valid files, a maximum of 5 MiB per file after decompression, and a maximum of 64 MiB for the whole archive after decompression.
- The archive must contain `SKILL.md` in the root directory or the single top-level directory, and its frontmatter must contain `name`.
- Creation does not automatically mount the Skill to the Agent, nor does it automatically save or publish an Agent version.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/agent/skill/create`

## **Request Authentication**

Use the Agent Key of the target LoopAgent, and the Key must have version management permission enabled. Refer to API Overview for authentication instructions.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/agent/skill/create' \
-H 'Authorization: Bearer ${API Key}' \
-F 'file=@/path/to/refund-policy.skill'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${API Key} | Authenticate with the API Key of the target LoopAgent, and the Key must have version management permission enabled. |
| Content-Type | multipart/form-data | Upload the skill package file as a form. |

### **Request Parameters (Form Data)**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| file | File | Yes | `.skill` or `.zip` skill package. |
| category\_id | String | No | Skill category ID; created as an empty category when not provided. |

## **Response**

### **Response Example**

```
{
    "code": 0,
    "message": "OK",
    "data": {
        "skill_id": "skill-xxxx",
        "name": "refund_policy",
        "version": "1.0.0"
    }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| skill\_id | String | The newly created Skill ID. |
| name | String | Skill name. |
| version | String | Skill version number. |

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
