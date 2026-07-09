_Last updated at: 2025-10-20_

# **Query Status of Adding Table Data**

Use this API to query the processing status of tasks for adding table data.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/database/query/import-results`

## **Authentication**

Refer to the authentication method description in API Overview for details.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/database/query/import-results?ids=id1&ids=id2' \
--header 'Authorization: Bearer your_apikey'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use Authorization: Bearer {token} for authentication. Obtain the token from the API key page. |
| Content-Type | application/json | Data type, value is application/json. |

### **Query Parameters**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| ids | list | Yes | Collection of task IDs for adding data. |

## **Response**

### **Response Example**

```
[
    {
        "id": "68ec7ad3e307920f002648cd",
        "progress": 1,
        "status": "FAIL",
        "total_count": 4,
        "success_count": 0,
        "fail_count": 4,
        "fail_detail": [
            {
                "row": null,
                "row_number_start": 1,
                "row_number_end": 2,
                "fail_reason": "(1062, \"Duplicate entry '14' for key 'product_feed_090833.id'\")"
            },
            {
                "row": 2,
                "row_number_start": 0,
                "row_number_end": 0,
                "fail_reason": "`id` must be unique, but the value '14' is duplicated (first at row `1`)."
            },
            {
                "row": 4,
                "row_number_start": 0,
                "row_number_end": 0,
                "fail_reason": "`no` is required and must have a value; the current value is invalid or the property is missing. `no` must be unique, but the value is empty or the property is missing."
            }
        ]
    }
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| id | string | The unique ID of the task. |
| progress | int | Task progress percentage, ranging from 1 to 100. |
| status | string | Task status. `FAIL` means failure, `PENDING_PARSE` means the file is being parsed, and `AVAILABLE` means at least one record was successfully added. |
| total\_count | int | Total number of items processed. |
| success\_count | int | Number of successfully processed rows. |
| fail\_count | int | Number of failed rows. |
| fail\_detail | list | Details of failed objects and failure reasons. The system processes data in chunks of 10 rows by default. The error reason shown represents the first failure encountered within that chunk. |

### **Failed Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code. |
| message | string | Error details. |

### **Error Codes**

| Code | Message |
| :---- | :---- |
| 50000 | Internal system error |

How to Interpret the Response Information

1. **First Failure Scenario:**  
    If the imported data conflicts with the data already in the table, **none of the data will be imported**.

   * "fail\_count" will be equal to "total\_count".

   * "row" will show as null.

   * In this case, directly check "fail\_reason" to locate the issue.

   * "row\_number\_start" and "row\_number\_end" may not match the actual row numbers—please ignore them.

2. **Second Failure Scenario:**  
    If the imported data contains **internal conflicts**, the system will import the **first conflicting record** and **discard the second one**.

   * "row" will show the row number of the **second conflicting record**.

   * "row\_number\_start" and "row\_number\_end" will both be 0\.

3. **Other Failure Scenarios:**  
    If the imported data **violates format or content rules**, that record will not be imported.

   * "row" will show the row number of the invalid record.

   * "row\_number\_start" and "row\_number\_end" will both be 0\.

```
Status Code: 200
[
  {
    "id": "68ee001a7e0b4e6bce74cd6a",
    "progress": 100,
    "status": "AVAILABLE",
    "total_count": null,
    "success_count": 1,
    "fail_count": 1,
    "fail_detail": [
      {
        "row_number_start": 0,
        "row_number_end": 0,
        "fail_reason": "`no` is required and must have a value; the current value is invalid or the property is missing. `no` must be unique, but the value is empty or the property is missing."
      }
    ]
  }
]
```
