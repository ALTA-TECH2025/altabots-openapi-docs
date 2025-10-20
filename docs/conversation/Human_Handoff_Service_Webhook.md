_Last updated at: 2025-10-20_

# **Human Handoff Service - Webhook**

AltaBots.ai currently supports three products or services for human-assisted service: `Intercom`, `LiveChat`, and `Webhook`. When developers choose webhook as the integration method for human-assisted service, they first need to build a Webhook service in their own server environment, providing the following three interfaces to process initialization requests from Agents for human-assisted service and to receive user messages. When developers choose webhook as the method for accessing human handoff services, they first need to build a Webhook receiving service in their own server environment, providing the following three interfaces to receive human handoff services requests initiated by the Agent and to receive messages.

## **Create Conversation ID**

Used to create a human handoff services conversation ID for Agent users.

### **Request Method**

`POST`

### **Request URL**

`https://your_domain/conversation/establish`

### **Request Example**

```shell
curl -v -X POST https://YOUR_DOMAIN/human/service/conversation/establish \
--header "Content-Type: application/json" \
--data '{
  "body": [
    {
      "text": "human service",
      "message_type": "QUESTION"
    },
    {
      "text": "",
      "message_type": "ANSWER"
    }
  ],
  "timestamp": 1742265090895,
  "email": "bob@gmail.com",
  "conversation_id": "67d8db020fa31d1ef64f53dg",
  "bot_id": "665d88b03ce2b13cf2d573454",
  "user_info": {
    "phone": null,
    "email": "bob@gmail.com",
    "user_id": "KDslas",
    "anonymous_id": "652face5184b30540a6ea7fe"
  }
}'
```

**Request Parameters**

| Parameter | Type | Description |
| ----- | ----- | ----- |
| conversation\_id | string | Conversation ID, needs to be passed through to AltaBots.ai in the customer service reply interface |
| timestamp | long | Timestamp |
| email | string | User email, required by some human service systems to provide normal service |
| bot\_id | string | Agent (formerly bot) ID |
| body | list\<Object\> | Message body |
| body.message\_type | string | Message type, QUESTION/ANSWER |
| body.text | string | Questions and context initiated by the customer for human customer service |
| user\_info | object | User information |
|     user\_info.phone | string | User's phone number, currently only available when transferring to human customer service via WhatsApp |
|     user\_info.email | string | User's email, available when the user inputs an email |
|     user\_info.user\_id | string | User ID. A unique user identity identifier customized by enterprise developers, set by developers for a specific anonymous ID |
|     user\_info.anonymous\_id | string | Anonymous ID. When a user initiates a conversation with the Agent on non-API channel platforms, the system generates an anonymous ID containing the information of the channel platform where the user is located |

### **Response**

| Parameter | Type | Description |
| ----- | ----- | ----- |
| code | int | Response code |
| message | string | Details |

## **Chat Interface**

Agent users send messages to human handoff services.

### **Request Method**

`POST`

### **Request URL**

`https://your_domain/chat`

### **Request Parameters**

| Parameter | Type | Description |
| ----- | ----- | ----- |
| conversation\_id | string | Conversation ID, needs to be propagated to AltaBots.ai in the human handoff services reply interface |
| timestamp | long | Timestamp |
| body | string | Message content |

### **Response**

| Parameter | Type | Description |
| ----- | ----- | ----- |
| code | int | Response code |
| message | string | Details |

## **Close Conversation Interface**

When a user conversation times out or the Agent user actively closes the conversation, this interface is called to close the conversation.

### **Request Method**

`POST`

### **Request URL**

`https://your_domain/conversation/close`

### **Request Parameters**

| Parameter | Type | Description |
| ----- | ----- | ----- |
| conversation\_id | string | Conversation ID, needs to be propagated to AltaBots.ai in the human handoff services reply interface |
| timestamp | long | Timestamp |
| type | string | Type of closure, TIMEOUT (timeout) / USER\_CLOSED (user-initiated closure) |

### **Response**

| Parameter | Type | Description |
| ----- | ----- | ----- |
| code | int | Response code |
| message | string | Details |

When developers choose webhook as the method for accessing human services, AltaBots.ai provides an API interface for receiving human handoff services reply messages and conversation control commands sent by developers.

## **Receive Customer Service Messages**

When developers choose webhook as the manual service access method, AltaBots.ai provides an interface for receiving manual customer service reply messages from the Webhook endpoint and sends the message content to the user.

### **Request Method**

`POST`

### **Request URL**

`https://altatech.ai/v1/human/message/receive` 

### **Request Parameters**

| Parameter | Type | Description | Required |
| ----- | ----- | ----- | ----- |
| conversation\_id | string | Conversation ID, propagated in the conversation creation interface and chat interface | true |
| timestamp | long | Timestamp | true |
| body | string | human handoff services reply content | true |

### **Response**

| Parameter | Type | Description |
| ----- | ----- | ----- |
| code | int | Response code |
| message | string | Details |

## **Manual Customer Service Closes Conversation**

When developers choose webhook as the manual service access method, the manual customer service provided by AltaBots can actively close the conversation when needed. After closure, the user will no longer receive messages from the customer service unless the user initiates a manual customer service conversation again.

### **Request Method**

`POST`

### **Request URL**

`https://altatech.ai/v1/human/close` 

### **Request Parameters**

| Parameter | Type | Description |
| ----- | ----- | ----- |
| conversation\_id | string | Conversation ID, needs to be passed through to AltaBots.ai in the human handoff services reply interface |
| timestamp | long | Timestamp |

### **Response**

| Parameter | Type | Description | Required |
| ----- | ----- | ----- | ----- |
| conversation\_id | string | Conversation ID, passed in the conversation creation interface and chat interface, just pass it through | true |
| timestamp | long | Timestamp | true |
