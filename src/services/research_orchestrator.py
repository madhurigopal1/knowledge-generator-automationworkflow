from __future__ import annotations

from typing import List

DEFAULT_SOURCES = [
    {
        "title": "Company overview",
        "publisher": "Official company website",
        "url": "https://example.com/company-overview",
        "source_type": "corporate",
        "published_date": None,
        "reliability": "high",
    },
    {
        "title": "Industry profile",
        "publisher": "Industry association",
        "url": "https://example.com/industry-profile",
        "source_type": "industry",
        "published_date": None,
        "reliability": "high",
    },
    {
        "title": "Public market or regulatory update",
        "publisher": "Public regulator or reporting authority",
        "url": "https://example.com/regulatory-update",
        "source_type": "regulatory",
        "published_date": None,
        "reliability": "high",
    },
]


def get_research_sources(client_name: str, industry: str) -> List[dict]:
    return [
        {
            **source,
            "title": f"{source['title']} — {client_name}",
            "url": source["url"].replace("example.com", f"{client_name.lower().replace(' ', '-')}.example.com"),
            "source_type": source["source_type"],
        }
        for source in DEFAULT_SOURCES
    ]

