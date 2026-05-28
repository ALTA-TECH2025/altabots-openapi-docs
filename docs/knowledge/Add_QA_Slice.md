_Last updated at: 2025-10-20_

## **Add QA Slice**

You can use this API to append QA slices (knowledge blocks) to an existing QA knowledge document. Batch addition is supported, and each slice can have custom keywords.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/bot/doc/qa/chunks/add`

## **Authentication**

See the authentication method description in API Overview.

## **Request Example**

```
curl -X POST https://altatech.ai/v1/bot/doc/qa/chunks/add \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json' \
  -d '{
      "doc_id": "680d1a2b3c4d5e6f7a8b9c0d",
      "chunks": [
        {
          "question": "How to contact customer service?",
          "answer": "You can contact us through the online customer service button at the bottom right corner of the official website. Working hours are Monday to Friday 9:00-18:00.",
          "keywords": ["customer service", "contact information", "online customer service"]
        },
        {
          "question": "What is the refund process?",
          "answer": "After logging in, go to the order management page, select the order you want to refund, click apply for refund and fill in the reason.",
          "keywords": ["refund", "return", "order"]
        }
      ]
    }'
```

## **Request Headers**

| Field         | Type              | Description                                                                                   |
|---------------|-------------------|-----------------------------------------------------------------------------------------------|
| Authorization | Bearer ${token}   | Use Authorization: Bearer ${token} for authentication. Get the token from API Key page.        |
| Content-Type  | application/json  | Data type, value must be application/json.                                                     |

## **Request Body**

| Field    | Type   | Required | Description                                                                                      |
|----------|--------|----------|--------------------------------------------------------------------------------------------------|
| doc_id   | string | Yes      | Target QA knowledge document id. Document type must be qa or qafile.                             |
| chunks   | list   | Yes      | List of QA slices. Cannot be empty.                                                              |

- The chunks list cannot be empty. Each slice's question and answer are required.
- Each slice's keywords support up to 50 items. Exceeding this will return an error.

## **Response Example**

```
{
    "code": 0,
    "message": "OK"
}
```

## **Successful Response**

| Field   | Type   | Description                       |
|---------|--------|-----------------------------------|
| code    | int    | Status code, 0 means success.     |
| message | string | Status message.                   |

## **Failure Response**

| Field   | Type   | Description                       |
|---------|--------|-----------------------------------|
| code    | int    | Error code.                       |
| message | string | Error description.                |

## **Error Codes**

| Code   | Message                |
|--------|------------------------|
| 40000  | Parameter error        |
| 50000  | Internal system error  |
