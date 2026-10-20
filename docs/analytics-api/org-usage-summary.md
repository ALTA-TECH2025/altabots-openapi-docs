_Last updated at: 2026-10-20_

# **Get Organization Usage Summary**

Retrieve the organization's total credit consumption, new conversation count, and user question count within a time range, broken down by Agent / Workflow with pagination. A single call returns data for all Agents in the organization, so there is no need to call each Agent individually.

Note: Data can be queried for a maximum range of 31 days; only the Development Space is counted. See "Statistical Scope" below for details.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/org/stat/summary`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication: `Authorization: Basic ${BASIC_TOKEN}`, where `${BASIC_TOKEN}` is the Base64 encoding of `DevKey:DevSecret`.

The calling account must be a member of the organization specified by `org_id` and have the "View Usage" permission (organization Owners and Admins have it by default).

## **Request Frequency**

- Each developer key can call this API up to 60 times per minute.
- Each call also counts toward the per-minute quota of the organization plan's "Statistics API", shared with statistics API calls made with Agent API Keys.
- Queries that include today or yesterday are cached for 5 minutes; results for earlier dates are cached for 1 hour. Calling every 5 to 15 minutes is recommended.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/org/stat/summary?org_id=${org_id}&start_time=1792425600000&end_time=1795017600000&page=1&page_size=20' \
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
| start\_time | Long | Yes | Start time, in milliseconds timestamp. Extended to 00:00 of that day in the organization's time zone. |
| end\_time | Long | Yes | End time (exclusive), in milliseconds timestamp. The last day is the calendar day (in the organization's time zone) of the millisecond before this time. The date range can span up to 31 days. |
| agent\_type | String | No | Break down only one type: `AGENT` or `WORKFLOW`; if omitted, both types are listed. Only affects the `agents` list, not `total`. |
| page | Integer | No | Page number, starting from 1, default 1, maximum 10000. |
| page\_size | Integer | No | Number of items per page, default 20, maximum 100. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "org_id": "65f0c2a1b4e8d93a1c7e5b20",
    "timezone": "+07:00",
    "range_start_date": "2026-10-16",
    "range_end_date": "2026-11-14",
    "data_since": "2026-10-15",
    "data_until": 1794614400000,
    "total": {
      "credits": 1234.5678,
      "unattributed_credits": 36.2011,
      "conversation_count": 5210,
      "message_count": 48213
    },
    "agents": {
      "page": 1,
      "page_size": 20,
      "total": 86,
      "list": [
        {
          "agent_id": "65f0c2a1b4e8d93a1c7e5b21",
          "name": "Customer Service Assistant",
          "agent_type": "AGENT",
          "credits": 402.1200,
          "conversation_count": 2104,
          "message_count": 19820
        },
        {
          "agent_id": "65f0c2a1b4e8d93a1c7e5b2a",
          "name": "Order Inquiry",
          "agent_type": "WORKFLOW",
          "credits": 130.5000,
          "conversation_count": null,
          "message_count": null
        }
      ]
    }
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| org\_id | String | Organization ID. |
| timezone | String | Organization time zone (UTC offset, e.g. `+07:00`), indicating which time zone the dates are split by. |
| range\_start\_date | String | Actual statistics start date, `yyyy-MM-dd` (organization time zone, inclusive). |
| range\_end\_date | String | Actual statistics end date, `yyyy-MM-dd` (organization time zone, inclusive). |
| data\_since | String | The earliest date from which data is complete (`yyyy-MM-dd`): credits are available from the feature launch date, conversation and question counts from 31 days before launch; the later of the two is used. Data before this date is incomplete. `null` if there is no data yet. |
| data\_until | Long | Time up to which conversation and question counts have been counted (milliseconds timestamp). Credits are real-time. |
| total.credits | Number | Total organization credit consumption, including Workflows and credits not attributed to any Agent, with 4 decimal places. |
| total.unattributed\_credits | Number | Portion not attributed to any Agent (e.g. knowledge base storage, speech recognition); not included in the `agents` list. |
| total.conversation\_count | Long | Total number of new conversations within the range. |
| total.message\_count | Long | Total number of user questions within the range, excluding AI replies. |
| agents.page | Integer | Current page number. |
| agents.page\_size | Integer | Number of items per page. |
| agents.total | Integer | Number of Agents and Workflows with data in the range (after filtering by `agent_type`). |
| agents.list[].agent\_id | String | Agent or Workflow ID. |
| agents.list[].name | String | Name. |
| agents.list[].agent\_type | String | `AGENT` or `WORKFLOW`. |
| agents.list[].credits | Number | Credit consumption. |
| agents.list[].conversation\_count | Long | Number of conversations created in the range; `null` for Workflows. |
| agents.list[].message\_count | Long | Number of user questions in the range; `null` for Workflows. |

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
| 40100 | No permission: missing the "View Usage" permission. |
| 40105 | Not a member of this organization. |
| 40324 | Incorrect DevKey or DevSecret. |
| 403132 | Invalid time range: the start time is not earlier than the end time, or the range exceeds the maximum query range. |

## **Statistical Scope**

- **Scope**: Only the Development Space is counted, including API, share pages, web embeds, bubble widgets, LiveDesk, the various instant messaging and phone channels, and Development Space Workflows. Workspace usage, including usage of published Agents in workspaces, is not included.
- **Credits**: All consumption types (excluding credit expiration and subscription payments). Workflow consumption is recorded under the Workflow itself; consumption generated when an Agent calls a Workflow is not counted toward that Agent. Credit data is available from the feature launch date (`data_since`); historical data is not backfilled.
- **Conversation count**: The number of conversations created within the range that have had at least one interaction, excluding Development Space debug previews. Workflow runs do not create conversations; workspace AI search is not counted. Conversation and question counts are available from 31 days before the feature launch.
- **Question count**: The number of question messages sent by users within the range, excluding AI replies.
- **Sorting**: `agents.list` is sorted by credits in descending order, then by conversation count. Agents with no credits, conversations, or questions in the range are not listed.
- **Update frequency**: Credits are updated in real time; conversation and question counts are updated on the hour every hour with about a 1-hour delay.
