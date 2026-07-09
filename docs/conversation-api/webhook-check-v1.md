_Last updated at: 2026-07-09_

# **Webhook Detection Service**

Allows developers to detect the availability of the AltaBots webhook service and the availability of the webhook URLs configured on a target Agent.

## **Detect the availability of the webhook services configured on an Agent**

AltaBots allows developers to detect, via API, the availability of all Webhook URLs configured on a target Agent, including the webhook URLs configured for receiving "Send Message" and "Human handoff service - webhook". When a developer calls this API, AltaBots automatically detects all Webhook URLs configured on the Agent that the current API Key belongs to, with no need to specify a detection target, and returns the detection result for each Webhook item by item in the response.

The developer Webhook services involved by the `istest` field are as follows:

- The request body of the Send Message API responding to a webhook contains this field. See Webhook receives messages.
- The request body for receiving human service conversation request notifications and user messages contains this field. See Human handoff service.

When a developer's Webhook service receives a request, it should identify the `istest` field in the message body: when `istest=true`, it is an availability test request and should not be processed as a real business message (e.g. do not store it, do not trigger human service, etc.), and returning HTTP status code `200` indicates that the Webhook is available.

### **Request Method**

POST

### **Request URL**

`https://altatech.ai/v1/webhook/check`

### **Request Authentication**

For details, refer to the authentication instructions in API Overview. This API identifies the target Agent by the API Key and detects the Webhooks configured under that Agent.

### **Request Example**

```
curl -X POST 'https://altatech.ai/v1/webhook/check' \
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer ${API Key} | Use Authorization: Bearer ${API Key} for authentication. Get the key from the API Key page as the API Key. |
| Content-Type | application/json | Data type, set to application/json. |

### **Request Parameters**

This API requires no request parameters. AltaBots automatically detects all Webhook URLs configured on the Agent that the current API Key belongs to.

## **Response**

### **Response Example**

```
{
    "results": [
        {
            "type": "message",
            "component_id": null,
            "component_name": null,
            "webhook_url": "https://your_domain/webhook/message",
            "reachable": true,
            "http_status": 200,
            "latency_ms": 156
        },
        {
            "type": "human_service",
            "component_id": "665d88b03ce2b13cf2d57346",
            "component_name": "Presale Human Service",
            "webhook_url": "https://your_domain/presale/human/service/conversation/establish",
            "reachable": true,
            "http_status": 200,
            "latency_ms": 188
        },
        {
            "type": "human_service",
            "component_id": "665d88b03ce2b13cf2d57347",
            "component_name": "Aftersale Human Service",
            "webhook_url": "https://your_domain/aftersale/human/service/conversation/establish",
            "reachable": false,
            "http_status": 502,
            "latency_ms": 3000
        }
    ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| results | JSON Array | List of detection results, returning the detection result of each configured Webhook of the Agent item by item. Webhooks that are not configured do not appear in the list. When the same Agent has multiple human service (handoff) components configured, each component corresponds to one `human_service` result. |
| type | string | Webhook type. `message`: the Webhook for receiving Agent response messages; `human_service`: the Webhook configured for the webhook mode of a human service component. |
| component\_id | string | The unique identifier ID of the human service (handoff) component, used to distinguish scenarios with multiple human service components configured. It is `null` for the `message` type. |
| component\_name | string | The name of the human service (handoff) component. It is `null` for the `message` type. |
| webhook\_url | string | The Webhook URL being detected. |
| reachable | boolean | Whether the Webhook is available. `true` means available, `false` means unavailable. |
| http\_status | int | The HTTP status code returned by the detection request; `null` or `0` on connection failure or timeout. |
| latency\_ms | long | The time taken by the detection request (in milliseconds). |

### **Availability Determination Suggestion**

AltaBots sends a detection request carrying `istest=true` to the Webhook URL in the standard message format, and determines availability based on the returned result:

| Case | Determination |
| :---- | :---- |
| Returns HTTP status code 200 | The Webhook is available (`reachable=true`) |
| Returns a non-200 code (e.g. 4xx/5xx) / request timeout / connection failure | The Webhook is unavailable (`reachable=false`) |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40000 | Parameter error |
| 40127 | Developer authentication failed |
| 40378 | Agent deleted |

## **AltaBots Webhook Service Status Detection**

AltaBots provides a health monitoring API for detecting the webhook service. Developers can call this API to probe whether the AltaBots webhook service is working normally. If the API returns HTTP status code `200` and the response body is an English indicator of normal service (such as `service is normal`), it means the AltaBots webhook service is working normally.

This API requires no authentication and returns plain text.

### **Request Method**

GET

### **Request URL**

`https://altatech.ai/v1/webhook/service/health`

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/webhook/service/health'
```

### **Response**

When the AltaBots service is working normally, it returns HTTP status code `200`, and the response body returns an English indicator of normal service.

```
service is normal
```

### **Availability Determination Suggestion**

The caller only needs to use the HTTP status code as the criterion:

| Case | Determination |
| :---- | :---- |
| Returns 200 and the response body is `service is normal` | The AltaBots service is working normally |
| Returns a non-200 code (e.g. 5xx) / request timeout / connection failure | The AltaBots service is unavailable |

It is recommended to set a reasonable request timeout (e.g. 3-5 seconds) and probe by polling at a fixed frequency (QPM:3); this API requires no authentication, so there is no need to carry an API Key when calling it.
