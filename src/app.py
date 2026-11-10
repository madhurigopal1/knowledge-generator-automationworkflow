from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.models import BriefRequest, BriefResponse
from src.services.industry_classifier import classify_industry, suggest_toc
from src.services.research_orchestrator import get_research_sources
from src.services.generation_service import draft_sections_for_brief

app = FastAPI(title="Knowledge Generator Automation Workflow")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/briefs/create", response_model=BriefResponse)
def create_brief(request: BriefRequest):
    classification = classify_industry(request.client_name, request.website, request.geography)
    toc = suggest_toc(classification["industry"], request.audience, request.purpose)
    sources = get_research_sources(request.client_name, str(classification["industry"]))
    sections = draft_sections_for_brief(request.client_name, str(classification["industry"]), toc)

    placeholders = [
        "[INTERNAL: current account relationship]",
        "[INTERNAL: strategic priorities and roadmap]",
        "[INTERNAL: confidential customer or revenue context]",
    ]

    return BriefResponse(
        client_name=request.client_name,
        industry={
            "industry": str(classification["industry"]),
            "sub_industry": str(classification["sub_industry"]),
            "confidence": float(classification["confidence"]),
            "rationale": str(classification["rationale"]),
        },
        table_of_contents=toc,
        sources=sources,
        sections=sections,
        internal_placeholders=placeholders,
    )


@app.exception_handler(Exception)
def handle_exception(_request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": str(exc)})

