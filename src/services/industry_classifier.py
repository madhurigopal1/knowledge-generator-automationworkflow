from __future__ import annotations

from typing import Dict, List

INDUSTRY_KEYWORDS = {
    "Healthcare": ["health", "medical", "hospital", "clinic", "pharma", "biotech"],
    "Financial Services": ["bank", "insurance", "fintech", "capital", "payments"],
    "Retail": ["retail", "ecommerce", "commerce", "store", "marketplace"],
    "Technology": ["software", "platform", "cloud", "ai", "saas", "data"],
    "Manufacturing": ["manufacturing", "industrial", "factory", "supply", "logistics"],
    "Energy": ["energy", "oil", "gas", "utility", "renewables"],
    "Public Sector": ["government", "city", "county", "agency", "public"],
}


def classify_industry(client_name: str, website: str | None = None, geography: str | None = None) -> Dict[str, str | float | None]:
    text = f"{client_name} {website or ''} {geography or ''}".lower()
    scores: Dict[str, int] = {key: 0 for key in INDUSTRY_KEYWORDS}

    for industry, keywords in INDUSTRY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                scores[industry] += 1

    if not any(scores.values()):
        industry = "General business"
        sub_industry = "Cross-industry / mixed profile"
        confidence = 0.35
        rationale = "No strong industry keyword match was found in the provided client information."
    else:
        industry = max(scores, key=scores.get)
        sub_industry = "Industry signal inferred from client name and optional context"
        confidence = min(0.95, 0.55 + (scores[industry] * 0.1))
        rationale = f"The client profile contains signals associated with {industry}."

    return {
        "industry": industry,
        "sub_industry": sub_industry,
        "confidence": round(float(confidence), 2),
        "rationale": rationale,
    }


def suggest_toc(industry: str, audience: str | None = None, purpose: str | None = None) -> List[str]:
    base_sections = [
        "Executive summary",
        "Client profile and operating context",
        "Industry structure and market position",
        "Business model and value proposition",
        "Strategic priorities and recent developments",
        "Products, services, and customer segments",
        "Technology and data landscape",
        "Risk, regulatory, and market context",
        "Opportunities and discovery questions",
        "Sources, assumptions, and open questions",
    ]

    tailored = base_sections[:]
    if industry in {"Healthcare", "Financial Services", "Public Sector"}:
        tailored.insert(5, "Compliance and operating environment")
    if industry == "Retail":
        tailored.insert(5, "Customer experience and channel strategy")
    if industry == "Technology":
        tailored.insert(5, "Platform, data, and AI strategy")

    if audience and "executive" in audience.lower():
        tailored = ["Executive summary", "Key takeaways", "Strategic context", "Risk and opportunity review"] + [
            section for section in tailored if section not in {"Executive summary", "Key takeaways"}
        ]

    return tailored

