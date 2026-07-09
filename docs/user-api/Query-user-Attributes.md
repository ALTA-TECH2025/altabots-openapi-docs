_Last updated at: 2025-12-01_

# **Query User Attributes**

Allows developers to query user attributes by specifying user IDs or anonymous user IDs.

Supports batch queries of up to 100 user IDs or anonymous user IDs per request.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v2/user-property/query`


## **Request Authentication**

Please refer to Overview in API Reference.

## **Request**

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {API Key} | Authentication using Authorization: Bearer {API Key}. Obtain from API Keys page. |

### **Request Example**

```
curl -X GET "https://altatech.ai/v2/user-property/query?user_ids=681db9dd3f650a117cf60775&anonymous_ids=681db9dd3f650a117cf60775" \
  -H "Authorization: Bearer app-DFRHRwhSetxEx5yZoXhNDDKu" \
  -H "Content-Type: application/json"
```

### **Request Body**

| Parameter | Type | Description | Required |
| :---- | :---- | :---- | :---- |
| user_ids | string | User IDs to query attributes for | Required, mutually exclusive with anonymous_ids |
| anonymous_ids | string | Anonymous user IDs to query attributes for | Required, mutually exclusive with user_ids |

> Note: Either user_ids or anonymous_ids must be provided. If both are provided, user_ids will take precedence.

## **Response**

### **Example Response Body**

```
[
  {
    "user_id": "681db9dd3f650a117cf60775",
    "property_values": [
      {
        "propertyName": "id",
        "value": "1234"
      },
      {
        "propertyName": "name",
        "value": "Sarah"
      }
    ]
  },
  {
    "anonymous_id": "681db9dd3f650a117cf60775",
    "property_values": [
      {
        "propertyName": "id",
        "value": "1234"
      },
      {
        "propertyName": "name",
        "value": "Sarah"
      }
    ]
  }
]
```

### **Successful Response**

| Parameter | Type | Description |
| :---- | :---- | :---- |
| user_id | string | The queried user ID |
| anonymous_id | string | The queried anonymous user ID |
| property_values | list | List of user attributes and their values for the user_id |

### **Error Response**

| Parameter | Type | Description |
| :---- | :---- | :---- |
| code | int | Error code |
| message | string | Error message |

### **Status Codes**

| Status Code | Description |
| :---- | :---- |
| 200 | Success |
| 400 | Invalid Parameters |
| 401 | Unauthorized |
| 403 | Forbidden |
| 500 | Server Error |
| 503 | User ID Not Found |
| 504 | Anonymous User ID Not Found |
