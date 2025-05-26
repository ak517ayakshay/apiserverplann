# API Server Reorganization Plan

## Overview

This reorganization plan addresses the issue of having all logic within router files by creating a modular, category-based structure. Each module is divided into subcategories based on functionality, with each subcategory containing its own router, service, and models.

## Directory Structure

```
src/
├── apc/                      # APC-specific code
│   ├── auth/                 # Authentication-related endpoints
│   ├── member_management/    # Member management functionality
│   ├── actions/              # Action endpoints (member/provider actions)
│   ├── vitals/               # Vitals-related endpoints
│   ├── reports/              # Report generation endpoints
│   ├── clinical/             # Clinical data endpoints (SOAP notes, etc.)
│   ├── annotations/          # Annotation-related endpoints
│   ├── external_events/      # External events functionality
│   └── visualization/        # Visualization and dashboard endpoints
│
├── member/                   # Member-specific code
│   ├── profile/              # Member profile management
│   ├── vitals/               # Member vitals management
│   ├── auth/                 # Member authentication
│   ├── dashboards/           # Member dashboards
│   ├── feedback/             # Member feedback functionality
│   ├── summary/              # Summary endpoints (clinical, admin)
│   └── actions/              # Member actions
│
├── internal/                 # Internal API code
│   ├── provider_management/  # Provider management endpoints
│   ├── analytics/            # Analytics endpoints
│   ├── logging/              # Logging functionality
│   └── reports/              # Internal reports
│
├── auth/                     # Authentication-related code
│   ├── provider_auth/        # Provider authentication
│   ├── member_auth/          # Member authentication
│   ├── token/                # Token management
│   └── middleware/           # Auth middleware
│
├── common/                   # Shared functionality
│   ├── utils/                # General utilities
│   ├── models/               # Shared data models
│   ├── services/             # Shared services
│   ├── middlewares/          # FastAPI middleware
│   └── validators/           # Input validation
│
└── main.py                   # Main application entry point
```

## Module Structure

Each subcategory will have the following structure:

```
subcategory/
├── router.py       # Route definitions only
├── service.py      # Business logic and data operations
└── models.py       # Data models (optional)
```

## Endpoint Mapping

### APC Endpoints

#### Auth
- `/apc/login`
- `/apc/login/validate_2fa`
- `/apc/login/resend_2fa`
- `/apc/forget_password`

#### Member Management
- `/apc/member/add`
- `/apc/member/update`
- `/apc/v1/member/get`

#### Actions
- `/apc/actions/member`
- `/apc/actions/provider`
- `/apc/v2/actions/provider`

#### Vitals
- `/apc/get_vitals`
- `/apc/vital_observations_timeseries`
- `/apc/vital_observations_aggregations`

#### Reports
- `/apc/reports/rpm/get_reports`
- `/apc/reports/rpm/refresh_reports`
- `/apc/reports/member_admin/get_reports`
- `/apc/reports/member_admin/refresh_reports`
- `/apc/reports/billing/get_reports`
- `/apc/reports/member_data_analytics/get_reports`
- `/apc/reports/provider_data_analytics/get_reports`

#### Clinical
- `/apc/v2/get_soap_draft`
- `/apc/soap/create_soap_draft`
- `/apc/soap/get_soap_notes`
- `/apc/soap/put_soap_note`
- `/apc/get_soap_draft`
- `/apc/get_clinical_assessments/ros_and_risk`
- `/apc/get_clinical_assessments/daily_rounds`
- `/apc/get_scores`

#### Annotations
- `/apc/member/annotations/get`
- `/apc/member/annotations/add`
- `/apc/member/annotations/docs_for_smartplots`

#### External Events
- `/apc/external_events/create_events`
- `/apc/external_events/get_events`
- `/apc/external_events/create_event_from_plain_description`

#### Visualization
- `/apc/adaptive_visualization/get_current_config`
- `/apc/adaptive_visualization/validate_panel_config`
- `/apc/adaptive_visualization/member_dashboards`
- `/apc/adaptive_visualization/get_panel_config_proposal`
- `/apc/adaptive_visualization/raw_llm_query`
- `/apc/generate_n_vitals_panel_url`

### Member Endpoints

#### Profile
- `/member/add`
- `/member/v2/add`
- `/member/update`
- `/member/get`
- `/member/v2/get`
- `/member/delete`

#### Vitals
- `/member/get_member_vitals`
- `/member/set_vitals`
- `/member/v2/{member_id}/set_vitals`
- `/member/vital_observations_aggregations`

#### Auth
- `/member/get_auth_url`
- `/member/v2/get_auth_link`
- `/member/v2/deauth`
- `/member/generate_otp`
- `/member/verify_otp`

#### Dashboards
- `/member/member_dashboards`
- `/member/v2/member_dashboards`

#### Feedback
- `/member/feedback`
- `/member/set_ama_info`

#### Summary
- `/member/v2/clinical_summary`
- `/member/v2/admin_summary`

#### Actions
- `/member/actions/member`

### Internal Endpoints

#### Provider Management
- `/internal/provider/show`
- `/internal/provider/add`
- `/internal/provider/delete`
- `/internal/provider/update`
- `/internal/provider/email_update`
- `/internal/provider/get_config`
- `/internal/provider/set_config`

#### Analytics
- `/internal/log_analytics`
- `/internal/member_analytics`

#### Logging
- `/internal/generic_logger`

#### Reports
- `/internal/reports/refresh_reports`

## Migration Strategy

1. Create the new directory structure
2. For each endpoint:
   - Create a router.py file in the appropriate subcategory directory
   - Create a service.py file with the business logic
   - Move the implementation from the original router file to the new service file
   - Update the router to use the new service
3. Update main.py to include the new routers
4. Test thoroughly to ensure functionality is preserved

## Files Per Subcategory

Each subcategory should contain:

1. `router.py` - Contains only route definitions and minimal request/response handling
2. `service.py` - Contains all business logic extracted from the original router
3. `models.py` (optional) - Contains subcategory-specific data models

## Naming Conventions

- Router files: `router.py`
- Service files: `service.py`
- Model files: `models.py`
- Utility files: descriptive name with `_utils.py` suffix (e.g., `validation_utils.py`) 