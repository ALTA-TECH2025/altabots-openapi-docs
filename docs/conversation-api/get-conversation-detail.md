_Last updated at: 2026-10-20_

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
  "quality_score": null,
  "conversation_content": [
    {
      "message_id": "645dd86906931c4a9e0ffb1f",
      "parent_message_id": "545dd86906931c4a9e0ffb1f",
      "create_time": 1683871849906,
      "feedback": "POSITIVE",
      "source_page": "https://your-site.com/pricing",
      "sentiment_label": "neutral",
      "question_categories": [
        {
          "category_id": "6893485e1aca766e47b0e892",
          "category_name": "Pricing"
        }
      ],
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
                  "url": "https://altatech.ai/example.png",
                  "format": "jpeg",
                  "name": "TAXI1",
                  "size": 1024
                },
                {
                  "url": "https://altatech.ai/example.png",
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
                  "url": "https://altatech.ai/example.mp3",
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
                  "url": "https://altatech.ai/example.pdf",
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
      "source_page": "https://your-site.com/pricing",
      "sentiment_label": "positive",
      "question_categories": [],
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
                  "url": "http://altatech.ai/example.mp3",
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
                  "url": "https://altatech.ai/example.pdf",
                  "format": "pdf",
                  "name": "example pdf"
                }
              ]
            },
            {
              "type": "image",
              "image": [
                {
                  "url": "https://altatech.ai/example.png",
                  "format": "png",
                  "name": "TAXI2"
                }
              ]
            }
          ]
        }
      ]
    }
  ],
  "audio_record_url": "https://altatech.ai/record/full-call.mp3",
  "user_sender": {
    "channel_type": "Channel::Whatsapp",
    "user_id": "+66812345678",
    "profile": {
      "name": "John Doe"
    },
    "additional_attributes": {},
    "provider": "whatsapp_cloud",
    "phone_number": "+66900000000"
  }
}
```

### Successful Response

| Field | Type | Description |
|-------|------|-------------|
| total | int | Total number of messages in the conversation. |
| quality_score | float | AI quality inspection score (conversation level), ranging from 0 to 1. null if the conversation has not been inspected or AI quality inspection is not enabled. |
| conversation_content | JSON Array | Message details. |
| message_id | string | Unique identifier for the message. |
| parent_message_id | string | Unique identifier for the parent message. |
| create_time | long | Timestamp when the message was created. |
| feedback | string | User feedback for the message, values: POSITIVE, NEGATIVE. No feedback returns empty. |
| source_page | string | Source page of this message, i.e. the URL of the web page the user was on when the message was created. Currently, only the Livechat channel supports this field; the value is empty when the conversation source is not Livechat. |
| sentiment_label | string | Sentiment label of the message, aligned with the sentiment field in conversation logs. Values: very_positive, positive, neutral, negative, very_negative, none; null if sentiment analysis has not been performed. |
| question_categories | JSON Array | Question category tags of this message, from the same source as the Question Category column on the Logs - Conversation Records page; an empty array if there is no category. |
| category_id | string | Question category ID. |
| category_name | string | Question category name. |
| role | string | Message role. Values: user, assistant. System notice messages related to human customer service (e.g., connected-to-human or session-timeout notices) do not return this field. |
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
| audio_record_url | string | URL of the full-call recording file of the voice call. Only available for voice (Audio) Agents; this field is not returned when there is no recording. |
| user_sender | JSON Object | User channel information. For third-party channel integrations (currently LiveDesk), it is stored when the conversation comes inbound, taken from the sender channel information of the channel webhook (supports channels such as WhatsApp / LINE), and shares the same source as the flow variable `ld_user_sender`. This field is not returned when not collected; see the table below for common fields. |

### Common user_sender Fields

This object is the user channel information passed through from the source channel. Fields vary by channel; the following are common fields, and the actual fields are subject to what the channel returns.

| Field | Type | Description |
|-------|------|-------------|
| channel_type | string | Channel type, such as `Channel::Whatsapp`, `Channel::Line`, `Channel::Webwidget`, etc. |
| user_id | string | User identifier on the channel side: phone number/wa_id for WhatsApp, userId for LINE, and identifier for other channels. |
| profile | JSON Object | User profile (e.g. name). |
| additional_attributes | JSON Object | Additional channel attributes. |
| provider | string | Channel provider. |
| phone_number | string | Phone number configured on the channel side. |

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
