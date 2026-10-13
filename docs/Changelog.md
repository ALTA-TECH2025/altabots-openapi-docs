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
- Added new API pages: Webhook Detection Service, Agent Test, Query LogTree (Agent API); Create Knowledge Base (Knowledge API); Workflow Test (Workflow API); List Database Tables (Database API).
- Added `anonymous_id` support to Create Conversation, Get Conversation List, and Webhook receives messages.
- Updated Vector Similarity Matching with new `group_ids`, `rerank_version`, and `doc_correlation` parameters and a `document_name` response field.
- Updated Voice to Text endpoint URL and added `user_email`/`user_phone` fields to Query User CDP.

## V1.7 · 2026-07-22
- Added Get Metadata Field List API (Knowledge API).
- Added Get Doc Metadata, Create Metadata Field, Edit Metadata Field, Delete Metadata Field, and Update Doc Metadata Value APIs (Knowledge API / Metadata API).

## V1.8 · 2026-10-13
- Added Agent version management APIs (Import, Publish, Query Version List, Rollback) and Agent Skill APIs (Create, Update) (Agent API).
- Added Workflow version management APIs (Import, Publish, Query Version List, Rollback) and Get Workflow Run List (Workflow API).
- Added Sync Knowledge Base API (Knowledge API).
- Added Account API pages: Import Agent / Workflow and precheck, Query Organization List, Create API Key, Organization Skill management, Tool & MCP management, and Query Model List.
- Send Message: added human handoff support (`human_agent` role, `human_agent_info`, `human_trigger` / `handoff` response fields, streaming codes 36 and 107), plus `is_process_result` and `ai_response` parameters.
- Get Conversation List: added `source_page` and `quality_score` response fields; `total` now returns the total number of matching conversations.
- Add Q&A / Text / Spreadsheet Docs: added optional `embedding_model_version_id` parameter.
