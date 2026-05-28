_Last updated at: 2025-10-20_

## **Update QA Knowledge Document**

You can use this API to update existing QA knowledge documents in the Agent's knowledge base. Two update methods are supported: replacing QA text content or updating QA files.

## **Request Method**

PUT

## **Request URL**

`https://altatech.ai/v1/bot/doc/qa/update`

## **Authentication**

See the authentication method description in the API Overview.

## **Request**

### **Request Example**

**QA Text Update Method:**
```
curl -X PUT https://altatech.ai/v1/bot/doc/qa/update \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json' \
  -d '{
      "doc_id": "680d1a2b3c4d5e6f7a8b9c0d",
      "knowledge_base_id": "673af861ed69656ac0895b07",
      "qaList": [
        {
          "question": "How to register an account?",
          "answer": "Visit the official website homepage, click the register button in the upper right corner, fill in your email, set a password, and complete email verification."
        },
        {
          "question": "How to reset the password?",
          "answer": "On the login page, click the forgot password link, enter the registered email, and follow the instructions in the email to reset."
        }
      ]
    }'
```

**QA File Update Method:**
```
curl -X PUT https://altatech.ai/v1/bot/doc/qa/update \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json' \
  -d '{
      "knowledge_base_id": "673af861ed69656ac0895b07",
      "files": [
        {
          "doc_id": "680d1a2b3c4d5e6f7a8b9c0d",
          "source_url": "https://example.com/qa_updated.csv",
          "file_name": "qa_data_v2.csv"
        }
      ]
    }'
```

## **Request Headers**

| Field           | Type             | Description                                                                 |
|-----------------|------------------|-----------------------------------------------------------------------------|
| Authorization   | Bearer ${token}  | Use Authorization: Bearer ${token} for authentication. Get your token from the API key page. |
| Content-Type    | application/json | Data type, value should be application/json.                                |

## **Request Body**

| Field              | Type   | Required      | Description                                                                                           |
|--------------------|--------|--------------|-------------------------------------------------------------------------------------------------------|
| doc_id             | string | Conditionally | Document id, required when updating QA text using qaList.                                             |
| knowledge_base_id  | string | No           | Knowledge base id.                                                                                    |
| qaList             | list   | Conditionally | QA pair list, will completely replace all QA pairs under this document. Choose either qaList or files.|
| files              | list   | Conditionally | File list, up to 20 files. Choose either qaList or files.                                             |
| header_row         | int    | No           | Header row number.                                                                                    |
| chunk_token        | int    | No           | Number of chunk tokens, default is 600.                                                               |
| splitter           | string | No           | Delimiter.                                                                                            |

When using qaList to update, all QA pairs under the target document will be completely replaced. Please ensure you provide the complete QA list.

qaList and files are mutually exclusive, and cannot both be empty.

## **Response**

### **Response Example**

```
{
    "doc": [
        {
            "doc_id": "680d1a2b3c4d5e6f7a8b9c0d",
            "doc_name": "FAQ"
        }
    ],
    "failed": []
}
```

### **Success Response**

| Field | Type | Description                       |
|-------|------|-----------------------------------|
| doc   | list | List of successfully updated docs. |
| failed| list | List of file names that failed to update. |

### **Failure Response**

| Field   | Type   | Description            |
|---------|--------|------------------------|
| code    | int    | Error code.            |
| message | string | Error description.     |

### **Error Codes**

| Code   | Message                |
|--------|------------------------|
| 40000  | Parameter error        |
| 50000  | Internal system error  |
