# Changelog

## V1.2 · 2025-12-01
- Updated four user-related API documents: 
  'User Management', 'Set User ID', 'Update User Attributes', 'Query User Attributes', 
  with unified headers, tables, and request/response sections.

## V1.3 · 2025-12-15
- Updated workflow-related APIs, including 'Workflow Execution' and 'Query Workflow Result'
- Upgraded 'Get Conversation Message Detail' API to a newer version with enhanced response content
- Enhanced 'Send Message' API to support custom agent behavior via 'custom_variables'

## V1.4· 2026-01-19
- Added Set UserID V2 API, Workflow Execution V2 ,Query User CDP API
- Deprecated legacy Set UserID API documentation, replaced by Set UserID V2;
- Deprecatedlegacy Workflow Execution API documentation, replaced by Workflow Execution V2.
- 
## V1.5· 2026-03-27
- Updated Send Message V2 API to provide more structured and detailed agent responses, including referenced knowledge sources and utilized tools.

## V1.6 · 2026-07-09
- Full sync against the upstream API reference: URL paths across every category now mirror the upstream slug structure (e.g. `conversation-api/send-message-v2`, `knowledge-base-api/get-knowledge-base-list`).
- Renamed "Conversation API" section to "Agent API" and "Speech API" section to "Models API" to match upstream naming; URL folders (`conversation-api/`, `models-api/`) are unchanged.
- Moved "Get Agent Conversation Credit Consumption List" and "Get Workflow Run Credit Consumption List" from the Workflow API section into the Analytics API section to match upstream categorization.
- Added new API pages: Webhook Detection Service, Agent Test, Query LogTree (Agent API); Create Knowledge Base (Knowledge API); Workflow Test (Workflow API); List Database Tables (Database API).
- Added `anonymous_id` support to Create Conversation, Get Conversation List, and Webhook receives messages.
- Updated Vector Similarity Matching with new `group_ids`, `rerank_version`, and `doc_correlation` parameters and a `document_name` response field.
- Updated Voice to Text endpoint URL and added `user_email`/`user_phone` fields to Query User CDP.
- Refreshed field length limits on Create Database Table and clarified filter/is_create behavior on Retrieve Table Data and Update Table Data.
- Swept all example content for leftover Simplified Chinese/mainland terminology and non-AltaBots domains.
