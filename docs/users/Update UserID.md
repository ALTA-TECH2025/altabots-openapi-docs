_Last updated at: 2025-12-01_

# **Update User Attributes**

Batch update one or more user attributes to improve profiling, segmentation, and personalization.

## **Request Method**

POST

## **Request URL**

`https://altatech.ai/v1/property/update`

## **Request Authentication**

See Overview for authentication steps.

## **Request**

### **Request Example**

```
curl -X POST "https://altatech.ai/v1/property/update" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{
        "user_id": "example_user_id",
        "property_values": [
          {
            "property_name": "example_property_name",
            "value": "example_value"
          }
        ]
      }'
```

### **Request Headers**

| Field | Type | Description |
| :---- | :---- | :---- |
| Authorization | Bearer {token} | Use `Authorization: Bearer {token}` for authentication. |
| Content-Type | application/json | Request payload format. |

### **Request Body**

| Field | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| user_id | string | Yes | The user whose attributes will be updated. |
| property_values | list | Yes | Collection of attribute updates. |
| property_values.property_name | string | Yes | Attribute key. |
| property_values.value | object | Yes | Attribute value (string, number, boolean, etc.). |

## **Response**

### **Response Example**

```
{
  "success_update": [
    {
      "property_name": "vip_level",
      "value": "gold"
    }
  ],
  "fail_update": [
    {
      "property_name": "last_purchase",
      "value": "2025-11-15"
    }
  ]
}
```

### **Response Body**

| Field | Type | Description |
| :---- | :---- | :---- |
| success_update | array | Attributes that were updated successfully. |
| success_update.property_name | string | Name of the updated field. |
| success_update.value | object | Value written to the field. |
| fail_update | array | Attributes that failed to update. |
| fail_update.property_name | string | Field name that failed. |
| fail_update.value | object | Value that was rejected. |