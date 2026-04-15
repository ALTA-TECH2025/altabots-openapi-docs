_Last updated at: 2025-10-20_

## **Add QA to Knowledge Document**

You can use this API to add QA pairs to the Agent knowledge base. Three methods are supported: directly passing QA text, uploading a QA format file (CSV), or uploading a document to be automatically converted into QA pairs.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/bot/doc/qa/add`

## **Authentication**

See the authentication method description in the API Overview.

## **Request Examples**

**QA Text Method:**
```
curl -X POST https://altatech.ai/v1/bot/doc/qa/add \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json' \
  -d '{
      "purpose": "QA_TEXT",
      "name": "FAQ",
      "knowledge_base_id": "673af861ed69656ac0895b07",
      "qaList": [
        {
          "question": "How to register an account?",
          "answer": "Click the register button at the top right corner of the homepage, fill in your email and password to complete registration."
        },
        {
          "question": "How to reset the password?",
          "answer": "Click forgot password on the login page and follow the instructions to reset."
        }
      ]
    }'
```

**QA File Method:**
```
curl -X POST https://altatech.ai/v1/bot/doc/qa/add \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json' \
  -d '{
      "purpose": "QA_FILE",
      "knowledge_base_id": "673af861ed69656ac0895b07",
      "files": [
        {
          "file_url": "https://example.com/qa.csv",
          "file_name": "qa_data.csv"
        }
      ]
    }'
```

**Document to QA Method:**
```
curl -X POST https://altatech.ai/v1/bot/doc/qa/add \
  -H 'Authorization: Bearer your_apikey' \
  -H 'Content-Type: application/json' \
  -d '{
      "purpose": "FILE_2_QA",
      "knowledge_base_id": "673af861ed69656ac0895b07",
      "files": [
        {
          "source_url": "https://example.com/product_manual.pdf",
          "file_name": "Product_Manual.pdf"
        }
      ]
    }'
```

## **Request Headers**

| Field          | Type                | Description                                                                 |
|----------------|---------------------|-----------------------------------------------------------------------------|
| Authorization  | Bearer ${token}     | Use Authorization: Bearer ${token} for authentication. Get your token from the API key page. |
| Content-Type   | application/json    | Data type, value should be application/json.                                |

## **Request Body**

| Field              | Type    | Required      | Description                                                                                  |
|--------------------|---------|--------------|----------------------------------------------------------------------------------------------|
| purpose            | string  | Yes          | Data type, options: QA_TEXT (QA text), QA_FILE (QA format file), FILE_2_QA (document to QA). |
| knowledge_base_id  | string  | No           | Knowledge base id. If not provided, the default knowledge base is used.                      |
| name               | string  | Conditionally| Document name, required when purpose is QA_TEXT.                                             |
| qaList             | list    | Conditionally| QA pair list, required when purpose is QA_TEXT.                                              |
| files              | list    | Conditionally| File list, required when purpose is QA_FILE or FILE_2_QA. Maximum 20 files.                  |
| header_row         | int     | No           | Header row number.                                                                           |
| chunk_token        | int     | No           | Number of tokens per chunk, default is 600.                                                  |
| splitter           | string  | No           | Separator.                                                                                   |

- When purpose is QA_TEXT, you must provide name and qaList.
- When purpose is QA_FILE or FILE_2_QA, you must provide files, up to 20 files.

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

### **Successful Response**

| Field   | Type | Description                           |
|---------|------|---------------------------------------|
| doc     | list | List of successfully added documents. |
| failed  | list | List of file names that failed to add.|

### **Failed Response**

| Field   | Type | Description            |
|---------|------|------------------------|
| code    | int  | Error code.            |
| message | string | Error description.   |

## **Error Codes**

| Code   | Message                |
|--------|------------------------|
| 40000  | Parameter error        |
| 50000  | Internal system error  |
