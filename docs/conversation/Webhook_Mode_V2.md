_Last updated at: 2025-10-20_

# **Webhook Mode V2**

The current AltaBots Agent message response modes support: blocking, streaming, and webhook. When developers use the webhook mode to receive response messages, the message content provided by the Agent or human customer service will be submitted to the specified webhook address.

## **Request Method**

POST

## **Request URL**

`Please configure your message acceptance address on the Agent - Integration - API - webhook page.`

## **Authentication**

For details, refer to the authentication method description in the API Overview.

## **Request**

### **Request Example**

```
curl -X POST YOUR_API \ 
  -H 'Authorization: Bearer your_apikey' \ 
  -H 'Content-Type: application/json' \ 
  -d '{
  "message_id": "65a4ccfC7ce58e728d5897e0",
  "message_type": "ANSWER",
  "text": "Hi, is there anything I can help you?",
  "flow_output": [
    {
      "content": "你好",
      "branch": "1",
      "from_component_name": "User Input"
    }
  ],
  "create_time": 1679587005,
  "conversation_id": "657303a8a764d47094874bbe"
}
'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer or Basic {token} | Use Authorization: Bearer OR Basic {token} for authentication. Obtain the token from the API Key page. |
| Content-Type | application/json | Data type, value is application/json. |

### **Request Body**

| Field | Type | Description |
| :---- | :---- | :---- |
| conversation\_id | string | Unique identifier for the conversation. |
| message\_id | string | Unique ID of the message. |
| create\_time | long | Timestamp when the message was generated. |
| message\_type | string | Message type, values: ANSWER, QUESTION. |
| text | string | Text content provided by the Agent. |
| output | JSON Array | Content of the Agent's reply in Flow mode. |
| from\_component\_branch | string | FlowAgent branch. |
| from\_component\_name | string | Upstream component name in FlowAgent. |
| content | object | AI Agent response message content, currently includes text and audio message types. |
| usage | object | Usage consumption. |
| output | JSON Array | Total tokens consumed by the Agent in this conversation. |
| total\_tokens | integer | Total tokens consumed for input \+ output in this conversation. |
| prompt\_tokens | integer | Total tokens consumed for input in this conversation. |
| completion\_tokens | integer | Total tokens consumed for output in this conversation. |
| prompt\_tokens\_details | object | Token consumption details for input in this conversation. |
| completion\_tokens\_details | object | Token consumption details for output in this conversation. |
| credits | object | Total credits consumed by the Agent in this conversation. |
| text\_input\_credits | double | Credits consumed for input text messages in this conversation. |
| text\_output\_\_credits | double | Credits consumed for output text messages in this conversation. |
| audio\_input\_credits | double | Credits consumed for input audio messages in this conversation. |
| audio\_output\_credits | double | Credits consumed for output audio messages in this conversation. |

## **Response**

### **Response Example**

```
{
  "code": 200,
  "msg": "success"
}
```
