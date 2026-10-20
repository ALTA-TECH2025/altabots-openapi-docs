_Last updated at: 2026-10-20_

# **Get Agent Escalation Rate**

Retrieve the number of conversations, the number of conversations escalated to human agents, and the escalation rate of a specified Agent within a time range. The methodology is consistent with "Agent Insights → Escalation Rate" in the console.

Note: Data can be queried for a maximum range of 92 days; only Development Space channels are counted. See "Statistical Scope" below for details.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/org/agent/stat/human-handoff`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication: `Authorization: Basic ${BASIC_TOKEN}`, where `${BASIC_TOKEN}` is the Base64 encoding of `DevKey:DevSecret`.

The calling account must be a member of the organization specified by `org_id` and have the "View Usage" permission (organization Owners and Admins have it by default), and must be able to view this Agent: the Agent creator, the organization Owner, or a member granted permission for this Agent (or all Agents).

## **Request Frequency**

- Each developer key can call this API up to 60 times per minute.
- Each call also counts toward the per-minute quota of the organization plan's "Statistics API", shared with statistics API calls made with Agent API Keys.
- Query results are cached for 10 minutes; calling once per hour is recommended.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/org/agent/stat/human-handoff?org_id=${org_id}&agent_id=${agent_id}&start_time=1788192000000&end_time=1790784000000' \
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
| agent\_id | String | Yes | Agent ID. Workflow is not supported. |
| start\_time | Long | Yes | Start time, in milliseconds timestamp. Extended to 00:00 of that day in the organization's time zone. |
| end\_time | Long | Yes | End time (exclusive), in milliseconds timestamp. The last day is the calendar day (in the organization's time zone) of the millisecond before this time. The date range can span up to 92 days. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "agent_id": "65f0c2a1b4e8d93a1c7e5b21",
    "timezone": "+08:00",
    "range_start_date": "2026-09-01",
    "range_end_date": "2026-09-29",
    "data_until": 1790665200000,
    "conversation_count": 1200,
    "handoff_conversation_count": 96,
    "handoff_rate": 0.0800
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| agent\_id | String | Agent ID. |
| timezone | String | Organization time zone (UTC offset, e.g. `+08:00`), indicating which time zone the dates are split by. |
| range\_start\_date | String | Actual statistics start date, `yyyy-MM-dd` (organization time zone, inclusive). |
| range\_end\_date | String | Actual statistics end date, `yyyy-MM-dd` (organization time zone, inclusive). |
| data\_until | Long | Time up to which data has been counted (milliseconds timestamp). If the range includes dates calculated in real time, this is the calculation time of the real-time part (results cached for up to 10 minutes); if the whole range is covered by completed daily statistics, this is the end of the range. |
| conversation\_count | Long | Number of conversations with activity within the range (accumulated by day). |
| handoff\_conversation\_count | Long | Number of conversations escalated to human agents. |
| handoff\_rate | Number | Escalation rate = `handoff_conversation_count` ÷ `conversation_count`, from 0 to 1, rounded to 4 decimal places; `null` if the conversation count is 0. |

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

- **Conversation count**: The number of conversations with activity on each day, accumulated by day; a conversation that continues across days is counted once for each day.
- **Escalated conversation count**: The number of conversations that were escalated to a human agent.
- **Channel scope**: Only Development Space channels are counted, including API, share pages, web embeds, bubble widgets, LiveDesk, and the various instant messaging and phone channels. Usage after the Agent is published to a workspace is not included.
- **Update frequency**: Dates with completed daily statistics are read from the daily statistics; the current day is calculated in real time. Daily statistics are generated after midnight in the organization's time zone; until they are complete, the previous day is also calculated in real time, so "yesterday" never shows 0 right after midnight.
- **Real-time methodology**: The real-time part counts each conversation by the time of its latest message, so a conversation that continues across days is counted only once (on the day of its latest message). This may differ slightly from the day-by-day accumulated daily statistics.
