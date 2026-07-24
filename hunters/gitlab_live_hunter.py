"""
VERIDEX X
GitLab Live Hunter
"""

import requests

from core.opportunity import Opportunity


def scan_gitlab_live():

    opportunities = []

    terms = [
        "help wanted",
        "bug fix",
        "automation"
    ]

    for term in terms:

        try:

            response = requests.get(
                "https://gitlab.com/api/v4/issues",
                params={
                    "search": term,
                    "state": "opened"
                },
                timeout=10
            )

            if response.status_code != 200:
                continue

            for issue in response.json()[:5]:

                opportunities.append(
                    Opportunity(
                        title=issue.get(
                            "title"
                        ),
                        source="GitLab",
                        url=issue.get(
                            "web_url",
                            ""
                        ),
                        description=issue.get(
                            "description",
                            ""
                        )[:200]
                    )
                )

        except Exception:
            continue

    return opportunities
