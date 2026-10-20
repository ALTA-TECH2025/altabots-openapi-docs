_Last updated at: 2026-10-20_

# **Retrieve Recent Activity of Agents**

Retrieve the number of new conversations and user questions for one or more Agents in the last N minutes, suitable for periodic activity checks. Up to 50 Agents can be queried per call.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/org/agent/stat/recent-activity`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication: `Authorization: Basic ${BASIC_TOKEN}`, where `${BASIC_TOKEN}` is the Base64 encoding of `DevKey:DevSecret`.

The calling account must be a member of the organization specified by `org_id` and have the "View Usage" permission (organization Owners and Admins have it by default), and must be able to view the Agents: the Agent creator, the organization Owner, or a member granted permission for the Agent (or all Agents).

## **Request Frequency**

- Each developer key can call this API up to 60 times per minute.
- Each call also counts toward the per-minute quota of the organization plan's "Statistics API", shared with statistics API calls made with Agent API Keys.
- Query results are cached for 30 seconds. Calling once per minute and combining multiple Agents into a single request is recommended.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/org/agent/stat/recent-activity?org_id=${org_id}&agent_id=${agent_id_1},${agent_id_2}&minutes=5' \
-H 'Authorization: Basic ${BASIC_TOKEN}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |

### **Request Parameters**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| org\_id | String | Yes | Organization ID, which can be obtained from the [Query Organization List](../account-api/list-organizations.md) endpoint. |
| agent\_id | String | Yes | Agent IDs, comma-separated, up to 50; duplicates are counted once. Workflow is not supported. |
| minutes | Integer | No | Number of minutes to count, from 1 to 60, default 5. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "minutes": 5,
    "window_start": 1790664900000,
    "window_end": 1790665200000,
    "agents": [
      {
        "agent_id": "65f0c2a1b4e8d93a1c7e5b21",
        "new_conversation_count": 3,
        "new_message_count": 27
      }
    ]
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| minutes | Integer | Length of the statistics window (minutes). |
| window\_start | Long | Window start (milliseconds timestamp). |
| window\_end | Long | Window end (milliseconds timestamp, exclusive). |
| agents[].agent\_id | String | Agent ID, in the same order as `agent_id` in the request. |
| agents[].new\_conversation\_count | Long | Number of conversations created in the window that have had at least one interaction. |
| agents[].new\_message\_count | Long | Number of user questions sent in the window, excluding AI replies. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |

### **Error Codes**

The HTTP status code is the first three digits of the error code, e.g. 40000 → 400, 40100 → 401, 403132 → 403.

| Code | Description |
| :---- | :---- |
| 40000 | Parameter error, such as missing required parameters or invalid parameter values. |
| 40001 | Too many requests: this developer key has exceeded the per-minute limit for this API. |
| 40008 | Exceeded the per-minute quota of the organization plan's "Statistics API". |
| 40010 | API temporarily unavailable, please try again later. |
| 40100 | No permission: missing the "View Usage" permission, or not allowed to view this Agent (including when the Agent does not belong to this organization). |
| 40105 | Not a member of this organization. |
| 40324 | Incorrect DevKey or DevSecret. |
| 40378 | The Agent has been deleted. |
| 403132 | Invalid time range: the start time is not earlier than the end time, or the range exceeds the maximum query range. |

## **Statistical Scope**

- **Look at both numbers**: On instant messaging channels, a conversation continues in the same session unless there are no new messages for 60 minutes, so an active channel Agent may go a long time without new conversations. Looking only at the new conversation count may wrongly flag it as inactive.
- **Channel scope**: Only Development Space channels are counted, including API, share pages, web embeds, bubble widgets, LiveDesk, and the various instant messaging and phone channels. Development Space debug previews and usage of the Agent in a workspace are not included.
- **Update frequency**: Calculated in real time.
