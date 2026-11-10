# Knowledge Generator Automation Workflow

This repository contains a starter implementation for an AI-driven client immersion document workflow.

## Quick start

1. Create a virtual environment:
   python -m venv .venv
   source .venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run the API:
   uvicorn src.app:app --reload

4. Test the endpoint:
   curl -X POST http://localhost:8000/briefs/create \
     -H "Content-Type: application/json" \
     -d '{
       "client_name": "Contoso Health",
       "website": "https://contosohealth.example",
       "geography": "United States",
       "audience": "Executive leadership",
       "purpose": "Pre-meeting immersion document",
       "as_of_date": "2026-11-10",
       "desired_depth": "standard"
     }'

## Project goals

- Identify the likely client industry and create a tailored outline.
- Gather approved public-source context and capture metadata.
- Draft content with citations and placeholder tracking.
- Preserve brand consistency and support refreshes over time.

## Current starter implementation

The codebase includes a minimal FastAPI service that:

- accepts a brief request,
- performs a simple industry classification heuristic,
- proposes a table of contents,
- returns mock research sources,
- drafts preliminary sections with placeholder markers.

This is intentionally a lightweight MVP foundation rather than a production research stack.

