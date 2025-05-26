"""
Clinical data router for the APC API.

This file will define the routes for clinical data endpoints.
The actual business logic will be implemented in the corresponding service file.

Routes to implement:
- GET /apc/v2/get_soap_draft: Get a SOAP draft for a member
- POST /apc/soap/create_soap_draft: Create a SOAP draft for a member
- POST /apc/soap/get_soap_notes: Get SOAP notes for a member
- PUT /apc/soap/put_soap_note: Save a SOAP note
- POST /apc/get_soap_draft: Legacy endpoint for getting a SOAP draft
- POST /apc/get_clinical_assessments/ros_and_risk: Get clinical assessments for review of systems and risk scores
- POST /apc/get_clinical_assessments/daily_rounds: Get clinical assessments for daily rounds
- GET /apc/get_scores: Get scores for a member

This router will be registered with the '/apc' prefix in the main application.
"""

# This file contains only documentation of what will be implemented