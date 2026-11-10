# Knowledge Generator Automation Workflow

An AI-driven workflow to accelerate the creation of client immersion documents by combining public research, industry classification, table-of-contents generation, branded drafting, and review-friendly internal placeholders.

## Problem

Creating a client immersion document usually requires several disconnected steps:

- identifying the client and industry context,
- researching the market, competitors, and recent developments,
- deciding what should be included in the document,
- drafting a polished narrative,
- inserting internal facts and stakeholder context responsibly,
- maintaining a consistent brand voice,
- refreshing the document over time without starting from scratch.

This process is time-intensive and often inconsistent from one analyst to the next.

## Solution

This workflow automates the repetitive parts while keeping human review in the loop:

1. Ingest a client brief and source inputs.
2. Identify or confirm the client and likely industry/sub-industry.
3. Recommend a tailored document structure and table of contents.
4. Collect reliable public information from approved sources.
5. Draft section content with traceable citations and evidence markers.
6. Insert placeholders for internal data that cannot be sourced publicly.
7. Apply the approved brand template and tone.
8. Version the output and support refreshes when the market changes.

## Core capabilities

### 1. Client and industry identification

- Accept a client name, website, geography, and target audience.
- Resolve the correct entity where possible.
- Suggest a likely industry/sub-industry and confidence score.
- Flag low-confidence matches for manual confirmation.

### 2. Customizable TOC generation

- Build an outline based on the client category, audience, and purpose.
- Include section types such as market overview, competitive context, product/operations, technology, regulatory landscape, and stakeholder questions.
- Allow analysts to edit, reorder, or remove sections before publication.

### 3. Public-source research orchestration

- Search approved sources such as:
  - company websites and investor relations pages,
  - industry reports,
  - public filings,
  - regulatory publications,
  - credible news and analyst commentary,
  - public datasets and government information.
- Rank sources by authority, recency, relevance, and corroboration.
- Store source metadata and timestamps for review.

### 4. Grounded content generation

- Draft sections using only approved evidence and internal approved facts.
- Attach citation metadata to claims.
- Clearly label opinions, hypotheses, estimates, and open questions.
- Avoid unsupported assertions or fabricated sources.

### 5. Internal placeholder management

- Insert explicit placeholders such as:
  - `[INTERNAL: strategic priority]`
  - `[INTERNAL: current account relationship]`
  - `[INTERNAL: revenue and pipeline summary]`
- Prevent confidential information from being guessed or inserted without review.
- Track placeholders by owner, sensitivity, and completion status.

### 6. Brand consistency and template control

- Apply approved document styles, headings, logos, and tone.
- Store templates and reusable blocks in a versioned registry.
- Ensure executive-ready output is consistent across documents and teams.

### 7. Refresh and versioning

- Save generation snapshots and document versions.
- Re-run source checks for updated reports and changes in the market.
- Highlight stale claims or changed evidence.
- Preserve approved edits while refreshing only the affected sections.

## Example workflow

```text
Client intake
   -> entity matching and industry classification
   -> tailored TOC proposal
   -> research plan and source selection
   -> evidence gathering and citation capture
   -> grounded section drafting
   -> internal placeholder insertion
   -> brand-aligned formatting
   -> human review and approval
   -> export + versioned refresh support
```

## Example document outline

1. Executive summary
2. Client profile and operating context
3. Industry structure and market position
4. Business model and value proposition
5. Strategy and recent developments
6. Products, services, and customer segments
7. Financial and operational indicators (public only)
8. Technology and data landscape
9. Risk, compliance, and regulatory context
10. Opportunities and discovery questions
11. Internal account context and placeholders
12. Sources, assumptions, and open questions

## Recommended system design

```text
User / reviewer workspace
   |
   v
Brief intake and configuration
   |
   v
Research orchestrator
   |-- entity resolution
   |-- industry classifier
   |-- source allowlist and fetch manager
   |-- evidence store
   |
   v
Grounded generation service
   |-- section drafting
   |-- citation mapping
   |-- placeholder insertion
   |
   v
Template registry and formatter
   |
   v
Review + approval workflow
   |
   v
Export, versioning, and refresh engine
```

## Suggested stack

A practical MVP can use:

- Frontend: React or a simple server-rendered UI
- API: Python with FastAPI
- Database: PostgreSQL
- Storage: object storage or file system for exports
- Search and retrieval: provider-agnostic connector layer
- LLM orchestration: model abstraction with policy controls
- Document output: DOCX/PDF generation with brand templates

## MVP product requirements

- User can start a brief from client name and context.
- System proposes a likely industry category with justification.
- System creates a recommended table of contents for the client and audience.
- Public-source research is compiled with source metadata and citations.
- Document sections are generated from evidence, not unsupported assumptions.
- Internal missing facts appear as explicit placeholders.
- Document uses a versioned brand template.
- Revisions can refresh stale content while preserving approved edits.
- Human review and approval is required before external distribution.

## Success metrics

- Time to first reviewable draft
- Number of claims with valid citations
- Source quality and freshness score
- Human edit rate after draft generation
- Documentation refresh effort reduction
- Percentage of placeholders resolved internally

## Repo structure

```text
README.md
/docs/
  architecture.md
  requirements.md
  roadmap.md
/src/
  research/
  generation/
  templates/
  placeholders/
  refresh/
/tests/
```

## Next steps

This repository should evolve from a concept into an MVP with:

1. brief intake and validation,
2. industry classification service,
3. source allowlist and evidence retrieval,
4. section drafting with citations,
5. placeholder management and approval workflow,
6. branded export and refresh mechanism.

This is best implemented as a controlled, auditable workflow rather than a fully autonomous document generator.

## License

TBD

