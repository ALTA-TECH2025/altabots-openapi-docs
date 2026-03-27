_Last updated at: 2026-03-27_

## **Send Message**

Through this API, you can send a message to the specified `conversation_id` and receive the Agent's generated response. The API supports submitting text, image, audio, and document as message content.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v2/conversation/message`

## **Authentication**

See the authentication method described in the API Overview.

## **Request Example**

```
curl -X POST 'https://altatech.ai/v2/conversation/message' \
-H 'Authorization: Bearer ${API Key}' \
-H 'Content-Type: application/json' \
-d '{
    "conversation_id": "686e2646cb8ee942d9a62d79",
    "response_mode": "blocking",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "I have uploaded 2 image files, please OCR and return 2 json records."
                },
                {
                    "type": "image",
                    "image": [
                        {
                            "base64_content": "<complete_base64_string>",
                            "format": "jpeg",
                            "name": "TAXI1"
                        },
                        {
                            "url": "https://altatech.ai/example.png",
                            "format": "png",
                            "name": "TAXI2"
                        }
                    ]
                },
                {
                    "type": "audio",
                    "audio": [
                        {
                            "url": "https://altatech.ai/example.mp3",
                            "format": "mp3",
                            "name": "example1 audio"
                        }
                    ]
                },
                {
                    "type": "document",
                    "document": [
                        {
                            "base64_content": "<complete_base64_string>",
                            "format": "pdf",
                            "name": "example pdf"
                        }
                    ]
                }
            ]
        }
    ],
    "conversation_config": {
        "long_term_memory": false,
        "short_term_memory": false,
        "knowledge": {
            "data_ids": [
                "58c70da0403cc812641b9356",
                "59c70da0403cc812641df35a"
            ],
            "group_ids": [
                "67c70da0403cc812641b93je",
                "69c70da0403cc812641df35f"
            ]
        },
        "custom_variables": {
            "var_current_url": "https://altatech.ai/example",
            "var_session_id": "abcdef"
        },
        "corner_citation": true
    }
}'
```

**Notes:**
- `image`, `audio`, and `document` all support both base64 encoding and URL links; choose one method.
- Developers can submit only the latest user message. altabots will automatically assemble short-term and long-term memory. If you need to customize short-term memory, refer to the following example:

```
"messages": [
    {
        "role": "user",
        "content": "Hello"
    },
    {
        "role": "assistant",
        "content": "Hello! How can I assist you today?"
    },
    {
        "role": "user",
        "content": "Hello"
    }
]
```

## **Request Headers**

| Field         | Type              | Description                                                                                 |
|---------------|-------------------|--------------------------------------------------------------------------------------------|
| Authorization | string            | Use `Authorization: Bearer ${API Key}` for authentication. Obtain your API Key from the API Key page. |
| Content-Type  | application/json  | Data type, must be `application/json`.                                                     |

## **Request Parameters**

| Field                | Type        | Required | Description                                                                                                                                                                                                                                                                                                                                                  |
|----------------------|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| conversation_id      | string      | Yes      | Unique identifier for the conversation. Must provide the `conversation_id` to continue the conversation.                                                                                                                                                                                                                                                     |
| response_mode        | string      | Yes      | The response and delivery mode for the AI Agent's reply. <br> `blocking`: Waits for completion before returning results (may be interrupted if the process is long). <br> `streaming`: Returns results in a streaming fashion using SSE (Server-Sent Events). <br> `webhook`: Both Agent and human agent messages are sent to the configured webhook address. |
| messages             | JSON Array  | Yes      | Conversation message content. Supports two roles: `user` and `assistant` to construct the conversation context. <br> At least one `user` message is required, and the latest `user` message should be last. <br> Developers can construct `assistant` messages as context.                                            |
| conversation_config  | object      | No       | Allows developers to temporarily adjust the Agent's function scope for special scenarios.                                                                                                                                                                                                                                                                    |

**Notes:**
- The Agent input/output configuration page supports different recognition schemes for different message types. Supported file types and sizes may vary. Adjust the API submission data accordingly.
- Maximum supported formats:
  - Text: string
  - Audio: .mp3, .wav
  - Image: .jpg, .jpeg, .png, .gif, .webp
  - Document: .pdf, .txt, .docx, .csv, .xlsx, .html, .json, .md, .tex, .ts, .xml, etc.

## **Response**

### **Response Example**

```
{
    "create_time": 1679587005,
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
                        "transcript": "Transcribed audio content"
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
    },
    "citations": [
        {
            "index": "1",
            "name": null,
            "type": "attachment",
            "content": "Text fragment of the citation",
            "segment_id": "b405464c-bbab-4a86-8",
            "segment_index": 1,
            "position": "",
            "timestamp_millis": 1772712445224,
            "data_id": "2328972389327892",
            "bot_id": "69a64bf0e01fd8172ca9826e",
            "attachment": {
                "id": "2328972389327892",
                "url": "https://altatech.ai/gfs/api/media/ailab/bot/chat/file/69a80c3cf303e87b81dfb127/20260305200722sus8a5.png",
                "name": "example.png",
                "type": "png"
            },
            "component_id": null
        }
    ]
}
```

### **Citation Mark Format Description**

When `corner_citation: true` is set in the request, the Agent's reply text will include citation superscript marks in the format `$[index]$`, for example:

- `$[1]$` indicates citation source 1
- `$[2]$` indicates citation source 2

`$[1]$` can appear anywhere in the text, indicating the referenced content at that position. In the response, each element in the `citations` array corresponds to a citation source, and the `index` field matches the superscript index in the text.

**Example:**

Text content: `"Here is a detailed explanation$[1]$: The order amount is $325.00$[1]$."`  
The element in the `citations` array with `index` "1" is the citation source for this mark.

---

### **Success Response (Blocking)**

⚠️ Human agent takeover is not available in blocking mode.

| Field           | Type        | Description                                                                 |
|-----------------|------------|-----------------------------------------------------------------------------|
| conversation_id | string     | Yes                                                                         |
| message_id      | string     | Unique identifier for a message in the conversation.                        |
| create_time     | long       | Timestamp when the reply message was generated.                             |
| output          | JSON Array | Agent reply content.                                                        |
| usage           | object     | Usage and consumption.                                                      |
| citations       | JSON Array | No                                                                          |

---

### **Success Response (Streaming)**

⚠️ Human agent takeover is not available in streaming mode.

| Field   | Type | Description                                                                                                                                                                                                                                                  |
|---------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| code    | int  | Message type code: 3-Text, 10-Flowagent Output, 0-End, 4-Usage Data, 39-Audio Message, 5-Tool Call Request, 6-Tool Call Response, 41-Thought, 83-Correlate Attachment Info, 20-Citation Info.                         |
| message | string | Message type: Text, FlowOutput, End, CorrelateAttachment, Citation.                                                                                                                                                                                        |
| data    | object | Reply content.                                                                                                                                                                                                                                              |

**Text message streaming data is returned in multiple parts:**

```
{"code":11,"message":"MessageInfo","data":{"message_id":"6785dba0f06d872bff9ee347"}}
{"code":3,"message":"Text","data":"I"}
{"code":3,"message":"Text","data":" can"}
{"code":3,"message":"Text","data":" help"}
{"code":3,"message":"Text","data":" you"}
{"code":3,"message":"Text","data":" with"}
{"code":3,"message":"Text","data":" that"}
{"code":3,"message":"Text","data":"."}
{"code":10,"message":"FlowOutput","data":[{"content":"Hello","branch":null,"from_component_name": "User Input"}]}
{"code":4,"message":"Cost","data":{"prompt_tokens":4922,"completion_tokens":68,"total_tokens":4990,"prompt_tokens_details":{"audio_tokens":0,"text_tokens":4922},"completion_tokens_details":{"reasoning_tokens":0,"audio_tokens":0,"text_tokens":68}}}
{"code":0,"message":"End","data":null}
```

**Audio message streaming data is returned in multiple parts:**

```
{"code":11,"message":"MessageInfo","data":{"message_id":"67b857b6be1f2906861a5e75"}}
{"code":39,"message":"Audio","data":{"audioAnswer":"","transcript":"Hello"}}
{"code":39,"message":"Audio","data":{"audioAnswer":"","transcript":", please"}}
{"code":39,"message":"Audio","data":{"audioAnswer":"","transcript":" ask"}}
{"code":39,"message":"Audio","data":{"audioAnswer":"","transcript":" anything"}}
{"code":39,"message":"Audio","data":{"audioAnswer":"EQAUAA0...IA3bi","transcript":""}}
{"code":39,"message":"Audio","data":{"audioAnswer":"EQAUAA0...IA3bi","transcript":""}}
{"code":39,"message":"Audio","data":{"audioAnswer":"EQAUAA0...IA3bi","transcript":""}}
{"code":10,"message":"FlowOutput","data":[{"content":" Audio:https://altatech.ai/example.wav,Transcript:(Hello! How can I assist you today?)","audioDatas":[{"transcript":"Hello! How can I assist you today?","url":"https://altatech.ai/example.wav","seconds":3}],"from_component_name":"AI Model-1"}],"componentId":12}
{"code":4,"message":"Cost","data":{"prompt_tokens":4922,"completion_tokens":68,"total_tokens":4990,"prompt_tokens_details":{"audio_tokens":0,"text_tokens":4922},"completion_tokens_details":{"reasoning_tokens":0,"audio_tokens":0,"text_tokens":68}}}
{"code":0,"message":"End","data":null}
```

**When `corner_citation: true` is set, streaming responses will include correlated attachment and citation info:**

**Correlate Attachment:**

```
{"code":83,"message":"CorrelateAttachment","data":[{"dataId":"69b1580c1c34273cb83caa24","dataName":"20260310175133jdj5gy.mp4","dataType":"mp4","url":"https://altatech.ai/gfs/api/media/ailab/bot/chat/file/69aa7d15014f3d626657ac70/20260311195437gmc4dr.mp4","content":"...","segmentId":"9c92b533-f457-4840-9","segmentIndex":1,"dimensions":0,"timestampMillis":1773230092549,"position":"","componentId":null,"showDocCorrelation":null,"nodeId":null}]}
```

**Citation:**

```
{"code":20,"message":"Citation","data":[{"citation":{"index":"1","name":null,"type":"attachment","tool":null,"doc":null,"attachment":{"id":"69b1580c1c34273cb83caa24","url":"https://altatech.ai/gfs/api/media/ailab/bot/chat/file/69aa7d15014f3d626657ac70/20260311195437gmc4dr.mp4","name":"20260310175133jdj5gy.mp4","type":"mp4","content":"..."},"segmentIndex":1,"timestampMillis":1773230092549,"position":"","segmentId":"9c92b533-f457-4840-9","botId":"697b097da21cf757465bcd0a","dataId":"69b1580c1c34273cb83caa24","toolId":null,"content":"..."}}]}
```

**Explanation:**
- `code: 83`, `message: "CorrelateAttachment"`: Correlated attachment info, including basic info and content fragment.
- `code: 20`, `message: "Citation"`: Citation info, including full citation source details, same structure as `citations` in blocking response.
- `type` in citation info may be: `attachment`, `doc`, or `tool`.
- When `type` is `attachment`, the `attachment` field contains attachment details; when `doc`, the `doc` field contains document details; when `tool`, the `tool` field contains tool details.

---

### **Success Response (Webhook)**

⚠️ Human agent takeover is available in webhook mode.

When the Agent is configured with human agent service, use webhook response mode to receive human agent reply messages. After configuring the webhook address in "Integration-API", the altabots system will send both "Agent" and "Human Agent" response messages to the webhook address.

**Webhook configuration:**  
See [Webhook Mode and Human Agent Service](#).

---

## **Error Response**

| Field   | Type   | Description      |
|---------|--------|------------------|
| code    | int    | Error code.      |
| message | string | Error details.   |

### **Error Codes**

| Code   | Message                                                        |
|--------|----------------------------------------------------------------|
| 40000  | Parameter error                                                |
| 40127  | Developer authentication failed                                |
| 40356  | Conversation does not exist                                    |
| 40358  | Conversation ID does not match agent or user                   |
| 40364  | The agent does not use a large model that supports image mode  |
| 50000  | Internal system error                                          |
| 20040  | Exceeded question length limit                                 |
| 20022  | Insufficient credits                                           |
| 20055  | API function is disabled, please ensure the API switch is on   |
