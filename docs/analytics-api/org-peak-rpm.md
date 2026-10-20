_Last updated at: 2026-10-20_

# **Get Organization Peak RPM**

Retrieve the organization's peak RPM (requests per minute) within a time range: requests from all Agents in the organization are first summed per minute, then the highest minute in the range is taken. The time the peak occurred, the average RPM, and the total number of requests are also returned.

Note: Data can be queried for a maximum range of 31 days; only Development Space channels are counted. See "Statistical Scope" below for details.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/org/stat/rpm`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication: `Authorization: Basic ${BASIC_TOKEN}`, where `${BASIC_TOKEN}` is the Base64 encoding of `DevKey:DevSecret`.

The calling account must be a member of the organization specified by `org_id` and have the "View Usage" permission (organization Owners and Admins have it by default).

## **Request Frequency**

- Each developer key can call this API up to 60 times per minute.
- Each call also counts toward the per-minute quota of the organization plan's "Statistics API", shared with statistics API calls made with Agent API Keys.
- Data is updated hourly; repeated queries within the same hour return the same result, so calling once per hour is recommended.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/org/stat/rpm?org_id=${org_id}&start_time=1788192000000&end_time=1788796800000' \
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
| start\_time | Long | Yes | Start time, in milliseconds timestamp. Rounded down to the nearest hour. |
| end\_time | Long | Yes | End time (exclusive), in milliseconds timestamp. Rounded up to the nearest hour. The aligned range cannot exceed 31 days. |

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "org_id": "65f0c2a1b4e8d93a1c7e5b20",
    "range_start": 1788192000000,
    "range_end": 1788796800000,
    "data_until": 1788793200000,
    "data_since": 1786125600000,
    "peak_rpm": 186,
    "peak_at": 1788512460000,
    "avg_rpm": 12.40,
    "total_requests": 2083411
  }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| org\_id | String | Organization ID. |
| range\_start | Long | Start of the actual statistics range: `start_time` aligned down to the hour, in milliseconds timestamp. |
| range\_end | Long | End of the actual statistics range (exclusive): `end_time` aligned up to the hour, in milliseconds timestamp. |
| data\_until | Long | Time up to which data has been counted (milliseconds timestamp). Parts of the range after this time have no data yet. |
| data\_since | Long | The earliest whole hour from which the organization has RPM data (milliseconds timestamp; the same for all organizations, roughly 31 days before the feature launch). Parts of the range before this time have no data; `null` if there is no data at all. |
| peak\_rpm | Long | Peak RPM: requests from all Agents in the organization summed per minute, taking the highest minute within the range. |
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
| 40100 | No permission: missing the "View Usage" permission. |
| 40105 | Not a member of this organization. |
| 40324 | Incorrect DevKey or DevSecret. |
| 403132 | Invalid time range: the start time is not earlier than the end time, or the range exceeds the maximum query range. |

## **Statistical Scope**

- **Requests**: Question messages submitted by users, plus conversation errors (including requests rejected for exceeding the call frequency), consistent with "Agent Insights → Requests per Minute" in the console. This is not the number of HTTP requests and may differ from the count used by plan rate limits.
- **Channel scope**: Only requests made to Development Space Agents through Development Space channels are counted, including API, share pages, web embeds, bubble widgets, LiveDesk, and the various instant messaging and phone channels. Development Space debug previews, Workflows (including Workflow API calls rejected for exceeding the call frequency), workspace AI search, and usage of published Agents in workspaces are not included.
- **Data range**: Data is available from 31 days before the feature launch; refer to `data_since` for the earliest available time.
- **Update frequency**: Data is aggregated on the hour every hour with about a 1-hour delay; refer to `data_until`.
- **Difference from the console**: The console's "Organization → Usage → RPM" page shows each day split into 24 hourly segments, while this API returns a single peak value for the whole range and the time it occurred.
