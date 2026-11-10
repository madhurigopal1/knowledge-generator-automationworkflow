from __future__ import annotations

from typing import List


def draft_sections_for_brief(client_name: str, industry: str, toc: List[str]) -> List[dict]:
    sections = []
    for idx, section in enumerate(toc[:6], start=1):
        content = (
            f"{section}: This section summarizes the current public context for {client_name} within the {industry} sector. "
            "It calls out operating context, strategic signals, and known public developments relevant to the client brief. "
            "Any confidential or internal-only details should be added through explicit placeholders rather than inferred data."
        )
        placeholders = []
        if "internal" in section.lower() or "strategic" in section.lower():
            placeholders.append("[INTERNAL: strategic priorities and account context]")
        sections.append({
            "title": section,
            "content": content,
            "source_urls": ["https://example.com/verified-source-1", "https://example.com/verified-source-2"],
            "placeholders": placeholders,
        })
    return sections

