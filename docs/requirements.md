# Product requirements

## Vision

Provide a workflow that helps account teams, consulting teams, and analysts create client immersion documents faster while improving accuracy, source traceability, and consistency with brand guidance.

## User personas

### Account or consulting lead
- needs a fast, credible summary before a meeting or proposal,
- wants a tailored outline instead of a generic brief,
- needs a versioned document that can be refreshed over time.

### Analyst or researcher
- needs structured source gathering,
- wants a workflow that reduces manual research effort,
- needs citations and evidence markers rather than unsupported narrative.

### Brand or knowledge manager
- needs consistent templates and approved language,
- wants controlled internal placeholders,
- requires governance over what is external vs. internal.

## Functional requirements

### Core workflow
- Start a brief by entering client metadata and research objective.
- Confirm or correct the client entity and industry subtype.
- Receive a recommended outline or table of contents.
- Generate a research plan using allowlisted public sources.
- Draft sections from evidence and flag unsupported or missing information.
- Insert placeholders for internal-only facts.
- Export a branded document in approved formats.

### Research requirements
- Allowlist and prioritize credible public sources.
- Capture publication date, retrieval timestamp, and target URL.
- Store evidence with source reliability and relevance scores.
- Mark low-confidence or contradictory sources.

### Content generation requirements
- Distinguish facts from hypotheses and opinions.
- Add citations to each claim or section where feasible.
- Explicitly label unresolved data as placeholders or open questions.
- Use version-aware generation metadata.

### Review requirements
- Allow manual edits at section level.
- Review citation quality and source integrity.
- Approve or reject document versions.
- Record changes across versions.

### Refresh requirements
- Refresh sources based on revised dates and new publications.
- Rebuild only updated sections where possible.
- Preserve accepted content and note changed facts.

## Non-functional requirements

- Access controls for internal content and approvals
- Rate limits for external research integrations
- Auditable generation and review logs
- Template governance and version locks
- Explainability for generated recommendations
- Clear separation of public and internal data

## Acceptance criteria

1. A user can initiate a brief and confirm the client entity.
2. The system recommends a tailored TOC based on the client and purpose.
3. Research output is linked to trusted sources and timestamps.
4. Unsupported claims are either cited or shown as placeholders.
5. Final output conforms to a selected brand template.
6. Refreshing the document highlights stale content and preserves approved edits.
7. A reviewer must approve the exported document for external use.

## Out of scope for MVP

- fully autonomous external publishing,
- unrestricted web scraping,
- unrestricted model access to sensitive internal data,
- unmanaged use of unsupported citations,
- automatic acceptance of generated content without review.

