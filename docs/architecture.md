# Architecture

## Goal

Create a trusted, repeatable workflow that transforms a client brief into a source-backed, brand-compliant immersion document while preserving human review and internal confidentiality.

## High-level architecture

### 1. Client brief intake

The workflow starts with structured inputs:

- client name
- website or public profile
- geography
- target audience
- purpose of the document
- as-of date
- desired depth or level of detail
- optional prior version or approved template

The system validates the data and asks for clarification when the entity or objective is ambiguous.

### 2. Entity resolution and industry classification

This service identifies the likely organization and classifies the company into a relevant industry or subsector.

Inputs:
- client name
- website
- geographic and market context
- related keywords or known aliases

Outputs:
- canonical client entity
- confidence score
- industry classification
- rationale and supporting evidence references
- required reviewer confirmation when confidence is low

### 3. Research orchestration

The system coordinates approved search and retrieval tasks.

Responsibilities:
- define the search plan,
- select relevant public sources,
- fetch and normalize metadata,
- rank sources by quality and relevance,
- store evidence snapshots,
- flag gaps and contradictory information.

### 4. Outline and table-of-contents generator

The TOC engine creates a draft document structure based on:

- industry and company type,
- audience and use case,
- business context and strategic questions,
- document length or depth requirements.

The generated outline is editable. Analysts can remove or reorder sections before drafting begins.

### 5. Grounded section generation

Section drafting is evidence-driven.

The system:
- groups retrieved evidence by section,
- assembles a summary with source-backed reasoning,
- attaches citations or source references to each factual claim,
- inserts placeholders where evidence is missing or internal-only facts are required,
- clearly marks speculative or secondary analysis.

### 6. Internal placeholder framework

This layer separates public research from confidential organization information.

Example placeholder categories:
- account relationship status,
- strategic priorities,
- current initiatives,
- SWOT or internal risk notes,
- policy-sensitive or segmented data.

Each placeholder should specify:
- field name,
- owner,
- sensitivity,
- completion status,
- approver or review rubric.

### 7. Brand template registry

A template registry holds approved document styles, logos, colors, and layouts.

Template rules:
- use approved corporate branding,
- maintain section formatting consistency,
- standardize front matter, disclaimers, and references,
- support multiple output formats such as DOCX and PDF.

### 8. Review and approval pipeline

Human review remains required before external use.

Reviewers can:
- edit generated sections,
- accept or reject citations,
- add internal facts via an approved channel,
- resolve placeholders,
- approve or reject the document for export.

### 9. Refresh and versioning

Every generated document and section should be versioned.

The refresh engine can:
- update stale source content,
- identify changed market conditions,
- regenerate only affected sections,
- preserve approved edits,
- compare new and previous versions side by side.

## Data model

Key entities:

- Brief
- ClientEntity
- IndustryClassification
- ResearchPlan
- Source
- Evidence
- Section
- Placeholder
- Template
- BriefVersion
- ReviewDecision

## Security and governance

- public research must remain separate from confidential internal data,
- provider access must be allowlisted and logged,
- all retrievals must be timestamped and traceable,
- policy checks should identify unsupported claims and missing citations,
- exports should require an approval state before publication.

## Design principles

1. Grounded rather than hallucinated
2. Human-in-the-loop review
3. Privacy-aware internal data handling
4. Template and style consistency
5. Refreshable, versioned outputs
6. Source-traceable decisions

