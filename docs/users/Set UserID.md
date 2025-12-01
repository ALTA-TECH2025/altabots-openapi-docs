_Last updated at: 2025-12-01_

# **Set User ID**

Assign a persistent `user_id` to agent users so that identities stay consistent across channels. The identifier enables cross-channel merging, business tool lookups, attribute management, chat history continuity, and enriched event callbacks.

⚠️ Use the same `user_id` that uniquely identifies the customer in your business system (CRM, membership ID, etc.).

## **Application Scenarios**

1. **Tool calls** – `user_id` is forwarded in Tool request headers so downstream services can resolve the user context.
2. **User attributes** – All properties are stored under the bound `user_id`, enabling centralized profiling.
3. **Chat logs** – Conversation history across widgets, iframe, or API channels is attached to the same identity.
4. **Event callbacks** – Bubble widget / iframe callbacks embed `user_id`, allowing analytics systems (GA4, webhooks) to join events with first-party data.


## **API: Set User ID**

Developers must set a `user_id` before creating a `conversation_id` via API.

### **Request Method**

POST

### **Request URL**

`https://altatech.ai/v1/conversation`

### **Request Authentication**

See Overview for authentication details.

### **Request Example**

```
curl -X POST https://altatech.ai/v1/conversation \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json' \
  -d '{
        "user_id": "your_user_id"
      }'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use `Authorization: Bearer {token}` for authentication. Generate the API key in Console. |
| Content-Type | application/json | Request payload format. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| user_id | string | Yes | Custom identifier that links to your customer record. |

## **Widget & Embedded Channels**

Refer to Bubble Widget / iframe advanced usage docs for full integration walkthroughs.

