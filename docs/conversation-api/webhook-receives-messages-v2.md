_Last updated at: 2026-07-09_

# **Webhook receives messages**

AltaBots Agent currently supports three message response modes: `blocking`, `streaming`, and `webhook`. When developers use the `webhook` mode to receive response messages, both AI responses and human responses will be submitted to the specified webhook URL.

| Response Mode | Supported Message Types |
| :---- | :---- |
| blocking | AI responses |
| streaming | AI responses |
| webhook | Human responses, AI responses |

## **Send Message API Pushes Response Messages to Webhook**

### **Request Method**

POST

### **Request URL**

Please configure your message receiving address on the Agent - Integration - API - webhook page.

### **Authentication**

Both Basic authentication and Bearer authentication are supported. Developers can choose the appropriate authentication method based on their own situation and configure it on the Agent - Integration - API - webhook page.

- When integrating the webhook URL, if the developer only fills in the webhook username, AltaBots will use Bearer authentication by default when initiating requests to the developer's webhook URL, with the value being the webhook username filled in by the developer.
- When integrating the webhook URL, if the developer fills in both the webhook username and the webhook secret, AltaBots will use Basic authentication when initiating requests to the developer's webhook URL, with the username being the webhook username and the password being the webhook secret filled in by the developer.

### **Request Example**

```
curl -X POST 'YOUR_API_URL' \
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json' \
-d '{
  "create_time": 1679587005,
  "user_id": "65a4ccfc7ce58e728d5897e0",
  "anonymous_id": "device_abcdef123456",
  "conversation_id": "657303a8a764d47094874bbe",
  "message_id": "65a4ccfC7ce58e728d5897e0",
  "output": [
    {
      "from_component_branch": "1",
      "from_component_name": "Component Name",
      "content": {
        "text": "Hi, is there anything I can help you?",
        "audio": [
          {
            "audio": "http://altatech.ai/example.mp3",
            "transcript": "The transcribed content of the audio"
          }
        ]
      }
    }
  ],
  "usage": {
    "tokens": {
      "total_tokens": 29,
      "prompt_tokens": 19,
      "prompt_tokens_details": {
        "audio_tokens": 0,
        "text_tokens": 0
      },
      "completion_tokens": 10,
      "completion_tokens_details": {
        "reasoning_tokens": 0,
        "audio_tokens": 0,
        "text_tokens": 0
      }
    },
    "credits": {
      "total_credits": 0.0,
      "text_input_credits": 0.0,
      "text_output_credits": 0.0,
      "audio_input_credits": 0.0,
      "audio_output_credits": 0.0
    }
  }
}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer or Basic {token} | Use Authorization: Bearer OR Basic {token} for authentication. Obtain the token from the API Key page. |
| Content-Type | application/json | Data type, value is application/json. |

### **Request Body**

| Field | Type | Description |
| :---- | :---- | :---- |
| user\_id | string | The user ID bound by the developer; null when no user is bound. |
| anonymous\_id | string | Anonymous user (device) ID. |
| conversation\_id | string | Unique identifier for the conversation. |
| message\_id | string | Unique identifier for a specific message within a conversation. |
| create\_time | long | Timestamp when the message was generated. |
| output | JSON Array | AI Agent response content. |
| from\_component\_branch | string | FlowAgent branch. |
| from\_component\_name | string | Upstream component name in FlowAgent. |
| content | object | AI Agent response message content, currently includes text and audio message types. |
| usage | object | Usage consumption. |
| tokens | JSON Array | Total tokens consumed by the Agent in this conversation. |
| total\_tokens | integer | Total tokens consumed for input \+ output in this conversation. |
| prompt\_tokens | integer | Total tokens consumed for input in this conversation. |
| completion\_tokens | integer | Total tokens consumed for output in this conversation. |
| prompt\_tokens\_details | object | Token consumption details for input in this conversation. |
| completion\_tokens\_details | object | Token consumption details for output in this conversation. |
| credits | object | Total credits consumed by the Agent in this conversation. |
| text\_input\_credits | double | Credits consumed for input text messages in this conversation. |
| text\_output\_credits | double | Credits consumed for output text messages in this conversation. |
| audio\_input\_credits | double | Credits consumed for input audio messages in this conversation. |
| audio\_output\_credits | double | Credits consumed for output audio messages in this conversation. |

## **Response Specification**

After the developer's webhook service successfully receives the message, it must return HTTP status code 200, and the response body should return a JSON-formatted success identifier.

```
{
  "code": 200,
  "msg": "success"
}
```

## **AltaBots Webhook Service Status Detection**

AltaBots provides a health monitoring endpoint for detecting its own webhook service. Developers can call this endpoint to probe whether the AltaBots webhook service is available and working properly. If the endpoint returns HTTP status code 200 and the response body is an English identifier indicating the service is normal (such as `service is normal`), it means the AltaBots webhook service is available and working properly.

This endpoint requires no authentication and returns plain text.

### **Request Method**

GET

### **Request URL**

`https://altatech.ai/v1/webhook/service/health`

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/webhook/service/health'
```

### **Response**

When the AltaBots service is available and working properly, it returns HTTP status code 200, and the response body returns an English identifier indicating the service is normal.

```
service is normal
```

### **Availability Determination Recommendations**

The caller only needs to use the HTTP status code as the criterion:

| Situation | Determination |
| :---- | :---- |
| Returns 200 and the response body is `service is normal` | AltaBots service is available |
| Returns non-200 (such as 5xx) / request timeout / connection failure | AltaBots service is unavailable |

It is recommended to set a reasonable request timeout (such as 3 to 5 seconds) and poll at a fixed frequency (QPM: 3). This endpoint requires no authentication, so there is no need to carry an API Key when calling it.
