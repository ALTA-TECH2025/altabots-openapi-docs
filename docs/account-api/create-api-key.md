_Last updated at: 2026-10-13_

# **Create API Key**

Allows the organization owner to create an API Key for an Agent or Workflow in the organization. You can use this endpoint to issue a new API Key for a specified Agent or Workflow and set whether the key has version management permission. Once created, the returned API Key can be used to call the resource-level endpoints of that Agent or Workflow.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/org/api-key/create`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication, and the calling account must be the owner of the organization.

## **Request**

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/org/api-key/create' \
-H 'Authorization: Basic ${BASIC_TOKEN}' \
-H 'Content-Type: application/json' \
-d '{
  "org_id": "p-xxxx",
  "agent_id": "68d0f1a2b3c4d5e6f7a8b9c0",
  "is_publish": true
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |
| Content-Type | application/json | Request body format. |

### **Request Body**

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| org\_id | String | Yes | Organization ID, which can be obtained from the [Query Organization List](list-organizations.md) endpoint. |
| agent\_id | String | No | ID of the Agent to create the API Key for. Mutually exclusive with `workflow_id`; only one of them can be provided. |
| workflow\_id | String | No | ID of the Workflow to create the API Key for. Mutually exclusive with `agent_id`; only one of them can be provided. |
| is\_publish | Boolean | Yes | Whether to enable version management permission (import, version list, publish, rollback) for this API Key. It only sets the permission and does not trigger a publish. Must be a JSON boolean `true` or `false`; values such as `"true"` or `1` are not supported. |

Notes:

- Exactly one non-empty value must be provided for `agent_id` or `workflow_id`. Providing both, neither, or a blank string returns a parameter error.
- The ID must match the resource type: passing a Workflow ID via `agent_id`, or an Agent ID via `workflow_id`, returns a type mismatch error.
- Each Agent or Workflow can have at most 10 API Keys. Once the limit is reached, delete an existing key before creating a new one.
- The name of the new API Key is generated automatically in the format `api-` followed by 12 random characters. You can view or edit it on the API Keys page in the console.
- This endpoint is rate-limited per account: at most 10 calls per minute per account.

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "api_key": "app-xxxxxxxxxxxxxxxxxxxxxxxx"
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| api\_key | String | The newly created API Key, used to call the resource-level endpoints of the corresponding Agent or Workflow. |

Keep the returned API Key secure. The response includes the header `Cache-Control: no-store`; do not retain the plaintext key in logs or caches.

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |

### **Error Codes**

| Code | Description |
| :---- | :---- |
| 40000 | Parameter error, e.g. a required parameter is missing, `is_publish` is not a boolean, `agent_id` and `workflow_id` do not satisfy the exactly-one rule, or the resource has reached its API Key limit. |
| 40101 | The `Authorization` request header is empty. |
| 40104 | The current account is not the owner of the organization. |
| 40324 | Invalid DevKey or DevSecret. |
| 40348 | The Agent or Workflow does not exist or does not belong to the organization. |
| 403204 | The provided ID does not match the resource type (Agent / Workflow). |

### **Status Codes**

| Status Code | Description |
| :---- | :---- |
| 200 | Success |
| 400 | Parameter error |
| 401 | Unauthorized |
| 403 | Insufficient permissions |
| 429 | Too many requests |
| 500 | Server error |
