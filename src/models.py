from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional, List


class BriefRequest(BaseModel):
    client_name: str = Field(..., description="Client or organization name")
    website: Optional[str] = Field(None, description="Optional company website")
    geography: Optional[str] = Field(None, description="Geography or market region")
    audience: Optional[str] = Field(None, description="Primary audience for the document")
    purpose: Optional[str] = Field(None, description="Purpose or use case")
    as_of_date: Optional[str] = Field(None, description="As-of date for the brief")
    desired_depth: Optional[str] = Field("standard", description="Depth of the document")


class IndustrySuggestion(BaseModel):
    industry: str
    sub_industry: Optional[str] = None
    confidence: float
    rationale: str


class ResearchSource(BaseModel):
    title: str
    publisher: str
    url: str
    source_type: str
    published_date: Optional[str] = None
    retrieved_at: Optional[str] = None
    reliability: str = "medium"


class GeneratedSection(BaseModel):
    title: str
    content: str
    source_urls: List[str] = []
    placeholders: List[str] = []


class BriefResponse(BaseModel):
    client_name: str
    industry: IndustrySuggestion
    table_of_contents: List[str]
    sources: List[ResearchSource]
    sections: List[GeneratedSection]
    internal_placeholders: List[str]

