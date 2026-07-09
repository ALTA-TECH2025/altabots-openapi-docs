_Last updated at: 2025-10-20_

# **Get Agent Information**

Get Agent basic information.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/bot/detail`

## **Request Authentication**

See Overview for authentication details.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/bot/detail' \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Get the key from the API Keys page as token. |
| Content-Type | application/json | Data type, set to application/json. |

### **Request Body**

None.

## **Response**

### **Response Example**

```
{
  "bot_id": "645dd86606931c4a9e0ffb1e",
  "name": "Conversational App",
  "logo": "https://altatech.ai/images/default_avatar.png",
  "bot_type": "QuestionAnswer",
  "welcome_message": "Welcome message when user first uses the bot",
  "introduction": "Introduction of the agent",
  "tags": "Tags of the agent",
  "identity_prompt": "Identity prompt of the agent",
  "ai_model": "ChatGPT",
  "ai_model_version": "3.5", 
  "creativity_level": 0.3,
  "doc_correlation": 0.2,
  "irrelevant_questions": true,
  "question_limit": 100,
  "long_term_memory": true
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| bot\_id | string | Agent ID. |
| name | string | Agent name. |
| logo | string | Agent avatar. |
| bot\_type | string | Agent type, value: QuestionAnswer, Flow. |
| welcome\_message | string | Welcome message when user first uses the agent. |
| introduction | string | Introduction of the agent. |
| tags | array | Tags of the agent. |
| identity\_prompt | string | Identity prompt of the agent. |
| ai\_model | string | AI model, value: ChatGPT. |
| ai\_model\_version | string | AI model version. |
| creativity\_level | float | Creativity level, value: 0-1. |
| doc\_correlation | float | Document correlation, value: 0-1. |
| irrelevant\_questions | boolean | Whether to answer questions irrelevant to dataset. Value: true, false. |
| question\_limit | int | Limit on Token length of user questions. |
| long\_term\_memory | boolean | Whether long term memory is enabled. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 40127 | Developer authentication failed |
| 20059 | Agent deleted |
