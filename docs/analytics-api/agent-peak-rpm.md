_Last updated at: 2026-10-20_

# **Get Agent Peak RPM**

Retrieve the peak RPM (requests per minute) of a specified Agent within a time range, along with the time the peak occurred, the average RPM, and the total number of requests.

Note: Data can be queried for a maximum range of 31 days; only Development Space channels are counted. See "Statistical Scope" below for details.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/org/agent/stat/rpm`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication: `Authorization: Basic ${BASIC_TOKEN}`, where `${BASIC_TOKEN}` is the Base64 encoding of `DevKey:DevSecret`.

The calling account must be a member of the organization specified by `org_id` and have the "View Usage" permission (organization Owners and Admins have it by default), and must be able to view this Agent: the Agent creator, the organization Owner, or a member granted permission for this Agent (or all Agents).

## **Request Frequency**

- Each developer key can call this API up to 60 times per minute.
- Each call also counts toward the per-minute quota of the organization plan's "Statistics API", shared with statistics API calls made with Agent API Keys.
- Data is updated hourly; repeated queries within the same hour return the same result, so calling once per hour is recommended.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/org/agent/stat/rpm?org_id=${org_id}&agent_id=${agent_id}&start_time=1788192000000&end_time=1788796800000' \
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
| start\_time | Long | Yes | Start time, in milliseconds timestamp. Rounded down to the nearest hour. |
| end\_time | Long | Yes | End time (exclusive), in milliseconds timestamp. Rounded up to the nearest hour. The aligned range cannot exceed 31 days. |
| conversation\_type | String | No | Count only a specific channel, such as `API`, `SHARE`, `EMBED`, `WIDGET`, `LIVEDESK`. Must be a Development Space channel; if omitted, all Development Space channels are counted. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "agent_id": "65f0c2a1b4e8d93a1c7e5b21",
    "range_start": 1788192000000,
    "range_end": 1788796800000,
    "data_until": 1788793200000,
    "peak_rpm": 42,
    "peak_at": 1788512460000,
    "avg_rpm": 3.18,
    "total_requests": 18234
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| agent\_id | String | Agent ID. |
| range\_start | Long | Start of the actual statistics range: `start_time` aligned down to the hour, in milliseconds timestamp. |
| range\_end | Long | End of the actual statistics range (exclusive): `end_time` aligned up to the hour, in milliseconds timestamp. |
| data\_until | Long | Time up to which data has been counted (milliseconds timestamp). Parts of the range after this time have no data yet. |
| peak\_rpm | Long | Peak RPM: the number of requests in the minute with the most requests (summed across all channels) within the range. |
| peak\_at | Long | Start of the peak minute (milliseconds timestamp). If several minutes tie, the earliest is returned; `null` if there are no requests in the range. |
| avg\_rpm | Number | Average RPM: total requests ÷ number of minutes with requests, rounded to 2 decimal places. |
| total\_requests | Long | Total number of requests in the range. |

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

- **Requests**: Question messages submitted by users, plus conversation errors (including requests rejected for exceeding the call frequency), consistent with "Agent Insights → Requests per Minute" in the console. This is not the number of HTTP requests and may differ from the count used by plan rate limits.
- **Channel scope**: Only Development Space channels are counted, including API, share pages, web embeds, bubble widgets, LiveDesk, and the various instant messaging and phone channels. Development Space debug previews, Workflow runs, and usage of the Agent after it is deployed to a workspace are not included.
- **Update frequency**: Data is aggregated on the hour every hour with about a 1-hour delay; refer to `data_until`. Data before 2026-03-09 has no minute-level detail, so queries for that period return 0.
