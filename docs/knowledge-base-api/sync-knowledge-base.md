_Last updated at: 2026-10-13_

# **Sync Knowledge Base Now**

Immediately triggers an incremental sync of the **sourced knowledge** in a knowledge base. Currently only the Google Drive source is supported.

> **Note:**
>
> - The endpoint returns immediately after completing validation and planning, so what it returns is "accepted", not "updated".
> - Rate limit: at most 1 request per minute per Agent / Workflow.

## **Request Method**

POST

## **Request URL**

Choose the corresponding path based on the resource type that the API Key belongs to. The request parameters, response structure, and rate-limiting rules of the two endpoints are exactly the same.

- Agent: `https://altatech.ai/v1/agent/knowledge-base/sync`
- Workflow: `https://altatech.ai/v1/workflow/knowledge-base/sync`

The request / response descriptions below apply to both paths; the examples are written using the Agent path.

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

Sync specified knowledge bases:

```bash
curl -X POST 'https://altatech.ai/v1/agent/knowledge-base/sync' \
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json' \
-d '{
    "source": "google-drive",
    "knowledge_base_ids": ["6a44c3512ceb43775567391c", "6a44c3512ceb43775567391d"]
}'
```

Sync all knowledge bases under this Agent:

```bash
curl -X POST 'https://altatech.ai/v1/agent/knowledge-base/sync' \
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json' \
-d '{
    "source": "google-drive"
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${API Key} | Use Authorization: Bearer ${API Key} for authentication. Get the key from the API Keys page and use it as the API Key. |
| Content-Type | application/json | Data type, with the value `application/json`. |

### **Request Parameters**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| source | String | Yes | Source type. Currently only `google-drive` is supported; passing any other value returns a parameter error. |
| knowledge\_base\_ids | Array&lt;String&gt; | No | List of target knowledge base IDs, **at most 200**; exceeding this returns a parameter error. Omitting it, passing `null`, or passing an empty array means all knowledge bases under this Agent / Workflow. IDs in the list that do not exist or do not belong to the current Agent / Workflow do not cause the whole request to fail; they appear in `skipped`. |

## **Response**

### **Response Example**

```json
{
    "code": 0,
    "message": "OK",
    "data": {
        "accepted": true,
        "source": "google-drive",
        "matched_knowledge_base_count": 2,
        "matched_doc_count": 37,
        "matched_folder_count": 3,
        "skipped": [
            {
                "reason": "DRIVE_NOT_AUTHORIZED",
                "message": "The document owner has not authorized Google Drive, or the authorization has expired.",
                "knowledge_base_id": "6a44c3512ceb43775567391e",
                "doc_count": 8
            },
            {
                "reason": "KNOWLEDGE_BASE_NOT_FOUND",
                "message": "Knowledge base does not exist or does not belong to this agent.",
                "knowledge_base_id": "deadbeefdeadbeefdeadbeef"
            }
        ],
        "scheduled_round_running": false
    }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Return code; `0` means success. |
| message | String | Return message. |
| data | Object | Acceptance result. |
| data.accepted | Boolean | Whether it has been accepted. `false` means nothing was started this time; see `skipped` for the reason. |
| data.source | String | The source type of this sync. |
| data.matched\_knowledge\_base\_count | Integer | The number of knowledge bases matched this time. |
| data.matched\_doc\_count | Integer | The number of knowledge documents that will be checked this time. Note that this is "will be checked", not "have been updated". |
| data.matched\_folder\_count | Integer | The number of folder sources that will be checked for newly added files this time. |
| data.skipped | Array&lt;Object&gt; | Details of what was skipped, aggregated by "knowledge base + reason", not expanded per document. |
| data.skipped[].reason | String | The skip reason; see the table below for values. |
| data.skipped[].message | String | Reason description. |
| data.skipped[].knowledge\_base\_id | String | The affected knowledge base ID. Not returned for overall reasons (such as insufficient balance). |
| data.skipped[].doc\_count | Integer | The number of affected documents. Not returned when the whole knowledge base is skipped. |
| data.scheduled\_round\_running | Boolean | Whether the system's scheduled sync round is currently running. For information only; it does not affect this acceptance. When `accepted` is `false`, this determination is not made this time and `null` is returned. |

### **`skipped[].reason` Values**

| Value | Meaning | Suggested Handling |
| :---- | :---- | :---- |
| KNOWLEDGE\_BASE\_NOT\_FOUND | The knowledge base does not exist, or does not belong to the Agent / Workflow bound to the current API Key. | Check `knowledge_base_ids`; you can first call [Get Knowledge Base List](get-knowledge-base-list.md) to confirm. |
| NO\_GOOGLE\_DRIVE\_SOURCE | The knowledge base exists, but it does not contain any documents from Google Drive. | This is normal and means the knowledge base does not need syncing. |
| DRIVE\_NOT\_AUTHORIZED | The member that owns the document has no usable Google Drive authorization (never authorized, or the authorization has expired). | Have the member re-authorize Google Drive. |
| DOC\_IN\_PROGRESS | The document is being processed. Usually a scheduled round or the previous sync has not finished. | Retry later, or wait for the processing to finish. |
| DOC\_NO\_OWNER | The document lacks owner member information, so it is impossible to determine whose Google Drive authorization to use. | Contact support to investigate this document. |
| INSUFFICIENT\_BALANCE | The organization balance is insufficient. In this case `accepted` is `false` and no sync is started. | Top up and retry. |
| SYNC\_IN\_PROGRESS | The previous manual sync of this Agent / Workflow is still running. In this case `accepted` is `false`. | Wait for the previous one to finish and retry. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |

Response example when `source` is invalid:

```json
{
    "code": 40000,
    "message": "Unsupported source: sharepoint. Supported: google-drive"
}
```

### **Error Codes**

| HTTP | Code | Scenario |
| :---- | :---- | :---- |
| 400 | 40000 | `source` is missing or unsupported; `knowledge_base_ids` exceeds 200; the number of documents matched in a single call exceeds 5000 (use `knowledge_base_ids` to narrow the scope). |
| 400 | 40001 | Triggered too frequently, exceeding the endpoint's rate limit. |
| 401 | 40101 | The `Authorization` request header is missing. |
| 401 | 40127 | The API Key is invalid. |

## **Usage Notes**

### **It returns "accepted", not "completed"**

The endpoint returns immediately after completing validation and planning; the actual fetching, parsing, and vectorization run asynchronously in the background. Therefore `matched_doc_count` is "how many documents will be checked this time", not "how many documents were updated". To confirm the final result, poll the [Get Doc List](get-knowledge-doc-list.md) endpoint to check document status; when a document's status becomes `AVAILABLE`, it means the document has finished syncing.

### **It only does incremental sync and does not consume quota repeatedly**

For each document, the system first compares the last modified time on Google Drive:

- Source document unchanged: skipped; it is not re-downloaded or re-parsed, and does not consume quota.
- Source document changed: re-fetched, re-parsed, and re-vectorized.
- New files in a bound folder: automatically added as knowledge documents.

Therefore calling this endpoint repeatedly is safe; unchanged content does not incur extra charges.

### **This endpoint cannot retry documents that failed to parse**

The incremental judgment only looks at whether the source document on Google Drive has changed, not what status the document is currently in.

Therefore, a document that previously failed to parse (with status `FAIL`) will not be reprocessed by this endpoint as long as its source file on Google Drive has not been modified — it will be treated as "source document unchanged" and skipped directly, its status stays unchanged, and it will not appear in `skipped`.

To retry documents that failed to parse, use the [Re-embed Failed Docs](re-embed-failed-docs.md) endpoint. Or make a modification to the source file on Google Drive so that its last modified time is updated, and this endpoint will re-fetch it.

### **Syncing deletes knowledge documents**

This endpoint does not only add and update; it also deletes knowledge documents according to the current state of Google Drive.

- When a bound Google Drive folder becomes empty, all knowledge documents already imported from that folder are deleted.
- The trigger condition is that the folder is still accessible on Google Drive but no files can be enumerated in it. The system first validates the folder's accessibility; when it cannot obtain the folder metadata (the folder was moved, permissions changed, temporarily unreachable, etc.), it skips the deletion to avoid accidental removal.
- The deletion scope is limited to "this folder + this knowledge base". When the same Google Drive folder is referenced by multiple knowledge bases, the knowledge bases do not affect each other.

This behavior is consistent with the system's scheduled sync; this endpoint simply makes it happen earlier. However, because this endpoint also covers documents that had no scheduled sync plan configured at import time (which would not otherwise be deleted by any automatic process), confirm before calling that the folder content on the Google Drive side is as expected.

### **Coverage**

The sync scope covers all documents from Google Drive in the knowledge base, including the portion that had no scheduled sync plan configured at import time — this portion is not processed by the system's scheduled rounds and can only be updated through this endpoint.

### **Rate Limiting**

- At most 1 request per minute per Agent / Workflow. The two paths share the same counter, so switching paths does not bypass the rate limit.
- It is also subject to the requests-per-minute (RPM) limit for knowledge-base APIs of the organization plan, sharing that quota with other knowledge-base endpoints.
- When the previous sync of the same Agent / Workflow has not finished, calling again returns `accepted=false` and `reason=SYNC_IN_PROGRESS`.

### **Relationship with Scheduled Sync**

- This endpoint and the system's scheduled sync are independent of each other and do not block each other. When `scheduled_round_running` is `true`, this request is still accepted and will not be rejected because a scheduled round is running.
- When both process the same document at the same time, they do not produce duplicate content: the system makes an incremental judgment based on the source document's last modified time, and already imported files are not created again.
- Scheduled sync runs automatically at the frequency configured for each knowledge base, while this endpoint ignores that frequency and triggers immediately. The two complement each other: scheduled sync handles routine updates, and this endpoint handles the "sync right now" scenario.
