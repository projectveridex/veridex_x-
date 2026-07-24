"""
VERIDEX X
GitHub Live Hunter
"""

import requests

from core.opportunity import Opportunity


SEARCH_TERMS = [
    "wordpress bug",
    "help wanted",
    "good first issue",
    "python automation"
]


def scan_github_live():

    opportunities = []

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "VERIDEX-X"
    }

    for term in SEARCH_TERMS:

        try:

            response = requests.get(
                "https://api.github.com/search/issues",
                params={
                    "q": f"{term} state:open"
                },
                headers=headers,
                timeout=10
            )

            if response.status_code != 200:
                continue

            for item in response.json().get("items", [])[:5]:

                opportunities.append(
                    Opportunity(
                        title=item["title"],
                        source="GitHub",
                        url=item["html_url"],
                        description=item.get(
                            "body",
                            ""
                        )[:200]
                    )
                )

        except Exception:
            continue

    return opportunities
