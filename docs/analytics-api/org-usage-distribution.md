_Last updated at: 2026-10-20_

# **Get Organization Credit Usage Distribution**

Retrieve the share ranking of the organization's credits or tokens by Agent / Workflow, along with trends by day, week, or month. You can view Agents only or Workflows only.

Note: Data can be queried for a maximum range of 92 days; only the Development Space is counted. See "Statistical Scope" below for details.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/org/usage/distribution`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication: `Authorization: Basic ${BASIC_TOKEN}`, where `${BASIC_TOKEN}` is the Base64 encoding of `DevKey:DevSecret`.

The calling account must be a member of the organization specified by `org_id` and have the "View Usage" permission (organization Owners and Admins have it by default).

## **Request Frequency**

- Each developer key can call this API up to 10 times per minute.
- Each call also counts toward the per-minute quota of the organization plan's "Statistics API", shared with statistics API calls made with Agent API Keys.
- Query results are cached for 10 minutes; calling once per day is recommended.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/org/usage/distribution?org_id=${org_id}&start_time=1792425600000&end_time=1792684800000&agent_type=WORKFLOW&granularity=DAY' \
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
| end\_time | Long | Yes | End time (exclusive), in milliseconds timestamp. The date range can span up to 92 days. |
| metric | String | No | `CREDITS` (default) or `TOKENS`. |
| granularity | String | No | Trend time granularity: `DAY` (default), `WEEK` (weeks start on Monday), `MONTH`. |
| agent\_type | String | No | `AGENT` for Agents only, `WORKFLOW` for Workflows only; if omitted, both types are ranked together. |
| top\_n | Integer | No | Number of trend series rows to keep, from 1 to 50, default 50; the rest are merged into an `OTHER` row. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "timezone": "+07:00",
    "data_since": "2026-10-15",
    "buckets": ["2026-10-16", "2026-10-17", "2026-10-18"],
    "total": 812.4411,
    "series": [
      {
        "row_type": "ITEM",
        "agent_id": "65f0c2a1b4e8d93a1c7e5b2a",
        "name": "Order Inquiry",
        "agent_type": "WORKFLOW",
        "total": 402.1200,
        "share": 49.49,
        "points": [130.5000, 141.0200, 130.6000]
      },
      {
        "row_type": "OTHER",
        "agent_id": null,
        "name": null,
        "agent_type": null,
        "total": 410.3211,
        "share": 50.51,
        "points": [120.1000, 150.2000, 140.0211]
      }
    ],
    "ranking": [
      {
        "row_type": "ITEM",
        "agent_id": "65f0c2a1b4e8d93a1c7e5b2a",
        "name": "Order Inquiry",
        "agent_type": "WORKFLOW",
        "total": 402.1200,
        "share": 49.49
      }
    ]
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| timezone | String | Organization time zone (UTC offset, e.g. `+07:00`). |
| data\_since | String | The earliest date for which credit data is available (`yyyy-MM-dd`); ranges before this date are incomplete. `null` if there is no data yet. |
| buckets | String[] | Start of each time bucket in ascending order: the date for `DAY`, the Monday for `WEEK` (`yyyy-MM-dd`), `yyyy-MM` for `MONTH`. `points` follow this order. |
| total | Number | Total amount in the range (credits or tokens, depending on `metric`). |
| series | Object[] | Top `top_n` rows used for trends, sorted by total in descending order; the rest are merged into one `row_type = OTHER` row. |
| ranking | Object[] | Full ranking, up to 500 rows; any excess is merged into one `OTHER` row. Does not include `points`. |
| series[].row\_type / ranking[].row\_type | String | `ITEM` is an Agent or Workflow; `OTHER` is a merged row; `UNATTRIBUTED` is consumption not attributed to any Agent (e.g. knowledge base storage, speech recognition), and is not returned when `agent_type` is specified. |
| series[].agent\_id / ranking[].agent\_id | String | Agent or Workflow ID; `null` for `OTHER` / `UNATTRIBUTED`. |
| series[].name / ranking[].name | String | Name; `null` for `OTHER` / `UNATTRIBUTED`. |
| series[].agent\_type / ranking[].agent\_type | String | `AGENT` or `WORKFLOW`; `null` for `OTHER` / `UNATTRIBUTED`. |
| series[].total / ranking[].total | Number | Total in the range, rounded to 4 decimal places. |
| series[].share / ranking[].share | Number | Percentage of the range total, from 0 to 100, rounded to 2 decimal places. |
| series[].points | Number[] | Value for each time bucket. |

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

- **Scope**: Only the Development Space is counted, including API, share pages, web embeds, bubble widgets, LiveDesk, the various instant messaging and phone channels, and Development Space Workflows. Workspace usage, including usage of published Agents in workspaces, is not included, so the total may be slightly lower than the same period on the console's "Organization → Usage" page.
- **Credits**: All consumption types (excluding credit expiration and subscription payments); Workflow consumption is recorded under the Workflow itself.
- **Data start**: Available from the feature launch date (`data_since`); historical data is not backfilled.
- **Update frequency**: Updated in real time.
