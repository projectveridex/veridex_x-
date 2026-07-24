"""
VERIDEX X
GitHub Live Hunter
"""

import requests


class Opportunity:

    def __init__(self, title, source, url, description=""):

        self.title = title
        self.source = source
        self.url = url
        self.description = description


SEARCH_TERMS = [
    "wordpress bug",
    "help wanted",
    "good first issue",
    "python automation",
    "website fix"
]


def scan_github_live():

    opportunities = []

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "VERIDEX-X"
    }

    for term in SEARCH_TERMS:

        url = (
            "https://api.github.com/search/issues"
            f"?q={term}+state:open"
        )

        try:

            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            if response.status_code != 200:
                continue

            data = response.json()

            for item in data.get("items", [])[:5]:

                opportunities.append(

                    Opportunity(
                        title=item["title"],
                        source="GitHub",
                        url=item["html_url"],
                        description=item.get("body", "")[:200]
                    )

                )

        except Exception:
            continue

    return opportunities
