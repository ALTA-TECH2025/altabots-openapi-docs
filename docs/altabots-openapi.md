

# 

# 

# **AltaBots.ai Open API Documentation**

| Version | Release Date |
| :---- | :---- |
| 1.0 | 2025/05 |
| 1.1 | 2025/10 |
| 1.2 | 2025/12 |
| 1.3 | 2025/12 |
| 1.4 | 2026/01 |
| 1.5 | 2026/03 |
| 1.6 | 2026/07 |

# **API Reference Overview**

The AltaBots API is designed to comply with HTTP and REST specifications. Query requests use the GET method, while submission requests use the POST method. An error will be returned if a request does not use the appropriate HTTP method.

Unless otherwise specified, parameter values should be encoded in UTF-8 with URL encoding.

## **Authentication**

The AltaBots REST API uses HTTP Bearer Authentication. Add the following `Authorization` header:

```
Authorization: Bearer ${API_Key}
```

### **API Activation**

To enable the API service, go to the AltaBots dashboard, navigate to "Agent Integration", select "Development - API Service", and click the "Enable" button to activate the API service.

After enabling the API service, click on the "API" card to enter the API management page. Click the "Create APIKey" button to generate an APIKey that can be used to call AltaBots APIs.

## **API Base URL**

All API requests should be made to:

```
https://altatech.ai/
```

## **API Categories**

The AltaBots platform provides a comprehensive set of API interfaces to meet developers' business needs. Developers can choose suitable APIs based on their requirements. The API categories are as follows:

| API Category | Description |
| :---- | :---- |
| Agent API | Interact and converse with Agents through this API. |
| Workflow API | Send requests and receive responses from workflows through this API. |
| Knowledge API | Manage knowledge bases on the AltaBots platform through this API. |
| Database API | Manage databases on the AltaBots platform through this API. |
| Models API | Access various model capabilities of the AltaBots platform through this API. |
| User API | Configure user information, attributes, and contact details through this API. |
| Analytics API | Query usage data for credits and tokens through this API. |
| Account API | Retrieve information about Agents, organizations, etc. under the account through this API. |

## **Response Format**

All responses are returned in JSON format. A typical success response includes the fields documented on each endpoint's page. When an error occurs, the API returns an appropriate HTTP status code together with a JSON body containing error details:

```
{
  "code": "error_code",
  "message": "A human-readable error message"
}
```

## **API Rate Limits**

The AltaBots platform implements rate limits for API calls, with different limits for different API categories. Exceeding these limits will result in a rate limit exceeded message. The specific limits are:

* **Free Plan**: All API types are limited to 3 requests per minute by default.
* **Enterprise Custom Plan**: Contact your AltaBots account representative to obtain customized API rate limit privileges.

## **Getting Started**

To get started with the AltaBots API:

1. Enable the API service and generate an API key in your AltaBots dashboard
2. Choose the API endpoints that match your use case
3. Make test requests using the provided examples
4. Implement error handling in your application
5. Monitor your usage to stay within rate limits

The following sections provide detailed documentation for each API endpoint, including request parameters, response formats, and example code.
