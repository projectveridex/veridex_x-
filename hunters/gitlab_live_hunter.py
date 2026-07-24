"""
VERIDEX X
GitLab Live Hunter
"""

import requests


def scan_gitlab_live():

    opportunities = []

    search_terms = [
        "help wanted",
        "good first issue",
        "bug fix",
        "automation"
    ]

    headers = {
        "User-Agent": "VERIDEX-X"
    }

    for term in search_terms:

        url = (
            "https://gitlab.com/api/v4/issues"
            f"?search={term}"
            "&state=opened"
        )

        try:

            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            if response.status_code != 200:
                continue

            issues = response.json()

            for issue in issues[:5]:

                opportunities.append({

                    "title": issue.get(
                        "title",
                        "Unknown GitLab Issue"
                    ),

                    "source": "GitLab",

                    "url": issue.get(
                        "web_url",
                        ""
                    ),

                    "description": issue.get(
                        "description",
                        ""
                    )[:200]

                })

        except Exception:
            continue

    return opportunities
