_Last updated at: 2025-12-15_

## **Get Conversation Message Details**

Retrieve all message details within a conversation using the conversation_id parameter. The response includes message_id, user queries, message types, message content, message timestamps, and more.

## **Request Method**

GET

## **Endpoint**

`https://altatech.ai/v2/messages`

## **Authentication**

Refer to API Overview for authentication instructions.

## **Request**

### Example Request

```
curl -X GET 'https://altatech.ai/v2/messages?conversation_id=xxxxxx&page=1&page_size=100' \
-H 'Authorization: Bearer ${API Key}'
```

### Request Headers

| Field | Type | Description |
|-------|------|-------------|
| Authorization | Bearer ${API Key} | Use Authorization: Bearer ${API Key} for authentication. Obtain your API key from the API Key page. |

### Request Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| conversation_id | string | Yes | Conversation identifier. |
| page | int | Yes | Page number to request. |
| page_size | int | Yes | Number of items per page, up to 100. |

## **Response**

### Example Response

```
{
  "total": 2,
  "conversation_content": [
    {
      "message_id": "645dd86906931c4a9e0ffb1f",
      "parent_message_id": "545dd86906931c4a9e0ffb1f",
      "create_time": 1683871849906,
      "feedback": "POSITIVE",
      "role": "user",
      "content": [
        {
          "branch_content": [
            {
              "type": "text",
              "text": "I have uploaded 2 image files, please OCR and return 2 json records."
            },
            {
              "type": "image",
              "image": [
                {
                  "url": "https://altabots.ai/example.png",
                  "format": "jpeg",
                  "name": "TAXI1",
                  "size": 1024
                },
                {
                  "url": "https://altabots.ai/example.png",
                  "format": "png",
                  "name": "TAXI2",
                  "size": 1024
                }
              ]
            },
            {
              "type": "audio",
              "audio": [
                {
                  "url": "https://altabots.ai/example.mp3",
                  "format": "mp3",
                  "name": "example1 audio",
                  "size": 1024
                }
              ]
            },
            {
              "type": "document",
              "document": [
                {
                  "url": "https://altabots.ai/example.pdf",
                  "format": "pdf",
                  "name": "example pdf",
                  "size": 1024
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "message_id": "745dd86906931c4a9e0ffb1f",
      "parent_message_id": "645dd86906931c4a9e0ffb1f",
      "create_time": 1683871849906,
      "feedback": "POSITIVE",
      "role": "assistant",
      "content": [
        {
          "from_component_branch": "1",
          "branch_content": [
            {
              "type": "text",
              "text": "Hi, is there anything I can help you?"
            },
            {
              "type": "audio",
              "audio": [
                {
                  "url": "http://altabots.ai/example.mp3",
                  "transcript": "Transcribed text content of the audio"
                }
              ]
            }
          ]
        },
        {
          "from_component_branch": "2",
          "branch_content": [
            {
              "type": "document",
              "document": [
                {
                  "url": "https://altabots.ai/example.pdf",
                  "format": "pdf",
                  "name": "example pdf"
                }
              ]
            },
            {
              "type": "image",
              "image": [
                {
                  "url": "https://altabots.ai/example.png",
                  "format": "png",
                  "name": "TAXI2"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### Successful Response

| Field | Type | Description |
|-------|------|-------------|
| total | string | Total number of messages in the conversation. |
| conversation_content | JSON Array | Message details. |
| message_id | string | Unique identifier for the message. |
| parent_message_id | string | Unique identifier for the parent message. |
| create_time | long | Timestamp when the message was created. |
| feedback | string | User feedback for the message, values: POSITIVE, NEGATIVE. No feedback returns empty. |
| role | string | Message role: user or assistant. |
| content | JSON Array | Message content. |
| from_component_branch | string | Component branch ID of the message source. Empty for user messages and regular Agents. |
| branch_content | JSON Array | Branch content of the message. |
| type | string | Message content type: text, image, audio, document, video, file. |
| text | string | Text message content. |
| image | JSON Array | Image message content. |
| audio | JSON Array | Audio message content. |
| document | JSON Array | Document message content. |
| video | JSON Array | Video message content. |
| file | JSON Array | File message content. |

### Error Response

| Field | Type | Description |
|-------|------|-------------|
| code | int | Error code. |
| message | string | Error details. |

### Error Codes

| Code | Message |
|------|---------|
| 40000 | Invalid parameters |
| 40005 | Pagination parameter exceeds actual count |
| 40127 | Developer authentication failed |
| 40356 | Conversation does not exist |
| 20059 | Agent has been deleted |
