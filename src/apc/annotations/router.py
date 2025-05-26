"""
Annotations router for the APC API.

This file will define the routes for annotation-related endpoints within the APC module.
The actual business logic will be implemented in the corresponding service file.

Routes to implement:
- GET /apc/member/annotations/get: Get annotations
- POST /apc/member/annotations/add: Add annotation to a specific observation
- POST /apc/member/annotations/docs_for_smartplots: Documentation for smartplots

This router will be registered with the '/apc' prefix in the main application.
""" 