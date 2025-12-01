

# 

# 

# **AltaBots.ai Open API Documentation**

| Version | Release Date |
| :---- | :---- |
| 1.0 | 2025/05 |
| 1.1 | 2025/10 |
| 1.2 | 2025/12 |

# **API Reference Overview**

The AltaBots API allows you to programmatically interact with your AI agents, manage conversations, access knowledge bases, and integrate AltaBots capabilities into your own applications and systems.

## **API Basics**

### **Base URL**

All API requests should be made to:

```
https://altatech.ai/
```

### **Authentication**

All API requests require authentication via an API key.

#### **How to Generate an API Key**

* **For Agent-related usage**  
   Navigate to: `Agent > Integrations > API Key` in your AltaBots dashboard to create an API key specific to the Agent you are working with.

```
Authorization: Bearer YOUR_API_KEY
```

### **Request Format**

Most API endpoints accept JSON-encoded request bodies. Make sure to include the following header in your requests:

```
Content-Type: application/json
```

### **Response Format**

All responses are returned in JSON format. A typical response structure includes:

```
{
  "data": { ... },  // The response data
  "meta": { ... },  // Metadata about the response
  "links": { ... }  // Links for pagination or related resources
}
```

### **Error Handling**

When an error occurs, the API returns an appropriate HTTP status code and a JSON response with error details:

```
{
  "error": {
    "code": "error_code",
    "message": "A human-readable error message",
    "status": 400  // The HTTP status code
  }
}
```

## **Rate Limits**

API rate limits vary by subscription plan:

* Free Tier: 100 requests per day  
* Professional: 1,000 requests per hour  
* Enterprise: Custom limits based on contract

Rate limit information is included in the response headers:

* X-RateLimit-Limit: The maximum number of requests allowed in the current period  
* X-RateLimit-Remaining: The number of requests remaining in the current period  
* X-RateLimit-Reset: The time when the rate limit will reset (Unix timestamp)

## **API Categories**

The AltaBots API is organized into several categories:

* Conversation API: Manage conversations with AI agents  
* Agent API: Create and manage AI agents  
* Knowledge Base API: Manage knowledge bases and their content  
* Analytics API: Access usage and performance data  
* User API: Manage user profiles and attributes  
* Webhook API: Configure and manage webhooks for events

## **Getting Started**

To get started with the AltaBots API:

1. Generate an API key in your AltaBots dashboard  
2. Choose the API endpoints that match your use case  
3. Make test requests using the provided examples  
4. Implement error handling in your application  
5. Monitor your usage to stay within rate limits

The following sections provide detailed documentation for each API endpoint, including request parameters, response formats, and example code.  
