_Last updated at: 2026-10-20_

# **Create a Share Link**

Create a share link for the Agent using the Agent's API Key. End users can open the link to directly interact with the Agent. You can set the link expiration, maximum number of users, maximum number of messages per user, access password, and whether to enable feedback suggestions. The effect is exactly the same as manually creating a share link on the "Share" page.

- The created share link is synchronized to the Agent's share link list. You can check the number of users and credits consumed in the console, and continue to edit or delete it. Members of the organization with permission to edit/delete share links can operate links created via API.
- Credits consumed by the share link are counted toward the organization to which the Agent belongs.
- If the organization has a custom domain bound, the returned share link address uses the custom domain.
- Only Agents are supported; calling with a Workflow API Key returns an incorrect Bot type error.
- If the current site does not have the "Share" integration channel enabled, the call returns that the operation is not supported.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/agent/share/create`

## **Request Authentication**

See Overview for authentication details. Use the target Agent's API Key as the token.

## **Request**

### **Request Example**

```
curl -X POST https://altatech.ai/v1/agent/share/create \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "Website trial link",
        "valid_days": 7,
        "user_limit": 10,
        "user_question_limit": 9999,
        "password": "Vc3h",
        "feedback_enabled": true
}'
```

All parameters are optional. When the request body is `{}`, a **permanently valid, password-free** share link is created for up to 10 users, with a maximum of 9999 messages per user, and feedback suggestions disabled. If access restrictions are needed, explicitly pass `valid_days` and `password`.

All field names use snake\_case. If the request body contains unrecognized fields (e.g., camelCase such as `validDays`), the API returns `40000` and lists these fields in the error message, without creating the link.

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Get the key from the API Keys page as token. |
| Content-Type | application/json | Data type, set to application/json. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| name | string | No | Name of the share link, maximum 20 characters. When editing the link in the console the name is required, so it is recommended to provide it when creating. |
| valid\_days | int | No | Validity period of the share link in days, range 1 ~ 3650, starting from creation time. Not passing it means no limit. |
| user\_limit | int | No | Maximum number of users, range 1 ~ 99999, default is 10. |
| user\_question\_limit | int | No | Maximum number of messages per user, range 1 ~ 99999, default is 9999. |
| password | string | No | Access password, must be 4 letters or numbers. Not passing it or passing an empty string means no password is required. |
| feedback\_enabled | boolean | No | Whether to enable feedback suggestions, default `false`. |

## **Response**

### **Response Example**

```
{
    "code": 0,
    "message": "OK",
    "data": {
        "share_id": "66f8c2a1e4b0a93c5d7f1a20",
        "link": "https://altatech.ai/s/csAbC123",
        "expire_time": 1760112000000
    }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| share\_id | string | Share link ID. |
| link | string | The share link address, which can be sent directly to end users for access. |
| expire\_time | long | Share link expiration time, timestamp in milliseconds. `null` if valid indefinitely. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Parameter error (including field value out of range, field type error, or unrecognized fields) |
| 40001 | Requests are too frequent, please try again later (up to 30 calls per minute per Agent) |
| 40008 | Requests are too frequent, please try again later (exceeds API RPM limit of the plan) |
| 40010 | Operation not supported (share link integration not enabled on current site) |
| 40101 | Header Authorization is empty |
| 40127 | Developer authentication failed |
| 40378 | Agent has been deleted |
| 20055 | API functionality is forbidden, please ensure API switch is turned on |
| 403171 | Bot type is incorrect |
