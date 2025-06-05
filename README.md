# ALYF API Server Architecture

## Executive Summary

This document outlines the architecture for the ALYF API Server, implementing a modern, scalable, and maintainable system following the Function-First Model-Service-Controller (MSC) architecture pattern. This design prioritizes business domain cohesion while ensuring proper separation of concerns, optimizing for both developer productivity and system performance.


## Directory Structure

```
src/
├── apc/                      # APC-specific code (Provider-facing)
│   ├── auth/                 # Authentication-related endpoints
│   │   ├── models/           # Auth data models
│   │   ├── services/         # Auth business logic
│   │   └── controllers/      # Auth request handlers
│   ├── member_management/    # Member management functionality
│   ├── actions/              # Action endpoints
│   ├── vitals/               # Vitals-related endpoints
│   ├── reports/              # Report generation endpoints
│   ├── clinical/             # Clinical data endpoints
│   ├── annotations/          # Annotation-related endpoints
│   ├── external_events/      # External events functionality
│   └── visualization/        # Visualization endpoints
│
├── member/                   # Member-specific code
│   ├── profile/              # Member profile management
│   ├── vitals/               # Member vitals management
│   ├── auth/                 # Member authentication
│   ├── dashboards/           # Member dashboards
│   ├── feedback/             # Member feedback functionality
│   ├── summary/              # Summary endpoints
│   └── actions/              # Member actions
│
├── internal/                 # Internal API code
│   ├── provider_management/  # Provider management endpoints
│   ├── analytics/            # Analytics endpoints
│   ├── logging/              # Logging functionality
│   └── reports/              # Internal reports
│
└── main.py                   # Main application entry point
```

## Architecture Components

### MSC Pattern Implementation

Each functional area implements the Model-Service-Controller (MSC) pattern:

#### Models
- Define data structures and schemas
- Handle validation logic and type safety
- Implement serialization/deserialization
- Enforce data integrity constraints

#### Services
- Implement business logic independent of transport layer
- Handle data processing and transformations
- Manage interactions with databases and external systems
- Enforce business rules and policies
- Remain stateless and optimized for reuse

#### Controllers
- Handle HTTP request/response cycle
- Perform authentication and authorization checks
- Validate input data via models
- Delegate business logic to services
- Return appropriate responses and handle errors


## API Endpoints by Category

### APC (Provider-Facing) Endpoints

#### Authentication
- `POST /login`: Provider authentication (authenticate)
- `POST /login/validate_2fa`: Validate two-factor authentication (validate_2fa)
- `POST /login/resend_2fa`: Resend 2FA token (resend_2fa)
- `POST /forget_password`: Initiate password reset flow (forget_password)

#### Member Management
- `POST /member/add`: Add new member (apc_member_add)
- `POST /member/update`: Update member information (apc_member_update)
- `POST /actions/member`: Perform actions on members (apc_actions_member)
- `GET /v1/member/get`: Get member data (get_member_data)

#### Provider Configuration
- `POST /actions/provider`: Perform provider actions (apc_actions_provider)
- `POST /v2/actions/provider`: Enhanced provider actions (v2_apc_actions_provider)
- `POST /v1/apc/provider/config_update`: Update provider configuration (provider_config_update)
- `GET /meta_info`: Get metadata information (get_meta_info)
- `GET /provider/generate_signup_link`: Generate signup link (generate_signup_link)

#### Visualization
- `GET /adaptive_visualization/get_current_config`: Get current visualization config (adaptive_visualization_get_config)
- `POST /adaptive_visualization/validate_panel_config`: Validate panel configuration (adaptive_visualization_validate_panel_config)
- `GET /adaptive_visualization/member_dashboards`: Get member dashboards (adaptive_visualization_member_dashboards)
- `POST /adaptive_visualization/get_panel_config_proposal`: Get panel config proposal (adaptive_visualization_get_panel_config_proposal)
- `GET /adaptive_visualization/get_panel_config_proposal`: Get panel config proposal (adaptive_visualization_get_panel_config_proposal)
- `GET /adaptive_visualization/raw_llm_query`: Execute raw LLM query (adaptive_visualization_raw_llm_query)
- `POST /generate_n_vitals_panel_url`: Generate vitals panel URL (generate_n_vitals_panel_url)
- `POST /get_vitals`: Get detailed vitals (get_vitals_detail)

#### Clinical Assessments
- `GET /get_clinical_assessments/ros_and_risk`: Get ROS and risk assessments (apc_get_clinical_assessments_ros_and_risk)
- `GET /get_scores`: Get clinical scores (apc_get_scores)
- `POST /get_clinical_assessments/daily_rounds`: Get daily rounds assessments (apc_get_clinical_assessments_daily_rounds)
- `POST /vital_observations_timeseries`: Get vital observations timeseries (api_vital_observations_timeseries)
- `POST /vital_observations_aggregations`: Get vital observations aggregations (api_vital_observations_aggregations)
- `GET /apc/get_schema`: Get schema information (get_schema)
- `GET /apc/secure_query`: Execute secure query (secure_query)
- `GET /member/get_daily_recording_report`: Get daily recording report (apc_api_member_get_daily_recording_report)

#### SOAP Notes
- `GET /v2/get_soap_draft`: Get SOAP draft v2 (get_soap_draft_v2)
- `POST /soap/create_soap_draft`: Create SOAP draft (soap_create_draft)
- `POST /soap/get_soap_notes`: Get SOAP notes (soap_get_notes)
- `PUT /soap/put_soap_note`: Update SOAP note (soap_put_note)
- `POST /get_soap_draft`: Get SOAP draft (get_soap_draft)

#### AI Interaction
- `GET /v1/ask_alyf/get_message_history`: Get message history (get_message_history_endpoint)
- `DELETE /v1/apc/ask_alyf/clear_message_history`: Clear message history (clear_message_history)
- `GET /ask_alyf/get_message_history`: Get Alyf message history (ask_alyf_get_message_history)
- `GET /ask_alyf/clear_message_history`: Clear Alyf message history (ask_alyf_clear_message_history)
- `GET /ask_alyf/get_full_response`: Get full response from Alyf (ask_alyf_get_full_response)

#### Reports
- `POST /reports/rpm/refresh_reports`: Refresh RPM reports (reports_rpm_refresh_reports)
- `POST /reports/rpm/get_reports`: Get RPM reports (reports_rpm_get_reports)
- `GET /reports/member_admin/refresh_reports`: Refresh member admin reports (reports_member_admin_refresh_reports)
- `GET /reports/member_admin/get_reports`: Get member admin reports (reports_member_admin_get_reports)
- `GET /reports/member_admin/get_html_report`: Get member admin HTML report (reports_member_admin_get_reports)
- `POST /reports/billing/get_reports`: Get billing reports (reports_billing_get_reports)
- `POST /reports/member_data_analytics/get_reports`: Get member analytics reports (reports_member_analytics_get_reports)
- `POST /reports/provider_data_analytics/get_reports`: Get provider analytics reports (reports_provider_analytics_get_reports)

### Member-Facing Endpoints

#### Authentication
- `POST /v1/member/login`: Member login (member_login)
- `POST /v1/member/login_by_code`: Login by code (member_login_by_code)
- `POST /v1/member/reset_password`: Reset password (member_reset_password)

#### Profile Management
- `GET /v1/member/profile`: Get member profile (get_member_profile)
- `POST /v1/member/update_profile`: Update member profile (update_member_profile)
- `POST /v1/member/notifications/update_settings`: Update notification settings (update_notification_settings)

#### Vitals Management
- `POST /v1/member/set_vitals`: Set member vitals (set_member_vitals)
- `GET /v1/member/get_vitals`: Get member vitals (get_member_vitals)
- `POST /v1/member/{member_id}/set_vitals`: Set vitals for specific member (set_vitals_v2)
- `GET /external_events/get_events`: Get external events (external_events_get_events)
- `POST /external_events/create_events`: Create external events (external_events_create_events)
- `GET /external_events/create_event_from_plain_description`: Create event from description (external_events_create_event_from_plain_description)
- `GET /member/annotations/get`: Get annotations (get_annotations)
- `POST /member/annotations/add`: Add annotation (add_annotation)
- `POST /member/annotations/docs_for_smartplots`: Get docs for smartplots (docs_for_smartplots)

#### Communication
- `POST /v1/member/send_otp`: Send OTP (send_otp)
- `POST /v1/member/verify_otp`: Verify OTP (verify_otp)
- `GET /v1/member/notifications`: Get notifications (get_notifications)
- `POST /v1/member/notifications/mark_read`: Mark notifications as read (mark_notifications_read)

### Internal Endpoints

#### Provider Management
- `POST /internal/admin/create_provider`: Create provider (create_provider)
- `GET /internal/admin/get_provider`: Get provider (get_provider)
- `POST /internal/admin/update_provider`: Update provider (update_provider)

#### Relay Functionality
- `* /api/relay/{service}/{path:path}`: Relay request to another service (relay_request) 
