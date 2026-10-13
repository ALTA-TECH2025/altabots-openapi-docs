_Last updated at: 2026-10-13_

# **Query Organization List**

Query the list of organizations accessible to the account that the current developer key belongs to.

## **Request Method**

GET

## **Request URL**

`https://altatech.ai/v1/org/list`

## **Request Authentication**

Uses account-level DevKey / DevSecret Basic authentication.

## **Request**

### **Request Example**

```
curl -X GET 'https://altatech.ai/v1/org/list' \
-H 'Authorization: Basic ${BASIC_TOKEN}'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Basic ${BASIC\_TOKEN} | The Basic Token obtained by Base64-encoding `DevKey:DevSecret`. |

### **Request Parameters**

None.

## **Response**

### **Response Example**

```
{
  "code": 0,
  "message": "OK",
  "data": [
    {
      "org_id": "p-xxxx",
      "org_name": "Demo Org",
      "is_owner": true
    }
  ]
}
```

### **Success Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| org\_id | String | Organization ID, which must be passed in subsequent organization resource endpoints. |
| org\_name | String | Organization name. |
| is\_owner | Boolean | Whether the current account is the owner of the organization. |

### **Failure Response**

| Field | Type | Description |
| :---- | :---- | :---- |
| code | Integer | Error code. |
| message | String | Error details. |

### **Status Codes**

| Status Code | Description |
| :---- | :---- |
| 200 | Success |
| 400 | Parameter error |
| 401 | Unauthorized |
| 403 | Insufficient permissions |
| 429 | Too many requests |
| 500 | Server error |
